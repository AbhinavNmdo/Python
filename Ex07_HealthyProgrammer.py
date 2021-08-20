from pygame import mixer
import datetime
from datetime import datetime
from time import time

water = 'water.mp3'
eyes = 'eyes.mp3'
exercise = 'exercise.mp3'


def playMusic(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        inputFromUser = input()
        if inputFromUser == stopper:
            mixer.music.stop()
            break



def logcat(msg):
    with open("HealthyPragrammer.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


# Intervals
intervalWater = time()
intervalEyes = time()
intervalExercise = time()
int_water = 10
int_eyes = 20
int_exercise = 30

# For Drink Water
while True:
    if time() - intervalWater > int_water:
        print("Your water drinking time, if you drink water then type 'drank' ")
        playMusic("water.mp3", "drank")
        intervalWater = time()
        logcat("Drink water at: ")

    if time() - intervalEyes > int_eyes:
        print("Your Eyes Exercise time, if you already do this then type 'edone' ")
        playMusic("eyes.mp3", "edone")
        intervalEyes = time()
        logcat("Eyes exercise done at: ")

    if time() - intervalExercise > int_exercise:
        print("Its your Physical Exercise time, if you done it then type 'done' ")
        playMusic("exercise.mp3", "done")
        intervalExercise = time()
        logcat("Physical Exercise done at: ")