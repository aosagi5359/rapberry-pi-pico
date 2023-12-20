import machine
import time
import _thread as thread

# Define GPIO pins
red1, yellow1, green1 = 2, 3, 4
red2, yellow2, green2 = 6, 7, 8
button_direction_pin = 14

# Initialize GPIO pins
red1_led = machine.Pin(red1, machine.Pin.OUT)
yellow1_led = machine.Pin(yellow1, machine.Pin.OUT)
green1_led = machine.Pin(green1, machine.Pin.OUT)
red2_led = machine.Pin(red2, machine.Pin.OUT)
yellow2_led = machine.Pin(yellow2, machine.Pin.OUT)
green2_led = machine.Pin(green2, machine.Pin.OUT)
button_direction = machine.Pin(button_direction_pin, machine.Pin.IN, machine.Pin.PULL_UP)

# Variable to indicate the current direction
current_direction = 1  # 1: Red-Horizontal, Green-Vertical; 2: Green-Horizontal, Red-Vertical

def switch_direction():
    global current_direction

    while True:
        if current_direction == 1:
            red1_led.value(1)
            green2_led.value(1)
            time.sleep(0.5)
            red1_led.value(0)
            green2_led.value(0)
            time.sleep(0.5)

            green1_led.value(1)
            red2_led.value(1)
            time.sleep(0.5)
            green1_led.value(0)
            red2_led.value(0)
            time.sleep(0.5)
        elif current_direction == 2:
            green1_led.value(1)
            red2_led.value(1)
            time.sleep(0.5)
            green1_led.value(0)
            red2_led.value(0)
            time.sleep(0.5)

            red1_led.value(1)
            green2_led.value(1)
            time.sleep(0.5)
            red1_led.value(0)
            green2_led.value(0)
            time.sleep(0.5)

# Function to handle direction button press
def direction_button_pressed(pin):
    global current_direction

    if current_direction == 1:
        current_direction = 2
    elif current_direction == 2:
        current_direction = 1

# Set up direction button interrupt
button_direction.irq(trigger=machine.Pin.IRQ_FALLING, handler=direction_button_pressed)

# Start the direction switching thread
thread.start_new_thread(switch_direction, ())

# Main loop
while True:
    # Your main code logic here (based on the current direction)
    pass
