import serial
from pynput.keyboard import Controller, Key
from pycaw.pycaw import AudioUtilities
import time

COM_PORT = "COM3"
BAUD_RATE = 9600

keyboard = Controller()

device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
print(device)
try:
    ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {COM_PORT}")
    time.sleep(2)

    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode(errors="ignore").strip()

            if data == "PRESSED1":
                print("Play/Pause")
                keyboard.press(Key.media_play_pause)
                keyboard.release(Key.media_play_pause)

            elif data == "PRESSED2":
                print("Previous Track")
                keyboard.press(Key.media_previous)
                keyboard.release(Key.media_previous)

            elif data == "PRESSED3":
                print("Next Track")
                keyboard.press(Key.media_next)
                keyboard.release(Key.media_next)

            elif data.startswith("VOL:"):
                try:
                    value = int(data.split(":")[1])
                    value = max(0, min(100, value))

                    device = AudioUtilities.GetSpeakers()
                    volume = device.EndpointVolume

                    volume.SetMasterVolumeLevelScalar(value / 100.0, None)

                    print(f"Volume: {value}")
                except ValueError:
                    pass

except Exception as e:
    print(f"Error: {e}")

finally:
    try:
        if ser.is_open:
            ser.close()
    except:
        pass