import subprocess

print("Input filename (no extension, assumes .mp4): ", end='')
filename = input()
inname = filename + ".mp4"
outname = filename + ".e.mp4"
print("Output filename: ", end='')

print("Resolution: 0=1440p 1=1080p 2=720p: ", end='')
resolution = { 0: "2560x1440", 1: "1920x1080", 2: "1280x720" }[int(input())]

print("crf (24-30): ", end='')
crf = input()

# ffmpeg -i input.mp4 -vcodec libx264 -preset veryslow -crf 30 output.mp4
subprocess.call(["ffmpeg", "-i", inname, "-vcodec", "libx264", "-preset", "veryslow", "-crf", crf, "-s", resolution, outname], shell=True)