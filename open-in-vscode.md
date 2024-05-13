To add a menu item when right-clicking on a file in macOS that allows opening the folder containing that file in Visual Studio Code, you can create an Automator service (known as a Quick Action in recent macOS versions). This service will be accessible from the context menu. Here's how you can do it:

Open Automator:

Launch Automator from your Applications folder.
Create a New Document:

Choose “New Document” at the bottom of the screen.
Select “Quick Action” and click “Choose”.
Configure the Workflow:

At the top of the right panel, set “Workflow receives current” to files or folders in Finder.
You can optionally set the image and color that will appear in the Services menu.
Add a Run Shell Script Action:

Drag “Run Shell Script” from the list of actions on the left (you can find it under “Utilities”) into the workflow area on the right.

Set “Pass input” to as arguments.

In the script area, replace the existing content with the following script:

```bash
for f in "$@"
do
   if [ -d "$f" ]; then
       open -a "Visual Studio Code" "$f"
   else
       open -a "Visual Studio Code" "$(dirname "$f")"
   fi
done
```
This script takes the selected file(s), determines the directory containing the file, and opens that directory in Visual Studio Code.

Save Your Service:

Go to File > Save and give your new service a name, like “Open Folder in VS Code”.
Use Your Service:

Right-click on any file in Finder.
Go to “Quick Actions” or “Services” from the context menu (the name depends on your macOS version).
Select “Open Folder in VS Code”.
If you don't see the service, you might need to go to System Preferences > Keyboard > Shortcuts > Services and make sure your newly created service is checked under “Files and Folders”.

This should set up a context menu item to open folders in Visual Studio Code from Finder with a right-click.