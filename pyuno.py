import serial
from pynput.keyboard import Controller, Key
import time

COM_PORT = 'COM3'  # Change this to your Arduino's port
BAUD_RATE = 9600

keyboard = Controller()

try:
    ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {COM_PORT}")
    time.sleep(2)  # Wait for Arduino to initialize
    
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            if data == "PRESSED":
                print("Switch pressed!")
                keyboard.press('a')
                keyboard.release('a')
                time.sleep(0.1)
                
except Exception as e:
    print(f"Error: {e}")
finally:
    if ser.is_open:
        ser.close()
