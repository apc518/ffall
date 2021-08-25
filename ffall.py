"""
ffall by Andy Chamberlain

apply an ffmpeg command to all files in the working directory with a given extension.
you must have ffmpeg installed and on your PATH already.

### Examples ###
A folder of 4k mp4 files that you want to downscale to 1080p:
`ffall -i .mp4 -vf scale=1920:1080 -preset slow .mp4`

A folder of wav files you want in mp3 format:
`ffall -i .wav .mp3`

"""

import os
import sys

if "ffall_output" not in os.listdir():
    os.mkdir("ffall_output")

input_ext = None
output_ext = None

in_idx = -1
out_idx = -1

for i, arg in enumerate(sys.argv):
    if i < 1: continue
    if arg.startswith("."):
        if input_ext is None:
            input_ext = arg
            in_idx = i
        else:
            output_ext = arg
            out_idx = i

def make_cmd(inp):
    new_args = []
    for i, arg in enumerate(sys.argv):
        if i == 0: # start the ffmpeg command
            new_args.append("ffmpeg")
        elif i not in (in_idx, out_idx): # fill in other arguments
            new_args.append(arg)
        elif i == in_idx: # input file
            new_args.append(f"\"{inp}\"")
        else: # output file
            if input_ext == output_ext:
                out = "ffall_output/" + inp.rsplit(".", 1)[0] + "_0" + output_ext
            else:
                out = "ffall_output/" + inp.rsplit(".", 1)[0] + output_ext
            new_args.append(f"\"{out}\"")
    
    return new_args

if not input_ext or not output_ext:
    print("You must enter file extension arguments, each starting with a period.\nExample: `\u001b[32mpython ffall.py -i .wav .mp3\u001b[0m`")
else:
    for item in os.listdir():
        if item.endswith(input_ext):
            cmd = " ".join(make_cmd(item))
            res = os.system(cmd)
            if res != 0:
                print(f"\u001b[31;1mAn error occurred trying to run an ffmpeg command: `{cmd}`\nSee ffmpeg error message above for details.\u001b[0m\nExiting...")
                break