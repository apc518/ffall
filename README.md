# ffall

apply an ffmpeg command to all files in the working directory with a given extension.
you must have ffmpeg installed and on your PATH already.

### Examples ###
A folder of 4k mp4 files that you want to downscale to 1080p:
`ffall -i .mp4 -vf scale=1920:1080 -preset slow .mp4`

A folder of wav files you want in mp3 format:
`ffall -i .wav .mp3`
