# simple-automation
Simple example about how use Seeeduino XIAO for steering elements of automation.

![Sample automation system](/sample_automation_system%20_20250125.jpg)

## Hardware used
- Grove Shield for Seeeduino XIAO
- Seeeduino XIAO  with microcontroller SAMD21G18 ARM Cortex-M0+ onboard
- 250mAh Li-Po Battery
- Grove - TTP223-B touch button
- Grove - Analog servo

## Software used
MuEditor --  a simple Python editor for programmers, that work with CircuitPython.

## Code explanation
When you set switch on Grove Shiled on ON position. You will see green light on XIAO board and red light on touch button board.
Is inform you that microcontroller is ready to use and wait for your action.

Touching the sensor causes the second LED to light up orange and the servo to move to the new position.
When not touching the servo back to basic position and and the second LED light down.
