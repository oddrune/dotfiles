# .BASHrc
[[ $TERM == xterm-256color ]] && export TERM=xterm

export PATH=$PATH:${HOME}/bin:${HOME}/.local/bin
export GOPATH=$HOME/go
export LANG=en_US.utf8
HISTFILE=$HOME/.bash_history
HISTFILESIZE=20000
HISTSIZE=2000

#[[ -s "/usr/local/rvm/scripts/rvm" ]] && source "/usr/local/rvm/scripts/rvm" 

export PYTHONSTARTUP=${HOME}/.pythonrc.py

export EDITOR=vim
export VISUAL=vim

[[ -e "$HOME/ha/api.sh" ]] && source "$HOME/ha/api.sh"

j() {
  dname=$1
  if [ "$dname" == "today" ]; then
    dname=`date +%Y-%m-%d`
  fi
  mkdir $dname 2>/dev/null
  cd $dname
  }


alias cls='sleep 1; cd; timeout 1 find /proc; clear'
alias ls='ls -Flh --color'
alias c='clear'
alias cd='cd -P'
alias s='screen -U -rd oddrune'
alias x=s
alias headers='lynx -dump -head'
alias cd2='cd ../..'
alias cd3='cd ../../..'
alias cd4='cd ../../../..'
alias cd5='cd ../../../../..'
unalias rm 2>/dev/null

[[ -e "${HOME}/.bashrc.${HOSTNAME}" ]] && source "${HOME}/.bashrc.${HOSTNAME}"

PS2='   '

if [ "$TERM" == "linux" ]; then
	TERM="xterm"
	export TERM
fi

# Sjekk bash versjon, og hent in .bash_completion om det er nyere
# enn 2.04.
bash=${BASH_VERSION%.*}; bmajor=${bash%.*}; bminor=${bash#*.}
if [ "$PS1" ] && [ $bmajor -eq 2 ] && [ $bminor '>' 04 ] \
   && [ -f ~/.bash_completion ]; then # interactive shell
        # Source completion code
        . ~/.bash_completion
fi

case $TERM in
    screen )
        ;&
    xterm )
        export PS1="\[$(tput bold)\]: \[$(tput setaf 5)\]\h\[$(tput setaf 7)\]:\w; \[$(tput sgr0)\]"
        ;;
esac



