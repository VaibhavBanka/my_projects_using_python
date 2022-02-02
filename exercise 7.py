from pygame import mixer
from time import time
from datetime import datetime
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.7)
    mixer.music.play(loops=-1)
    print("Type",stopper,'when you are done drinking water.')
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open('C:/users/dell/desktop/mylogs.txt','a') as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    watersecs=900
    exercisesecs=1800
    eyessecs=2700

    while True:
        if time()-init_water>watersecs:
            print("WaterDrinkng Time. Enter 'Drank' to stop the alarm.")
            musiconloop("C:/users/dell/downloads/water.mp3", 'drank')
            init_water=time()
            log_now("Drank water at ")
        if time()-init_eyes> eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop("C:/Users/Dell/Downloads/remind_message.mp3",'doneeyes')
            init_eyes=time()
            log_now("Eyes Relaxed at ")
        if time()-init_exercise> exercisesecs:
            print("Physical exercise time. Enter 'donephy' to stop the alarm.")
            musiconloop("C:/Users/Dell/Downloads/remind_message.mp3",'donephy')
            init_exercise=time()
            log_now("Physical Activity Done at ")

