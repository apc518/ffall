# ffall

apply an ffmpeg command to all files in the working directory with a given extension.
you must have ffmpeg installed and on your PATH already.

### Examples ###
A folder of 4k mp4 files that you want to downscale to 1080p:
`python ffall.py -i .mp4 -vf scale=1920:1080 -preset slow .mp4`

A folder of wav files you want in mp3 format:
`python ffall.py -i .wav .mp3`
