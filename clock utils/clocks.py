import os
import ctypes
import time
import threading

# CONFIG

# gpu downclocks
TARGET_CORE = 600
TARGET_MEM = 5_001
# windows power plan ids
HIGH_PERF = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
POWER_SAVE = "a1841308-3541-4fab-bc81-f71556f20b4a"
timer_active = True # repeat timer task on a 1 second interval (specific issue for PS2 which sets it to 1ms and is measurably worse for it)
TIMER_RES = 5_000

# END CONFIG 

ntdll = ctypes.WinDLL('ntdll.dll')
min = ctypes.c_ulong()
max = ctypes.c_ulong()
curr = ctypes.c_ulong()

def ms(field): return field.value / 10_000

def query_timer_res(): ntdll.NtQueryTimerResolution(ctypes.byref(min), ctypes.byref(max), ctypes.byref(curr))
def release_timer(): ntdll.NtSetTimerResolution(TIMER_RES, 0, ctypes.byref(curr))

def set_plan_name(name): 
    if timer_active: time.sleep(1) # Let timer task adjust
    ctypes.windll.kernel32.SetConsoleTitleW(f"Windows/NVIDIA Clock Tool: Plan = {name}")
    print(f"{name} plan activated.")

set_timer = False
def timer_task():
    while timer_active:
        if set_timer:
            # Check Windows timer interval
            query_timer_res()

            if curr.value != TIMER_RES:
                print(f"Current timer resolution: {ms(curr)}ms")
                # Set Windows timer interval
                ntdll.NtSetTimerResolution(TIMER_RES, 1, ctypes.byref(curr))
                print(f"Timer resolution set to {ms(curr)}ms")
        else: release_timer()
        
        time.sleep(1)
    release_timer()

MENU = "0. EXIT\n1. Repeat Menu\n\nSet Clocks:\n2. Downclock\n3. Restore High Clocks\n\nQuery:\n10. GPU Supported Clocks\n11. Power Plans\n12. Current Timer Resolution"

# Main executable 
if __name__ == "__main__":
    print("=== Windows/NVIDIA Clocks Tool by kabii ===")
    print(MENU)
    print("\n\n== Starting ==")

    # start timer task
    timer_thread = threading.Thread(target=timer_task)
    timer_thread.start()

    select = 2
    while(True):
        if select == 0:
            break
        if select == 1:
            print(MENU)
        if select == 2:
            # force gpu downclock - this only makes sense on systems with multiple monitors(!) or other conditions that maintain the gpu at 3d clocks
            # otherwise, the gpu should drop even lower to 2d clocks on its own
            os.system(f"nvidia-smi -i 0 -lgc {TARGET_CORE}")
            os.system(f"nvidia-smi -i 0 -lmc {TARGET_MEM}")
            os.system(f"powercfg /SETACTIVE {POWER_SAVE}")
            set_timer = False
            set_plan_name("Power Saver")
        elif select == 3:
            # reset clocks
            os.system("nvidia-smi -i 0 -rgc")
            os.system("nvidia-smi -i 0 -rmc")
            print("GPU clocks reset.")
            os.system(f"powercfg /SETACTIVE {HIGH_PERF}")
            set_timer = True
            set_plan_name("High Performance")
        elif select == 10:
            # list supported gpu clocks
            os.system("nvidia-smi -q -d SUPPORTED_CLOCKS")
        elif select == 11:
            # list power plans
            os.system("powercfg /L")
        elif select == 12:
            # query current timer resolution
            query_timer_res()
            print("== Timer Resolution ==")
            print(f"Current: {ms(curr)}ms - Min: {ms(min)}ms - Max: {ms(max)}ms")
        user_in = input("\nSelect op (1 for options): ")
        try:
            select = int(user_in)
        except ValueError as _:
            print("Invalid input. Options:")
            select = 1

    timer_active = False
    timer_thread.join()

    os.system("pause")