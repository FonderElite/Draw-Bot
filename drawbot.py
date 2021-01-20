import os
import pyautogui
import tkinter.font
import time
import colorama
from colorama import Fore, Back, Style
import turtle
colorama.init(autoreset=True)
import platform
import math
os = platform
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
        pyautogui.dragRel(distancing * 12, 6.5, duration=0.5)  # right
        pyautogui.dragRel(4, distancing, duration=0.5)  # down
        pyautogui.dragRel(-distancing* 2, 9, duration=0.5)  # left
        pyautogui.dragRel(12, -distancing, duration=0.5)  # up
def sun():
    turtle.bgcolor("black")
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.done()

def skull():
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
    print(Fore.YELLOW +
          '''Thank you for using my tool :> 
          ~FonderElite
          ''')

help = Fore.YELLOW + '''
|-------------------------------------|
|[+]Commands:                         |
|[+]-h help                           |
|[+]-d drawable                       |
|[+]-D Draw                           |
|[+]-s screen size                    |
|[+]-S start                          |
|[+]-i install                        |
|[+]-u update                         |
|ex. python3 drawbot.py -S -D Square  |
|-------------------------------------|'''
paint = print(Fore.GREEN + "[Open a painting canvas to start drawing!]")
info = print(Fore.YELLOW + "python3 drawbot.py -h for help command")
screensize = str(pyautogui.size())
type = ["Square", "Triangle", "Circle","Sun"]
this = "[+]"
while True:
 command = input(Fore.CYAN + this + "Input a command: ")

 if command == "./drawbot -h":
    print(help)
 elif command == "./drawbot":
    print(help)
 elif command == "./drawbot -i":
    print("Preparing to install...")
    time.sleep(2)
    print(os.system("sudo bash install.sh"))
    print(Fore.GREEN + "DONE!")
 elif command == "./drawbot -u":
    print("Updating...")
    time.sleep(4)
    print(os.system("git clone https://github.com/FonderElite/Draw-Bot"))
    print(Fore.GREEN + "DONE!")
 elif command == "./drawbot -d":
    print(Fore.YELLOW + '''
          .:'
      __ :'__
   .'`__`-'__``. [+]Square
  :__________.-' [+]Circle
  :_________:    [+]Triangle
   :_________`-; [+]Sun
    `.__.-.__.'
    ''')
 elif command == "./drawbot -s":
    print("Scanning Screen-Size...")
    time.sleep(3)
    nice = Fore.MAGENTA + ">>Your Screen size is:"
    size = str(pyautogui.size())
    print(nice + size)
 elif command == "./drawbot -S -D Square":
    print("Starting...")
    time.sleep(2)
    function()
    skull()
 elif command == "./drawbot -S -D Triangle":
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
    skull()
 elif command == "./drawbot -S -D Circle":
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
    skull()

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
 elif command == './drawbot -S -D Sun':
     print("Scanning Screen-Size...")
     time.sleep(3)
     print(Fore.MAGENTA + "Your Screen size is:" + screensize)
     print(Fore.GREEN + "OK!")
     print("Check Turtle Graphics!")
     time.sleep(2)
     sun()
 else:
    print(Fore.RED + '''

@@@@@@@@ @@@@@@@  @@@@@@@   @@@@@@  @@@@@@@  @@@ 
@@!      @@!  @@@ @@!  @@@ @@!  @@@ @@!  @@@ @@@ 
@!!!:!   @!@!!@!  @!@!!@!  @!@  !@! @!@!!@!  !@! 
!!:      !!: :!!  !!: :!!  !!:  !!! !!: :!!      
: :: ::   :   : :  :   : :  : :. :   :   : : :.: 

    ''')
    try:
         os == "Linux"
    except:
         pyautogui.alert("Directory: C:\Program Files has been deleted")
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
