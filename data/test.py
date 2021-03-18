import Jetson.GPIO as GPIO
import time

if __name__ == "__main__":
    GPIO.setwarnings(False)
    pin = 18
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)

    while True:
        if GPIO.input(pin) == GPIO.HIGH:
            print('Detect! ^.^')
        elif GPIO.input(pin) == GPIO.LOW:
            print('Do not Detect T.T')
        else:
            print('Exception')
        time.sleep(1)

