import board
import digitalio
import pwmio
import time

from adafruit_motor import servo

touch = digitalio.DigitalInOut(board.D1)
touch.switch_to_input(pull=digitalio.Pull.UP)

# create a PWMOut object on Pin A5.
pwm = pwmio.PWMOut(board.A5, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

led = digitalio.DigitalInOut(board.YELLOW_LED_INVERTED)
led.direction = digitalio.Direction.OUTPUT

print("READY...")
while True:
    led.value = False if touch.value else True
    my_servo.angle = 30 if touch.value else 0
    time.sleep(0.1)
