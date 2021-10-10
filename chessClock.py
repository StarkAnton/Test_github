import tkinter as tk
HEIGHT = 600
WIDTH = 800
root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="gray")
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

label = tk.Label(frame, text="enter name")
label.pack()
entry = tk.Entry(frame, bg="red")
entry.pack()


#currentPlayerButton1 = tk.Button(root)
#waitingPlayerButton2 = tk.Button(root)
#Button1.pack()
#Button2.pack()
root.mainloop()
#window.title("test")
