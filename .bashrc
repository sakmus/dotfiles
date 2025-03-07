#
# ~/.bashrc
#

eval "$(starship init bash)"

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

export PATH=$PATH:$HOME/.local/bin
alias battery="upower -i /org/freedesktop/UPower/devices/battery_BAT0"
alias cpumax="sudo cpupower frequency-set -g performance"
alias cpulow="sudo cpupower frequency-set -g powersave"
alias cpu-info="cpupower frequency-info"
alias cleanup="sudo pacman -Rns $(pacman -Qtqd)"

alias vim="nvim"
alias vi="nvim"

# Enable bash-completion
if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
fi

