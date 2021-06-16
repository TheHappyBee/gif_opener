import tkinter as tk
from tkinter import filedialog as fd
import time
import threading
import os
from PIL import Image
import system as sys
def get_avg_fps(PIL_Image_object):
    """ Returns the average framerate of a PIL Image object """
    PIL_Image_object.seek(0)
    frames = duration = 0
    while True:
        try:
            frames += 1
            duration += PIL_Image_object.info['duration']
            PIL_Image_object.seek(PIL_Image_object.tell() + 1)
        except EOFError:
            return frames / duration * 1000
    return None
def getfile():
     file = fd.askopenfilename()
     img = Image.open(file)
     fps = get_avg_fps(img)
     size = os.path.getsize(file)
     file_words = []
     for word in file:
          file_words.append(word)
     if file_words[-3]+file_words[-2]+file_words[-1] != 'gif':
          print("not a valid file type")
          return
     
          
     window = tk.Toplevel()
     def run_gif():
          i = 0
          while True:
               try:
                    photo = tk.PhotoImage(file = file,format="gif -index" +' '+ str(i))
                    gif = tk.Label(window, image=photo)
                    gif.grid(row=0,column=0)
                    i += 1
                    time.sleep(1/fps)
               except:
                    i = 0
     gif_thread=threading.Thread(target=run_gif)
     gif_thread.start()
     window.mainloop()
     sys.exit()
          
          
def display():
     root = tk.Tk()
     root.title(".gif opener")
     root.geometry('50x100')
     root.configure(bg = "lightgreen")
     label = tk.Label(root, text = ".gif opener")
     label.pack()
     button = tk.Button(root, text = "File", command = getfile)
     button.place(x = "50", y= "50")
     root.mainloop()

display()
