from tkinter import *

# One function (one algorithm) to draw a face
def draw_face(canvas, x, y, color, mood):
    # Face circle
    canvas.create_oval(x-50, y-50, x+50, y+50, fill=color, outline="black")

    # Eyes
    canvas.create_oval(x-25, y-20, x-15, y-10, fill="black")
    canvas.create_oval(x+15, y-20, x+25, y-10, fill="black")

    # Mouth - changes based on mood
    if mood == "happy":
        canvas.create_arc(x-25, y-10, x+25, y+20, start=180, extent=180, style=ARC, width=2)
    elif mood == "sad":
        canvas.create_arc(x-25, y+10, x+25, y+30, start=0, extent=180, style=ARC, width=2)
    elif mood == "surprised":
        canvas.create_oval(x-10, y, x+10, y+20, outline="black", width=2)

# Main window
root = Tk()
root.title("One Algo Three Faces")

canvas = Canvas(root, width=400, height=200, bg="white")
canvas.pack()

# Draw three faces using same function (algorithm)
draw_face(canvas, 80, 100, "yellow", "happy")
draw_face(canvas, 200, 100, "lightblue", "sad")
draw_face(canvas, 320, 100, "pink", "surprised")

root.mainloop()
