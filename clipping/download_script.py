import subprocess

print("Video URL: ", end='')
url = input()
print(f"Getting available qualities for video: {url}.\n")

subprocess.call(["ytdl", "-F", url], shell=True)

print("Select quality (single or audio+video): ", end='')
selection = input()
print(f"Passing DL quality {selection} to yt-dl\n")

subprocess.call(["ytdl", "-f", selection, url], shell=True)