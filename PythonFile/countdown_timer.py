import time


def start_countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Time left: {time_format}", end='\r')
        time.sleep(1)
        seconds -= 1

if __name__ == "__main__":
    # Input for countdown timer
    countdown_seconds = int(input("Enter the countdown time in seconds: "))
    # Start the countdown
    start_countdown(countdown_seconds)
