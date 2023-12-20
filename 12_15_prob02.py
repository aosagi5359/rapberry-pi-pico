import machine
import time
import _thread as thread

# Define GPIO pins
red1, yellow1, green1 = 2, 3, 4
red2, yellow2, green2 = 6, 7, 8

# Initialize GPIO pins
red1_led = machine.Pin(red1, machine.Pin.OUT)
yellow1_led = machine.Pin(yellow1, machine.Pin.OUT)
red2_led = machine.Pin(red2, machine.Pin.OUT)
yellow2_led = machine.Pin(yellow2, machine.Pin.OUT)

# Variable to indicate whether the LED thread is running
led_thread_running = False

def flash_red_both_directions():
    while led_thread_running:
        red1_led.value(1)
        time.sleep(0.5)
        red1_led.value(0)
        time.sleep(0.5)

        red2_led.value(1)
        time.sleep(0.5)
        red2_led.value(0)
        time.sleep(0.5)

def flash_yellow_both_directions():
    while led_thread_running:
        yellow1_led.value(1)
        time.sleep(0.5)
        yellow1_led.value(0)
        time.sleep(0.5)

        yellow2_led.value(1)
        time.sleep(0.5)
        yellow2_led.value(0)
        time.sleep(0.5)

def flash_red_horizontal_yellow_vertical():
    while led_thread_running:
        red1_led.value(1)
        red2_led.value(1)
        time.sleep(0.5)
        red1_led.value(0)
        red2_led.value(0)
        time.sleep(0.5)

        yellow1_led.value(1)
        yellow2_led.value(1)
        time.sleep(0.5)
        yellow1_led.value(0)
        yellow2_led.value(0)
        time.sleep(0.5)

def swap_directions():
    while led_thread_running:
        red1_led.value(1)
        yellow2_led.value(1)
        time.sleep(0.5)
        red1_led.value(0)
        yellow2_led.value(0)
        time.sleep(0.5)

        yellow1_led.value(1)
        red2_led.value(1)
        time.sleep(0.5)
        yellow1_led.value(0)
        red2_led.value(0)
        time.sleep(0.5)

# Main loop
while True:
    command = input("Enter command (a, b, c, d): ")

    if led_thread_running:
        led_thread_running = False  # Stop the current LED thread before starting a new one
        time.sleep(1)  # Allow some time for the thread to terminate

    if command == 'a':
        thread.start_new_thread(flash_red_both_directions, ())
        led_thread_running = True
    elif command == 'b':
        thread.start_new_thread(flash_yellow_both_directions, ())
        led_thread_running = True
    elif command == 'c':
        thread.start_new_thread(flash_red_horizontal_yellow_vertical, ())
        led_thread_running = True
    elif command == 'd':
        thread.start_new_thread(swap_directions, ())
        led_thread_running = True
    else:
        print("Invalid command. Please enter a, b, c, or d.")
