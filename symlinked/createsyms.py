#!/bin/python3
import subprocess
import os
import sys

files = [
    '~/.config/symlinked/zsh/zshrc ~/.zshrc',
    '~/.config/symlinked/bash/bashrc ~/.bashrc',
    '~/.config/symlinked/xorg/xbindkeysrc ~/.xbindkeysrc',
    '~/.config/symlinked/xorg/Xresources ~/.Xresources',
    '~/.config/symlinked/xorg/xprofile ~/.xprofile',
    '~/.config/symlinked/profile ~/.profile'
]

def main():
    remove_flags = {'remove', 'r', '-r', 'uninstall'}
    

    command = ['ln', '-sf']
# TODO
#    if len(sys.argv) >= 2 and remove_flags.__contains__(sys.argv[1]):
#        command = ['rm']

    for file in files:
        expanded_home: list[str] = []
        for path in file.split(' '):
            expanded_home.append(os.path.expanduser(path))

        subprocess.run(command + expanded_home)



if __name__ == '__main__': 
    main()
