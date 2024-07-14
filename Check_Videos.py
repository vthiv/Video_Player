import tkinter as tk
import tkinter.scrolledtext as tkst

import Video_Library as Library
import Font_Manager as Fonts


def set_text(text_area, content):   # inserts content into the text_area
    text_area.delete("1.0", tk.END) # first the existing content is deleted
    text_area.insert(1.0, content)  # then the new content is inserted

def only_numbers(char):
    return char.isdigit()


class CheckVideos():
    def __init__(self, window): #Defining the function
        window.geometry("750x350") # give the window size
        window.title("Check Videos") # title which appear on top of the GUI when view it

        #List up all the videos details and grid used to position up the button
        list_videos_btn = tk.Button(window, text="List of all videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        #Create a label and position up the label
        Enter = tk.Label(window, text="Enter the video number")
        Enter.grid(row=0, column=1, padx=10, pady=10)

        # Create a entry box for user to key in the input and position up the entry box
        validation = window.register(only_numbers)
        self.input_txt = tk.Entry(window, width=3, validate="key", validatecommand=(validation, '%S'))
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Create a button to check the video text and position up the button
        check_videos_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_videos_btn.grid(row=0, column=3, padx=10, pady=10)

        #List up all the video details in scrollable text box, which can adjust the text box size
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # A text box for video detail to appear and position up the text box
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # A status label when a button is clicked and position up the label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Show's all list of videos to user
        self.list_videos_clicked()

#Define the check video button
    def check_video_clicked(self):
        key = self.input_txt.get() #Get input from user
        name = Library.get_name(key) #Convert the input key to the video name
        if name is not None:  #when name is match, a valid output will appear, if not there will be no output
            director = Library.get_director(key) #Get the values that match the key
            rating = Library.get_rating(key)  #Get the values that match the key
            play_count = Library.get_play_count(key) #Get the values that match the key
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}" #Display the output with correct details
            set_text(self.video_txt, video_details) #Appear the correct details in the text box
        else:
            set_text(self.video_txt, f"Video {key} not found")  #if the details wrong, this text will appear
        self.status_lbl.configure(text="Check Video button was clicked!") #when the button is clicked then this label will appear

    def list_videos_clicked(self): #List out all the video details
        video_list = Library.list_all() #Get the video list
        set_text(self.list_txt, video_list) # Set the list text in the video list
        self.status_lbl.configure(text="List of videos button was clicked!") #when the button is clicked then this label will appear


if __name__ == "__main__": #Execute the code when the file run directly
    window = tk.Tk() # A tkinter window
    Fonts.configure() # A font style that used in this code
    CheckVideos(window) # Open up this window in GUI
    window.mainloop() # Runs the window, whenever a button is clicked
