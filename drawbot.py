import os
import pyautogui
import tkinter.font
import time
import colorama
from colorama import Fore, Back, Style
import turtle
colorama.init(autoreset=True)
import math

print(Fore.CYAN + '''
 ██████████                                       ███████████            █████   
░░███░░░░███                                     ░░███░░░░░███          ░░███    
 ░███   ░░███ ████████   ██████   █████ ███ █████ ░███    ░███  ██████  ███████  
 ░███    ░███░░███░░███ ░░░░░███ ░░███ ░███░░███  ░██████████  ███░░███░░░███░   
 ░███    ░███ ░███ ░░░   ███████  ░███ ░███ ░███  ░███░░░░░███░███ ░███  ░███    
 ░███    ███  ░███      ███░░███  ░░███████████   ░███    ░███░███ ░███  ░███ ███
 ██████████   █████    ░░████████  ░░████░████    ███████████ ░░██████   ░░█████ 
░░░░░░░░░░   ░░░░░      ░░░░░░░░    ░░░░ ░░░░    ░░░░░░░░░░░   ░░░░░░     ░░░░░  
''')
print('''
Made By: FonderElite || Droid
Visit My Github Page: https://github.com/FonderElite
''')
time.sleep(2)
easy = ["triangle", "Triangle", "Circle", "circle", "square"]


#
def function():
    print("Scanning Screen-Size...")
    time.sleep(3)
    print(Fore.MAGENTA + "Your Screen size is:" + screensize)
    time.sleep(2)
    print(Fore.GREEN + "OK!")
    print("Open A Painting Canvas To Begin Drawing!")
    time.sleep(5)

    pyautogui.click()
    distance = 200

    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2)  # move right
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=0.2)  # move down

        pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
        distance = distance - 5

        pyautogui.dragRel(0, -distance, duration=0.2)  # move up


# Circle Function
def circle():
    et = turtle.bgcolor('black')
    turtle.setup(800, 600)

    board = turtle.Turtle()
    board.color("white")
    for i in range(20):
        board.circle(40)
        board.right(36)


    turtle.done()
    # Triangle Function
def triangle():
    pyautogui.click();
    distancing = 250
    while distancing > 0:
        pyautogui.dragRel(distancing * 12, 0, duration=0.5)  # right
        pyautogui.dragRel(4, distancing, duration=0.5)  # down
        pyautogui.dragRel(-distancing* 2, 9, duration=0.5)  # left
        pyautogui.dragRel(12, -distancing, duration=0.5)  # up


help = Fore.YELLOW + '''
 |------------------------------------|
|[+]Commands:                         |
|[+]-h help                           |
|[+]-d drawable                       |
|[+]-D Draw                           |
|[+]-s screen size                    |
|[+}-S start                          |
|ex. python3 drawbot.py -S -D         |
|-------------------------------------|'''
paint = print(Fore.GREEN + "[Open a painting canvas for Square to work!]")
info = print(Fore.YELLOW + "python3 drawbot.py -h for help command")
screensize = str(pyautogui.size())
type = ["Square", "Triangle", "Circle"]
this = "[+]"
command = input(Fore.CYAN + this + "Input a command: ")
if command == "python3 drawbot.py -h":
    print(help)
    print("Try again.")
elif command == "python3 drawbot.py":
    print(help)
    print("Try again.")
elif command == "python3 drawbot.py -d":
    print(Fore.YELLOW + '''
          .:'
      __ :'__
   .'`__`-'__``. [+]Square
  :__________.-' [+]Circle
  :_________:    [+]Triangle
   :_________`-;
    `.__.-.__.'
    ''')
elif command == "python3 drawbot.py -s":
    print("Scanning Screen-Size...")
    time.sleep(3)
    nice = Fore.MAGENTA + ">>Your Screen size is:"
    size = str(pyautogui.size())
    print(nice + size)
elif command == "python3 drawbot.py -S -D Square":
    print("Starting...")
    time.sleep(2)
    function()
elif command == "python3 drawbot.py -S -D Triangle":
    print("Starting...")
    time.sleep(2)
    print("Scanning Screen-Size...")
    time.sleep(3)
    print(Fore.MAGENTA + "Your Screen size is:" + screensize)
    time.sleep(2)
    print(Fore.GREEN + "OK!")
    print("Open A Painting Canvas To Begin Drawing!")
    time.sleep(5)
    triangle()
elif command == "python3 drawbot.py -S -D Circle":
    print("Starting...")
    time.sleep(2)
    print("Scanning Screen-Size...")
    time.sleep(3)
    print(Fore.MAGENTA + "Your Screen size is:" + screensize)
    time.sleep(2)
    print(Fore.GREEN + "OK!")
    print("Wait for it..")
    time.sleep(2)
    print("Wait for it...")
    time.sleep(2)
    print(Fore.GREEN + "OK!")
    circle()

    circle()

elif command == type[0]:
    print("Scanning Screen-Size...")
    time.sleep(3)
    print(Fore.MAGENTA + "Your Screen size is:" + screensize)
    print(Fore.GREEN + "OK!")
    print("Open A Painting Canvas To Begin Drawing!")
    time.sleep(5)

    pyautogui.click()
    distance = 200

    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2)  # move right
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=0.2)  # move down

        pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
        distance = distance - 5

        pyautogui.dragRel(0, -distance, duration=0.2)  # move up

else:
    print(Fore.RED + '''

@@@@@@@@ @@@@@@@  @@@@@@@   @@@@@@  @@@@@@@  @@@ 
@@!      @@!  @@@ @@!  @@@ @@!  @@@ @@!  @@@ @@@ 
@!!!:!   @!@!!@!  @!@!!@!  @!@  !@! @!@!!@!  !@! 
!!:      !!: :!!  !!: :!!  !!:  !!! !!: :!!      
: :: ::   :   : :  :   : :  : :. :   :   : : :.: 

    ''')
print(Fore.RED + '''
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--` 
''')
print(Fore.YELLOW + '''

Thank you for using my tool :>
~Fonder-Elite
''')
#
# Radius
# R = 400
# measuring screen size
# (x,y) = pyautogui.size()
# locating center of the screen
# (X,Y) = pyautogui.position(x/2,y/2)
# offsetting by radius
# pyautogui.moveTo(X+R,Y)

# for i in range(360):
# setting pace with a modulus
# if i%6==0:
# pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
