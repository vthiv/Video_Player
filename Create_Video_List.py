import tkinter as tk

import Video_Library as Library
import Font_Manager as Fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


def add_text(text_area, content):
    text_area.insert(1.0, content)


def only_numbers(char):
    return char.isdigit()


class CreateVideoList:
    def __init__(self, window):
        window.geometry("800x300")
        window.title("Create Video List")

        Enter = tk.Label(window, text="Enter the video number (01-05)")
        Enter.grid(row=0, column=1, padx=10, pady=10)

        validation = window.register(only_numbers)
        self.input_txt = tk.Entry(window, width=3, validate="key", validatecommand=(validation, '%S'))
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        add_video_btn = tk.Button(window, text="Add Video", command=self.add_video_clicked)
        add_video_btn.grid(row=1, column=3, padx=10, pady=10)

        self.video_txt = tk.Text(window, width=20, height=10, wrap="none")
        self.video_txt.grid(row=0, column=3, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.video_txt2 = tk.Text(window, width=20, height=10, wrap="none")
        self.video_txt2.grid(row=0, column=4, sticky="W", padx=10, pady=10)

        play_btn = tk.Button(window, text="Play", command=self.play_clicked)
        play_btn.grid(row=1, column=4, padx=10, pady=10)

        clear_btn = tk.Button(window, text="Clear", command=self.clear_clicked)
        clear_btn.grid(row=1, column=1, padx=10, pady=10)

    def add_video_clicked(self):
        Library.play_count = 0
        key = self.input_txt.get()
        name = Library.get_name(key)
        if name is not None:
            director = Library.get_director(key)
            rating = Library.get_rating(key)
            play_count = Library.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count} \n"
            add_text(self.video_txt, video_details)
        else:
            add_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Add Video was clicked!")

    def play_clicked(self):
        key = self.input_txt.get()
        name = Library.get_name(key)
        play_count = Library.get_play_count(key)

        if name is not None:
            Library.increment_play_count(key)
            video_details = f"{name}\nplays: {play_count} \n"
            set_text(self.video_txt2, video_details)
        else:
            set_text(self.video_txt2, f"Video {key} not found \n ")
        self.status_lbl.configure(text="Play Video button was clicked!")

    def clear_clicked(self):
        self.input_txt.delete(0, "end")
        self.video_txt.delete("1.0", "end")
        self.video_txt2.delete("1.0", "end")
        self.status_lbl.configure(text="Video was cleared")


if __name__ == "__main__":
    window = tk.Tk()
    Fonts.configure()
    CreateVideoList(window)
    window.mainloop()
