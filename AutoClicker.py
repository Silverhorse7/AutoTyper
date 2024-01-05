import tkinter as tk
from tkinter import ttk
import pyautogui
import time
import threading
import keyboard
import random

class AutoTyper:
    def __init__(self):
        self.typing = False

    def start_typing(self):
        text = text_entry.get("1.0", tk.END)
        lines = text.splitlines()

        try:
            start_wps = float(start_wps_entry.get())
            end_wps = float(end_wps_entry.get())
        except ValueError:
            result_label.config(text="Please enter valid numbers for WPS!")
            return

        if start_wps <= 0 or end_wps <= 0:
            result_label.config(text="WPS should be greater than 0!")
            return

        self.typing = True
        result_label.config(text="Starting in 3 seconds...")
        window.update()
        time.sleep(3)

        for line in lines:
            words = line.split()
            for word in words:
                if not self.typing:
                    break

                for char in word:
                    if not self.typing:
                        break
                    pyautogui.press(char)

                interval = random.uniform(1/start_wps, 1/end_wps)
                time.sleep(interval)

                if not self.typing or word == words[-1]:
                    continue
                pyautogui.press("space")

            if not self.typing or line == lines[-1]:
                continue
            pyautogui.press("enter")

        result_label.config(text="Done typing!" if self.typing else "Typing stopped!")
        self.typing = False

    def toggle_typing(self):
        if self.typing:
            self.typing = False
        else:
            threading.Thread(target=self.start_typing).start()

auto_typer = AutoTyper()

def on_f10_key():
    auto_typer.toggle_typing()

keyboard.add_hotkey('f10', on_f10_key)

window = tk.Tk()
window.title("Auto Typer")

frame = ttk.Frame(window, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

text_label = ttk.Label(frame, text="Enter your text:")
text_label.grid(row=0, column=0, sticky=tk.W, pady=5)

text_entry = tk.Text(frame, height=10, width=40)
text_entry.grid(row=1, column=0, columnspan=2, pady=5)

start_wps_label = ttk.Label(frame, text="Start WPS:")
start_wps_label.grid(row=2, column=0, sticky=tk.W, pady=5)

start_wps_entry = ttk.Entry(frame)
start_wps_entry.grid(row=2, column=1, pady=5)

end_wps_label = ttk.Label(frame, text="End WPS:")
end_wps_label.grid(row=3, column=0, sticky=tk.W, pady=5)

end_wps_entry = ttk.Entry(frame)
end_wps_entry.grid(row=3, column=1, pady=5)

start_button = ttk.Button(frame, text="Start Typing (F10)", command=auto_typer.toggle_typing)
start_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=5)

window.mainloop()
