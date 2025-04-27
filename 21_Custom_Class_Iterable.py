import time
class Countdown:
    def __init__(self, start):
        self.start = start   # Set the starting number

    def __iter__(self):
        return self          # Return the iterator object (self)

    def __next__(self):
        if self.start < 0:
            raise StopIteration  # Stop iteration when finished
        current = self.start
        self.start -= 1      # Decrease the number by 1
        return current       # Return the current number

# Create a Countdown object starting from 5
countdown = Countdown(50)

# Use for loop to go through countdown
print("Countdown:")
for number in countdown:
    print("\r",number, end=' ', flush=True)
    time.sleep(1)