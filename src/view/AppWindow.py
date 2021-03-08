import tkinter as tk
from typing import Callable


class AppWindow:
    def __init__(self,
                 callback: Callable):
        self.callback = callback
        self.__main: tk.Tk = tk.Tk()
        self.__main.title("FragmentVideoDownloader")
        self.__main.geometry("350x150+10+20")
        self.__main.resizable(False, False)

    def show(self):
        self.__render()
        self.__main.mainloop()

    def __render(self):
        tk.Label(self.__main, text="Video URL").grid(row=0, pady=10, padx=10)
        self.__is_audio_separated = tk.IntVar(value=0)

        audio_checkbox = tk.Checkbutton(self.__main, {
            "variable": self.__is_audio_separated,
            "text": "Audio URL",
            "command": lambda: self.__change_visibility(audio_input)
        })
        audio_checkbox.grid(row=1, column=0, padx=10)

        video_input = tk.Entry(self.__main, width=20)
        video_input.grid(row=0, column=1)

        audio_input = tk.Entry(self.__main, width=20)

        tk.Button(
            self.__main,
            text='start',
            command=lambda: self.callback(video_input.get(), audio_input.get())
        ).grid(row=2, column=1, sticky="e")

    def __change_visibility(self, entry):
        if self.__is_audio_separated.get() == 1:
            entry.grid(row=1, column=1)
        else:
            entry.grid_forget()
