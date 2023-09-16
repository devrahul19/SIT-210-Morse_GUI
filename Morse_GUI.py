#SIT 210
# Name - RAHUL DHIMAN
#TASK 5.3D
import tkinter as tk
import RPi.GPIO as GPIO
import time
# configuring GPIO 
GPIO.setmode(GPIO.BCM)
LED_PIN = 14  # using GPIO14 for the LED 

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  # Initially turn off the LED

# Morse Code Dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}
 # this function helps converting text to Morse Code 
def text_to_morse(input_text):
    morse = ''
    for char in input_text.upper():
        if char in morse_code:
            morse += morse_code[char] + ' '
        else:
            morse += char + ' '
    return morse
# blinking dot 
def blink_dot():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.2)  # duration of a dot
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.2)  # duration between dots and dashes
# blinking dash 
def blink_dash():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.6)  # Adjust the duration of a dash
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.2)  # Adjust the duration between dots and dashes
# blinks the morse code acc to input
def blink_morse_code(message):
    for char in message:
        if char == '.':
            blink_dot()
        elif char == '-':
            blink_dash()
        elif char == ' ':
            time.sleep(1)  #  duration between words
            
# function used for converting text to morse message and then use blink morse code function
def convert_and_blink():
    input_text = entry.get()
    morse_message = text_to_morse(input_text)
    blink_morse_code(morse_message)


win= tk.Tk()
win.title("TASK 5.3D")
win.geometry('400x400')

label = tk.Label(win, text="Enter your name:")
label.pack(padx=20, pady=10)

entry = tk.Entry(win)
entry.pack(padx=20, pady=5)

convert_button = tk.Radiobutton(win, text="Convert and Blink the Morse Code", command=convert_and_blink)
convert_button.pack(pady=10)

win.mainloop()

# Cleanup GPIO
GPIO.cleanup()
