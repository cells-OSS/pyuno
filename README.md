# pyuno
Simple python script to interface with the innoswitch sketch.

This program can be used with [Innoswitch](https://github.com/cells-oss/innoswitch)

NOTE: Currently the volume knob function detects the output device you have selected and uses that, if you change it it will stop working until you restart the script with the new output device selected. Depending on the annoyance i will make it work when the output has changed but i think right now it's okay, i also plan on adding a CLI interface in the future that will let you change the output device you want to control as well.

# SCHEMATIC
<img width="1322" height="729" alt="sch" src="https://github.com/user-attachments/assets/31e7ee98-908b-4816-a007-cc328322875a" />

black - jumper wire

green - resistor

red - keyboard switch