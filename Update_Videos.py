import tkinter as tk
import tkinter.ttk as ttk

import Video_Library as Library
import Font_Manager as Fonts


def set_text(text_area, content):  # inserts content into the text_area
    text_area.delete("1.0", tk.END)  # first the existing content is deleted
    text_area.insert(1.0, content)  # then the new content is inserted


def add_text(text_area, content):
    text_area.insert(1.0, content)


def only_numbers(char):
    return char.isdigit()


class UpdateVideos():
    def __init__(self, window):  # __init__ is initialize the object and self is represent the instance of the class
        window.geometry("1000x400")  # give a container size which can include widgets in GUI
        window.title("Update Videos")  # title which appear on top of the GUI when view it

        Enter = tk.Label(window, text="Enter the video number")
        Enter.grid(row=0, column=0, padx=5, pady=5)

        validation = window.register(only_numbers)
        self.input_txt = tk.Entry(window, width=3, validate="key", validatecommand=(validation, '%S'))
        self.input_txt.grid(row=0, column=1, padx=5, pady=5)

        Enter1 = tk.Label(window, text="Select new rating")
        Enter1.grid(row=1, column=0, padx=5, pady=5)

        self.combo = ttk.Combobox(window, width=10)
        self.combo["values"] = [" ", "1 Star", "2 Star", "3 Star", "4 Star", "5 Star"]
        self.combo.current(0)
        self.combo.grid(row=2, column=0, padx=5, pady=5)

        self.detail_txt = tk.Text(window, width=30, height=10, wrap="none")
        self.detail_txt.grid(row=0, column=3, sticky="NW", padx=5, pady=5)

        add_btn = tk.Button(window, text="Add the list", command=self.add_video)
        add_btn.grid(row=1, column=3)

        self.detail_txt2 = tk.Text(window, width=30, height=10, wrap="none")
        self.detail_txt2.grid(row=0, column=4, sticky="NW", padx=5, pady=5)

        update_btn = tk.Button(window, text="Update in the list", command=self.update)
        update_btn.grid(row=1, column=4)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=7, column=2, columnspan=4, sticky="W", padx=10, pady=10)

    def add_video(self):
        Library.play_count = 0
        key = self.input_txt.get()
        name = Library.get_name(key)
        if name is not None:
            director = Library.get_director(key)
            rating = Library.get_rating(key)
            play_count = Library.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count} \n \n \n"
            add_text(self.detail_txt, video_details)
        else:
            add_text(self.detail_txt, f"Video {key} not found \n \n \n")
        self.status_lbl.configure(text="Add Video was clicked!")

    def update(self):
        key = self.input_txt.get()
        name = Library.get_name(key)
        rating = self.combo.get()

        if name is not None:
            director = Library.get_director(key)
            rating = self.combo.get()
            play_count = Library.get_play_count(key)
            video_details = f"{name} \n{director} \nrating: {rating} \nplays: {play_count} \n \n \n"
            set_text(self.detail_txt2, video_details)
        else:
            set_text(self.detail_txt2, f"Video {key} not found \n \n \n \n")
        self.status_lbl.configure(text="Update button was clicked")


if __name__ == "__main__":
    window = tk.Tk()
    Fonts.configure()
    UpdateVideos(window)
    window.mainloop()
