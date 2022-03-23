"""
Author: Samuel Burke
Date: 3/23/22

Main GUI that uses the morse.py functionality
"""
import tkinter as tk

import pyperclip

import morse

background = 'gray15'
text_color = "#55c62b"
text_bg = "gray17"
font = "Krungthep"


class GUI:
    """
    Main GUI for morse code translator
    """

    def __init__(self):
        """
        Constructs a GUI window
        """
        self.window = tk.Tk()
        self.window.title("Morse Code Encoder")
        self.window.config(bg=background, pady=50, padx=0)
        self.message_label = tk.Label(text="Enter Message", bg=background, fg=text_color, font=(font, 35, "bold"))
        self.message_label.grid(column=0, row=0)

        self.message = tk.Text(insertbackground=text_color, height=4, width=40, bg=text_bg, fg=text_color,
                               font=(font, 16, "bold"))
        self.message.config(highlightthickness=0)
        self.message.grid(column=0, row=1)

        self.canvas = tk.Canvas(width=500, height=200, bg=background, highlightthickness=0)
        self.wave = tk.PhotoImage(file="wave.png")
        self.canvas.create_image(250, 100, image=self.wave)
        self.canvas.grid(column=0, row=2)

        self.play = tk.Button(command=self.play, text="PLAY", width=10, height=2, highlightthickness=0, font=font,
                              borderwidth=0)
        self.play.grid(column=0, row=3)
        self.window.mainloop()

    def play(self):
        """
        method executed when user clicks the 'play' button. Function copys the morse code text to the clipboard and
        plays the morse code audio.
        """
        text = self.message.get(1.0, tk.END)
        morse_message = morse.text_to_morse(text)
        output_string = ""
        for word in morse_message:
            for letter in word:
                for c in letter:
                    output_string += c
                output_string += " "
            output_string += " / "
        pyperclip.copy(output_string[:-4])
        morse.morse_to_sound(morse_message)
        popup = tk.Toplevel(self.window)
        popup.title("Copied")
        popup.config(padx=25, pady=50, bg=background)
        message = tk.Label(popup)
        message.config(text="Copied to clipboard!", pady=20, bg=background, fg=text_color, font=(font, 16, "bold"))
        message.grid(column=0, row=0)
        ok = tk.Button(popup, pady=5, command=popup.destroy, text="OK", highlightthickness=0, font=font,
                       borderwidth=0)
        ok.grid(column=0, row=1)


if __name__ == "__main__":
    GUI()
