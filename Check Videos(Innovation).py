import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst

import Video_Library as Library
import Font_Manager as Fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


def only_numbers(char):
    return char.isdigit()


class CheckVideos():
    def __init__(self, window):
        window.geometry("750x600")
        window.title("Check Videos")

        Enter = tk.Label(window, text="Check Video", font=("Arial Bold", 20))
        Enter.grid(row=0, column=0, padx=10, pady=10)

        Enter = tk.Label(window, text="Enter the video number (01-05)")
        Enter.grid(row=1, column=0, padx=5, pady=5)

        validation = window.register(only_numbers)
        self.input_txt = tk.Entry(window, width=3, validate="key", validatecommand=(validation, '%S'))
        self.input_txt.grid(row=1, column=1, padx=5, pady=5)

        check_video_no_btn = tk.Button(window, text="Check Video", command=self.check_video_no)
        check_video_no_btn.grid(row=1, column=3, padx=10, pady=10)

        Enter1 = tk.Label(window, text="Enter the video name")
        Enter1.grid(row=2, column=0, padx=5, pady=5)

        self.input_txt1 = tk.Entry(window, width=20)
        self.input_txt1.grid(row=2, column=1, padx=5, pady=5)

        check_video_name_btn = tk.Button(window, text="Check Video Name", command=self.check_video_name)
        check_video_name_btn.grid(row=2, column=3, padx=10, pady=10)

        Enter2 = tk.Label(window, text="Select the director name")
        Enter2.grid(row=3, column=0, padx=5, pady=5)

        self.combo = ttk.Combobox(window, width=25)
        self.combo["values"] = [" ", "Fred Quimby", "Blake Edwards", "Michael Curtiz", "Robert Wise", "Victor Fleming"]
        self.combo.current(0)
        self.combo.grid(row=3, column=1, padx=5, pady=5)

        check_directory_btn = tk.Button(window, text="Check Directory", command=self.check_directory)
        check_directory_btn.grid(row=3, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=6, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=10, column=0, columnspan=4, sticky="W", padx=10, pady=10)

    def check_video_no(self):
        key = self.input_txt.get()
        name = Library.get_name(key)
        if name is not None:
            director = Library.get_director(key)
            rating = Library.get_rating(key)
            play_count = Library.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.list_txt, video_details)
        else:
            set_text(self.list_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def check_video_name(self):
        key = self.input_txt1.get()
        name = Library.get_name(key)
        if name is not None:
            director = Library.get_director(key)
            rating = Library.get_rating(key)
            play_count = Library.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.list_txt, video_details)
        else:
            set_text(self.list_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Directory button was clicked!")

    def check_directory(self):
        key = self.combo.current()
        name = Library.get_name(key)
        if name is not None:
            rating = Library.get_rating(key)
            play_count = Library.get_play_count(key)
            video_details = f"{name}\nrating: {rating}\nplays: {play_count}"
            set_text(self.list_txt, video_details)
        else:
            set_text(self.list_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Directory button was clicked!")


if __name__ == "__main__":
    window = tk.Tk()
    Fonts.configure()
    CheckVideos(window)
    window.mainloop()
