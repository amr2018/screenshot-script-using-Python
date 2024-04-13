from uuid import uuid4
from mss import mss
import tkinter as tk

root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.attributes('-transparentcolor', 'white')

# screenshot function
def take_sreenshot():
    with mss() as sct:
        sct.shot(mon = -1, output = f'{str(uuid4())}.png')

# close full screen window function
def close_fullscreen(event = None):
    take_sreenshot()
    root.attributes('-fullscreen', False)
    root.destroy()

# add canvas to make it transparent
canvas = tk.Canvas(root, background='white')
canvas.pack(fill=tk.BOTH, expand=True)


root.bind('<Escape>', close_fullscreen)
root.mainloop()
