import RPi.GPIO as GPIO
import time

__author__ = 'Zsolti'


class Translator:

    _pins = [3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26,29,31,32,33,35]
    _input_pinst=[36,37,38,40]
    height = 0
    width = 0
    leds_on = []

    def __init__(self, height, width, matrix):
        self.width = width
        self.height = height
        self.matrix = matrix
        GPIO.setmode(GPIO.BOARD)
        for pin in self._pins:
            GPIO.setup(pin, GPIO.OUT)
        for pin in self._input_pinst:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #for pin in range(0, width + height):
            #GPIO.setup(int(self._pins[pin]), GPIO.OUT)

    def test(self):
        for x in range(0, self.height):
            for y in range(0, self.width):
                GPIO.output(self._pins[x], GPIO.HIGH)
                GPIO.output(self._pins[self.height + y], GPIO.HIGH)
                time.sleep(1)
                self.reset_all()


    def output_to_gpio(self):
        #GPIO.output(5, GPIO.HIGH)
        #time.sleep(0.00001)
        #self.reset_outputs()
        #Matrix = [[0 for y in range(9)] for x in range(11)]

        #if len(self.matrix) > 10:
            #for the_x in range (0, 11):
                #current_y = 0
                #for the_y in range(1, 9):
                 #   Matrix[the_x][the_y] = self.matrix[the_x][current_y]
                  #  current_y +=1
            #self.matrix = Matrix
            #print Matrix

        real_x = 0
        for x in range(0, self.height):
            for y in range(0, self.width):
               #if y <= 7:
                   if (self.matrix[x][y+1] == 1):
                        GPIO.output(self._pins[x], GPIO.HIGH)
                        self.leds_on.append(self._pins[x])
                        GPIO.output(self._pins[self.height  + y], GPIO.HIGH)
                        self.leds_on.append(self._pins[self.height + y])
                        time.sleep(0.0002)
                        self.reset_outputs()

    def reset_all(self):
        for pin in self._pins:
            GPIO.output(pin, GPIO.LOW)

    def reset_outputs(self):
        for pin in self.leds_on:
            GPIO.output(pin, GPIO.LOW)
        self.leds_on = []

    def set_matrix(self, new_matrix):
        self.matrix = new_matrix


