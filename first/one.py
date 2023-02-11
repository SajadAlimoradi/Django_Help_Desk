from threading import Thread
from playsound import playsound


def play():
    while True:
        playsound("D:\\Django\\Project_01\\D_and_D_V3.2\\Sounds\\game.mp3")


t1 = Thread(target=play)
t1.start()

while True:
    user_input = input("enter data : ")
    print(user_input)


# t2 = Thread(target=game)
# t2.start()
