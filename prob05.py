import machine
import time
import _thread as thread
import uasyncio as asyncio

# Define GPIO pins
red1, yellow1, green1 = 2, 3, 4
red2, yellow2, green2 = 6, 7, 8
button_pin = 13

# Set up GPIO pins for traffic light 1
traffic_light1_pins = [red1, yellow1, green1]
for pin in traffic_light1_pins:
    machine.Pin(pin, machine.Pin.OUT)

# Set up GPIO pins for traffic light 2
traffic_light2_pins = [red2, yellow2, green2]
for pin in traffic_light2_pins:
    machine.Pin(pin, machine.Pin.OUT)

# Set up GPIO pin for the push button
button = machine.Pin(button_pin, machine.Pin.IN, machine.Pin.PULL_UP)

# Define traffic light sequences
async def traffic_light_sequence1():
    while True:
        machine.Pin(red1, machine.Pin.OUT).value(1)
        await asyncio.sleep(5)
        machine.Pin(red1, machine.Pin.OUT).value(0)
        machine.Pin(yellow1, machine.Pin.OUT).value(1)
        await asyncio.sleep(0.5)
        machine.Pin(yellow1, machine.Pin.OUT).value(0)
        machine.Pin(green1, machine.Pin.OUT).value(1)
        await asyncio.sleep(5)
        machine.Pin(green1, machine.Pin.OUT).value(0)
        machine.Pin(yellow1, machine.Pin.OUT).value(1)
        await asyncio.sleep(0.5)
        machine.Pin(yellow1, machine.Pin.OUT).value(0)

async def traffic_light_sequence2():
    while True:
        machine.Pin(red2, machine.Pin.OUT).value(1)
        await asyncio.sleep(8)
        machine.Pin(red2, machine.Pin.OUT).value(0)
        machine.Pin(yellow2, machine.Pin.OUT).value(1)
        await asyncio.sleep(0.5)
        machine.Pin(yellow2, machine.Pin.OUT).value(0)
        machine.Pin(green2, machine.Pin.OUT).value(1)
        await asyncio.sleep(2)
        machine.Pin(green2, machine.Pin.OUT).value(0)
        machine.Pin(yellow2, machine.Pin.OUT).value(1)
        await asyncio.sleep(0.5)
        machine.Pin(yellow2, machine.Pin.OUT).value(0)

# Initial traffic light sequence
current_sequence = 1
loop = asyncio.get_event_loop()
loop.create_task(traffic_light_sequence1())
loop.create_task(traffic_light_sequence2())

# Function to handle button press
def button_pressed(p):
    global current_sequence
    current_sequence = 3 - current_sequence  # Switch between 1 and 2

# Set up interrupt for button press
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_pressed)

# Run the event loop
loop.run_forever()
