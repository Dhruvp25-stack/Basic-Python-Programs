# Countdown Timer Program
# User sets time in seconds, script counts down and alerts when finished

import time
import winsound  # Works on Windows. For Linux/Mac, a print beep is also added.

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print("Time Left:", timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("\n⏱️ Time's up!")
    
    # For Windows beep
    try:
        frequency = 1000
        duration = 800
        winsound.Beep(frequency, duration)
    except:
        print("\a")   # fallback beep for Mac/Linux

if __name__ == "__main__":
    print("----- Countdown Timer -----")
    try:
        total_seconds = int(input("Enter time in seconds: "))
        countdown(total_seconds)
    except ValueError:
        print("❌ Invalid input! Please enter an integer value.")
