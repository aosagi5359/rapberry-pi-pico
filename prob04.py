import machine
import time
import _thread as thread

# Define GPIO pins
red1, yellow1, green1 = 2, 3, 4
red2, yellow2, green2 = 6, 7, 8
button_pin1 = 15
button_pin2 = 14

# Initialize GPIO pins
red1_led = machine.Pin(red1, machine.Pin.OUT)
yellow1_led = machine.Pin(yellow1, machine.Pin.OUT)
green1_led = machine.Pin(green1, machine.Pin.OUT)
red2_led = machine.Pin(red2, machine.Pin.OUT)
yellow2_led = machine.Pin(yellow2, machine.Pin.OUT)
green2_led = machine.Pin(green2, machine.Pin.OUT)
button1 = machine.Pin(button_pin1, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(button_pin2, machine.Pin.IN, machine.Pin.PULL_UP)

# Variable to indicate the current LED direction
current_direction = 'horizontal'

def set_horizontal_direction():
    global current_direction
    current_direction = 'horizontal'
    print("Direction: Horizontal")

def set_vertical_direction():
    global current_direction
    current_direction = 'vertical'
    print("Direction: Vertical")

# Function to handle button1 press
def button1_pressed(pin):
    set_horizontal_direction() if current_direction == 'vertical' else set_vertical_direction()

# Function to handle button2 press
def button2_pressed(pin):
    set_horizontal_direction() if current_direction == 'vertical' else set_vertical_direction()

# Set up button1 interrupt
button1.irq(trigger=machine.Pin.IRQ_FALLING, handler=button1_pressed)

# Set up button2 interrupt
button2.irq(trigger=machine.Pin.IRQ_FALLING, handler=button2_pressed)

# LED operations
def horizontal_direction():
    while current_direction == 'horizontal':
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

def vertical_direction():
    while current_direction == 'vertical':
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

# Main loop
while True:
    if current_direction == 'horizontal':
        horizontal_direction()
    elif current_direction == 'vertical':
        vertical_direction()
