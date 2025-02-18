import time

def type_effect(text, speed=0.05):  # Default speed is 0.05 if not provided
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()  # Ensure the output moves to the next line
