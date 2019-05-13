#!/bin/bash
youtube-dl -o "~/Desktop/spotiProject/new_songs/$1.%(ext)s" --extract-audio --audio-format mp3 $2