from machine import Pin
import utime
import _thread

# 初始化 GPIO 腳位
red1 = Pin(2, Pin.OUT)   # 第一個燈的紅色通道
yellow1 = Pin(3, Pin.OUT) # 第一個燈的黃色通道
green1 = Pin(4, Pin.OUT)

red2 = Pin(6, Pin.OUT)   # 第二個燈的紅色通道
yellow2 = Pin(7, Pin.OUT) # 第二個燈的黃色通道
green2 = Pin(8, Pin.OUT)



# 當前指令
current_command = None

# 閃爍燈的函數
def blink_lights():
    global current_command
    while True:    
        
        if current_command == 'a':
            cAL()
            red1.value(1)
            green2.value(1)
        elif current_command == 'b':
            cAL()
            red2.value(1)
            green1.value(1)
        elif current_command == 'c':
            cAL()
            red1.value(1)
            red2.value(1)
            utime.sleep(1)
            red1.value(0)
            red2.value(0)
        elif current_command == 'd':
            cAL()
            yellow1.value(1)
            yellow2.value(1)
            utime.sleep(1)
            yellow1.value(0)
            yellow2.value(0)
        elif current_command == 'e':
            cAL()
            traffic(1)
            utime.sleep(3)
            cAL()
            traffic(2)
            utime.sleep(3)
            cAL()
            traffic(3)
            utime.sleep(3)
            cAL()
            traffic(4)
            utime.sleep(3)
        elif current_command == 'f':
            cAL()
            traffic(1)
            utime.sleep(1)
            cAL()
            traffic(2)
            utime.sleep(1)
            cAL()
            traffic(3)
            utime.sleep(6)
            cAL()
            traffic(4)
            utime.sleep(1)
        else:
            # 如果沒有指令，則關閉所有燈
            cAL()
        utime.sleep(0.1) # 小延時以防止佔用太多 CPU 資源
def traffic(mode):
    if mode == 1:
        red1.value(1)
        green2.value(1)
    elif mode == 2:
        red1.value(1)
        yellow1.value(1)
        yellow2.value(1)
    elif mode == 3:
        red2.value(1)
        green1.value(1)
    elif mode == 4:
        red2.value(1)
        yellow2.value(1)
        yellow1.value(1)
def cAL():
    red1.value(0)
    red2.value(0)
    yellow1.value(0)
    yellow2.value(0)
    green1.value(0)
    green2.value(0)
# 讀取命令的函數
def read_commands():
    global current_command
    while True:
        current_command = input("Enter command (a, b, c, d, e, f): ")

# 創建並啟動閃爍燈的線程
_thread.start_new_thread(blink_lights, ())

# 主循環，用於讀取命令
read_commands()

