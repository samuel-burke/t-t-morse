"""
Author: Samuel Burke
Date: 3/23/22

parses raw text into morse code characters and morse code audio
"""
import time

import pygame

morse_key = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
    '¿': '..-.-',
    '¡': '--...-',
}

speed = 0.09  # 15 WPM
pygame.mixer.init()
pygame.mixer.music.load("static.wav")
dot = pygame.mixer.Sound("dot.wav")
dash = pygame.mixer.Sound("dash.wav")


def text_to_morse(text):
    """
    Converts text input into a list of corresponding morse code characters
    :param text: the text to convert
    :return: the list of morse code letters
    """
    words = text.upper().strip().split(" ")
    message = []
    for word in words:
        morse_word = []
        for c in word:
            if c in morse_key:
                morse_word.append(morse_key[c])
        message.append(morse_word)
    return message


def static_sound(func):
    """
    Adds a static sound to the message
    :param func: the message to wrap the static around
    :return: the static wrapped function
    """
    def sound_buffer(*args):
        pygame.mixer.music.play(-1)
        time.sleep(1)
        func(args[0])
        time.sleep(1)
        pygame.mixer.music.pause()
    return sound_buffer


@static_sound
def morse_to_sound(*args):
    """
    Converts morse code into audible dots and dashes with the conventional spacing
    :param args: the list of morse code letters
    """
    for word in args[0]:
        for letter in word:
            for dit_dah in letter:
                if dit_dah == ".":
                    pygame.mixer.Sound.play(dot)
                    time.sleep(speed)
                elif dit_dah == "-":
                    pygame.mixer.Sound.play(dash)
                    time.sleep(3 * speed)
                time.sleep(0.5 * speed)
            time.sleep(2.5 * speed)
        time.sleep(7 * speed)
