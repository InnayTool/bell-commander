import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
pygame.init()
sound = pygame.mixer.music
sound.load("sound.mp3")



def my_callback(e):
    if sound.get_pos() == -1:
        sound.play()

GPIO.add_event_detect(24, GPIO.RISING)
GPIO.add_event_callback(24, my_callback)

"""
class bell:
    def __init__(self):
        self.active = False
        self.timer = time.clock()
        self.interval = 3
        self.ring_time = 0.1

    def activate(self):
        self.active=True
    def deactivate(self):
        self.active=False

    #def update(self):
    #    if not self.active:
    #        return

        if self.timer+self.interval <time.clock():
"""                    
    



print("Armed.")
while True:
    time.sleep(0.001)
