"""
Lookup Vendor given MAC Addresses in an input CSV file and output the same file with the new column for Manufacturer

Requirements:
    - pandas
    - requests

pip install pandas requests

Usage:
    python mac_vendor_lookup.py input.csv --output processed.csv
    
    Arguments:
        input.csv: Path to input CSV file
        --output: Optional output file path (default: output.csv)

Examples:
    python script.py dhcp_reservation_list.csv
    python script.py dhcp_reservation_list --output results/dhcp_reservation_with_manufacturer_list.csv

Author: Ryan Garaygay + Claude
Date: 2025-08-20
"""

import pandas as pd
import requests
import time
import sys
from pathlib import Path

def lookup_manufacturer(mac_address):
    """
    Look up the manufacturer for a given MAC address using the macvendors.com API.
    
    Args:
        mac_address (str): MAC address to look up
        
    Returns:
        str: Manufacturer name or error message
    """
    try:
        # Make API request with MAC address as-is
        url = f"https://api.macvendors.com/{mac_address}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            return response.text.strip()
        elif response.status_code == 404:
            return "Unknown"
        else:
            return f"Error: HTTP {response.status_code}"
            
    except requests.exceptions.RequestException as e:
        return f"Network Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def process_csv_with_manufacturers(input_file, mac_column, output_file=None, delay=1.0):
    """
    Process CSV file to add manufacturer information based on MAC addresses.
    
    Args:
        input_file (str): Path to input CSV file
        mac_column (str): Name of the MAC address column
        output_file (str): Path to output CSV file (optional)
        delay (float): Delay between API calls in seconds to avoid rate limiting
    """
    try:
        # Read the CSV file
        print(f"Reading CSV file: {input_file}")
        df = pd.read_csv(input_file)
        
        # Verify MAC column exists
        if mac_column not in df.columns:
            raise ValueError(f"Column '{mac_column}' not found in CSV file. Available columns: {list(df.columns)}")
        
        print(f"Using MAC address column: '{mac_column}'")
        print(f"Processing {len(df)} records...")
        
        # Add manufacturer column
        manufacturers = []
        
        for index, row in df.iterrows():
            mac_address = row[mac_column]
            print(f"Processing {index + 1}/{len(df)}: {mac_address}")
            
            manufacturer = lookup_manufacturer(mac_address)
            manufacturers.append(manufacturer)
            
            # Add delay to avoid overwhelming the API
            if index < len(df) - 1:  # Don't delay after the last request
                time.sleep(delay)
        
        # Add manufacturer column to dataframe
        df['Manufacturer'] = manufacturers
        
        # Determine output file name
        if output_file is None:
            input_path = Path(input_file)
            output_file = input_path.parent / f"{input_path.stem}_with_manufacturers{input_path.suffix}"
        
        # Save the updated CSV
        df.to_csv(output_file, index=False)
        print(f"\nCompleted! Results saved to: {output_file}")
        
        # Display summary
        unique_manufacturers = df['Manufacturer'].value_counts()
        print(f"\nManufacturer summary:")
        for manufacturer, count in unique_manufacturers.items():
            print(f"  {manufacturer}: {count}")
            
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    """Main function to handle command line arguments"""
    if len(sys.argv) < 3:
        print("Usage: python mac_vendor_lookup.py <input_csv_file> <mac_column_name> [output_csv_file] [delay_seconds]")
        print("\nExample:")
        print("  python mac_vendor_lookup.py devices.csv MAC_Address")
        print("  python mac_vendor_lookup.py devices.csv mac_address devices_with_vendors.csv")
        print("  python mac_vendor_lookup.py devices.csv mac_address devices_with_vendors.csv 0.5")
        return
    
    input_file = sys.argv[1]
    mac_column = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else None
    delay = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
    
    print("MAC Address Manufacturer Lookup Tool")
    print("=" * 40)
    print(f"Input file: {input_file}")
    print(f"MAC column: {mac_column}")
    print(f"Output file: {output_file if output_file else 'Auto-generated'}")
    print(f"API delay: {delay} seconds")
    print()
    
    process_csv_with_manufacturers(input_file, mac_column, output_file, delay)

if __name__ == "__main__":
    main()
