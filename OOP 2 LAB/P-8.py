import time

def countdown_timer():
        countdown_time = int(input("Enter the time in seconds for the countdown: "))

        if countdown_time <= 0:
            print("Please enter a positive number.")
            return

        print(f"Countdown starts from {countdown_time} seconds:")

        while countdown_time > 0:
            print(countdown_time)
            time.sleep(1)
            countdown_time -= 1

        print("Time's up!")

countdown_timer()
