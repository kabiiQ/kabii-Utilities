# kabii-Utilities

### Support the Developer

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/E1E5AF13X)

Relatively simple Python scripts I use to simplify some tasks on my PC. These may or may not be helpful to anyone else. 

# 'clipping' script
- Requires ytdl in PATH

Runs yt-dl, pulls available qualities and then downloads the selection. 

# 'reencode' script
- Requires ffmpeg in PATH

Runs ffmpeg to do a basic re-encoding of a video to reduce file size greatly. 

I use this regularly for ShadowPlay clips to reduce them to an uploadable filesize to Discord.

# 'clock utils' 
- Must be run with admin perms, from elevated command prompt, a shortcut specified as administrator-mode

Allows manually toggling between high performance and power saving states for high-spec PCs. This script should not be needed if your system properly downclocks at idle, however under Windows 10, mine will not do so. 

As-is, this script only functions on Windows for NVIDIA GPUs.

In high performance mode, my system tends to jump around between **300-400w** randomly while just browsing. With this tool active it seems to sits **stable** around **225w**. Of course, when you are trying to run games or productivity applications, I want the highest performance possible. 

This helps me to automate setting the following clock states with 1 command.
## NVIDIA Clocks
- Toggles lower NVIDIA clocks as my GPU stays at near-max clock 3D clock speeds at all times. This is a common issue with NVIDIA GPUs, it seems simply having multiple monitors attached(!) can force 3D clocks, but I also run NVIDIA Broadcast/Wallpaper Engine which seem to really force the clocks to max even if not needed. 
- This util can NOT reach the level of natural downclocking/2D clocks, but it saves nearly **50W** (116 -> 70 idle) on its own while active for me.

## Windows Power Plan
- Toggles between power saver and high performance plans in Windows. The primary savings in power saver plan come from the CPU clocking down when idle. 

## Windows System Timer 
- The script also builds in the ability to check/set the Windows system timer. This is a fairly niche functionality, and should not be needed in most cases as modern games seem to set the timer properly already. 
- For me, 1 game in particular, PlanetSide 2, seems to specifically set the timer interval to 1ms (and not just at launch!). Input are noticibly more crisp at .5ms, so this feature checks and sets the timer back to .5ms every second if it's been changed. I would not be surprised if there are other older games that this helps if you're very sensitive to input lag!