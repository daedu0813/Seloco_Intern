import Jetson.GPIO as GPIO
import time

if __name__ == "__main__":
    trig = 7    # T
    echo = 11   # R
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    # set GPIO direction
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    while True:
        GPIO.output(trig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trig, GPIO.LOW)

        statTime = time.time()
        stoptTime = time.time()

        while GPIO.input(echo) == 0:
            startTime = time.time()

        while GPIO.input(echo) == 1:
            stopTime = time.time()

        timeElapsed = stopTime - startTime
        
        distance = (timeElapsed * 34300) / 2
        distance = round(distance, 2)

        if(distance > 0 and distance < 500):
            print("Distance: " + str(distance) + "cm")

        time.sleep(0.5)
