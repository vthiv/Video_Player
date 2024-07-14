import tkinter as tk

import Font_Manager as Fonts
from Check_Videos import CheckVideos
from Create_Video_List import CreateVideoList
from Update_Videos import UpdateVideos


def check_videos_clicked():
    Status.configure(text="Check Videos button was clicked!")
    CheckVideos(tk.Toplevel(window))

def create_video_clicked():
    Status.configure(text="Create Video button was clicked!")
    CreateVideoList(tk.Toplevel(window))

def update_videos_clicked():
    Status.configure(text="Update Video button was clicked!")
    UpdateVideos(tk.Toplevel(window))



window = tk.Tk()
window.geometry("520x150")
window.title("Video Player")

Fonts.configure()

# Creating a Header Widget
Header = tk.Label(window, text="Select an option by clicking one of the buttons below")
Header.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Creating three button
check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

create_video_list_btn = tk.Button(window, text="Create Video List", command=create_video_clicked)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_video_btn = tk.Button(window, text="Update Videos", command=update_videos_clicked)
update_video_btn.grid(row=1, column=2, padx=10, pady=10)

Status = tk.Label(window, text=" ", font=("Helvetica", 10))
Status.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
