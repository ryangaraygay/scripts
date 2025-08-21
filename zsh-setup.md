# you need brew
```
brew install zsh-syntax-highlighting zsh-autosuggestions
```

# add these to your ~/.zshrc
```
source $(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh

alias ll='ls -lG'
alias f='open -a Finder ./'
alias which='type -all'

sha256check() { local G='\033[0;32m' R='\033[0;31m' N='\033[0m'; [[ -f "$1" ]] && [[ "$(shasum -a 256 "$1" | cut -d' ' -f1)" == "$2" ]] && echo -e "${G}✓ MATCH${N}" || echo -e "${R}✗ FAIL${N}"; }
```
