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
```
