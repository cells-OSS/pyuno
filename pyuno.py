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
            if data == "PRESSED1":
                print("Switch 1 pressed!")
                keyboard.press(Key.media_play_pause)
                keyboard.press(Key.media_play_pause)
                time.sleep(0.1)
            if data == "PRESSED2":
                print("Switch 2 pressed!")
                keyboard.press(Key.media_previous)
                keyboard.press(Key.media_previous)
                time.sleep(0.1)
            if data == "PRESSED3":
                print("Switch 3 pressed!")
                keyboard.press(Key.media_next)
                keyboard.press(Key.media_next)
                time.sleep(0.1)
                
except Exception as e:
    print(f"Error: {e}")
finally:
    if ser.is_open:
        ser.close()
