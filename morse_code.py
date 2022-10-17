#Importing different Libraries
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
import time

# Declaring a variable to switch an LED on and off
led = LED(15)

# Time unit for morse code
unit = 0.2

# Creating a window and setting the font
win = Tk()
win.title("Morse Code Generator")
win.geometry("455x223")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

# Closing button for the window
def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Declaring the dot in morse code
def dot():
    led.on()   
    time.sleep(unit * 1)
    led.off()    
    time.sleep(unit * 1)

# Declaring the dash in morse code 
def dash():
    led.on()
    time.sleep(unit * 3)
    led.off()
    time.sleep(unit * 1)

# Morse code function
def morse_code():
    # Getting the text from the text-box
    text = text_box.get(1.0, "end-1c")
    for i in text:
      if i == 'a':
        dot()
        dash()
      elif i == 'b':
        dash()
        dot()
        dot()
        dot()
      elif i == 'c':
        dash()
        dot()
        dash()
        dot()
         
      elif i == 'd':
        dash()
        dot()
        dot()
         
      elif i == 'e':
        dot()
         
      elif i == 'f':
        dash()
        dot()
        dot()
        dash()
        dot()
         
      elif i == 'g':
        dash()
        dash()
        dot()
         
      elif i == 'h':
        dot()
        dot()
        dot()
        dot()
         
      elif i == 'i':
        dot()
        dot()
         
      elif i == 'j':
        dot()
        dash()
        dash()
        dash()
         
      elif i == 'k':
        dash()
        dot()
        dash()
         
      elif i == 'l':
        dot()
        dash()
        dot()
        dot()
         
      elif i == 'm':
        dash()
        dash()
         
      elif i == 'n':
        dash()
        dot()
         
      elif i == 'o':
        dash()
        dash()
        dash()
         
      elif i == 'p':
        dot()
        dash()
        dash()
        dot()
         
      elif i == 'q':
        dash()
        dash()
        dot()
        dash()
         
      elif i == 'r':
        dot()
        dash()
        dot()
         
      elif i == 's':
        dot()
        dot()
        dot()
         
      elif i == 't':
        dash()
         
      elif i == 'u':
        dot()
        dot()
        dash()
         
      elif i == 'v':
        dot()
        dot()
        dot()
        dash()
         
      elif i == 'w':
        dot()
        dash()
        dash()
         
      elif i == 'x':
        dash()
        dot()
        dot()
        dash()
         
      elif i == 'y':
        dash()
        dot()
        dash()
        dash()
         
      elif i == 'z':
        dash()
        dash()
        dot()
        dot()
         
    time.sleep(unit * 3)

# Limiting the text in text box
def text_size(value):
    text_ = text_box.get('1.0','end-1c')
    breaks = text_.count('\n')
    t_size = len(text_) - breaks
    if t_size > 12:
        text_box.delete('end-2c')
    
# Designing the GUI
Label(win, text="Enter the Text in the Textbox").pack()
text_box = Text(win, height = 5, width = 20)
text_box.pack()

# Everytime key is pressed, text_size function is called
text_box.bind('<KeyRelease>', text_size)

Button(win, text="Generate Morse Code",command = morse_code, font = myFont, bg = 'green').pack()
Button(win, text="Exit", font= myFont, command = close, bg='red').pack()


