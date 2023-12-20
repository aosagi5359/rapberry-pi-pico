import machine
import time
import _thread as thread

# Define GPIO pins
red1, yellow1, green1 = 2, 3, 4
red2, yellow2, green2 = 6, 7, 8
button_pin = 15

# Initialize GPIO pins
red1_led = machine.Pin(red1, machine.Pin.OUT)
yellow1_led = machine.Pin(yellow1, machine.Pin.OUT)
red2_led = machine.Pin(red2, machine.Pin.OUT)
yellow2_led = machine.Pin(yellow2, machine.Pin.OUT)
button = machine.Pin(button_pin, machine.Pin.IN, machine.Pin.PULL_UP)

# Variable to indicate the current LED operation
current_operation = 'a'

def flash_red_both_directions():
    while current_operation == 'a':
        red1_led.value(1)
        time.sleep(0.5)
        red1_led.value(0)
        time.sleep(0.5)

        red2_led.value(1)
        time.sleep(0.5)
        red2_led.value(0)
        time.sleep(0.5)

def flash_yellow_both_directions():
    while current_operation == 'b':
        yellow1_led.value(1)
        time.sleep(0.5)
        yellow1_led.value(0)
        time.sleep(0.5)

        yellow2_led.value(1)
        time.sleep(0.5)
        yellow2_led.value(0)
        time.sleep(0.5)

def flash_red_horizontal_yellow_vertical():
    while current_operation == 'c':
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
    while current_operation == 'd':
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

# Function to handle button press
def button_pressed(pin):
    global current_operation

    if current_operation == 'a':
        current_operation = 'b'
    elif current_operation == 'b':
        current_operation = 'c'
    elif current_operation == 'c':
        current_operation = 'd'
    elif current_operation == 'd':
        current_operation = 'a'

# Set up button interrupt
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_pressed)

# Main loop
while True:
    if current_operation == 'a':
        flash_red_both_directions()
    elif current_operation == 'b':
        flash_yellow_both_directions()
    elif current_operation == 'c':
        flash_red_horizontal_yellow_vertical()
    elif current_operation == 'd':
        swap_directions()
