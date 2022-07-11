#!/bin/sh

case "$1" in 
    *.tar*) tar tf "$1";;
    *.zip) unzip -l "$1";;
    *.rar) unrar l "$1";;
    *.7z) 7z l "$1";;
    *.pdf) pdftotext "$1" -;;

    *.jpg) fbv "$1";;
    # Default
    *) highlight -O ansi "$1";;
esac