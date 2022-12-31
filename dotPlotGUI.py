import tkinter as tk
import Alignment.dotPlot as dp

def clearFrame():
    # destroy all widgets from window
    for widget in window.winfo_children():
       widget.destroy()

def initialize(event):
    clearFrame()
    global greeting, textBox1, textBox2, button1, button2, button3
    greeting = tk.Label(text = "Welcome to Mike's Dot-Plot Alignment", font=('Arial',17,'bold'), fg = "black")
    seq1Label = tk.Label(text = "Enter sequence 1:", font=('Arial',11,'bold'), fg = "black")
    seq2Label = tk.Label(text = "Enter sequence 2:", font=('Arial',11,'bold'), fg = "black")
    textBox1 = tk.Text(fg="black", bg="white", width=30, height = 1)
    textBox2 = tk.Text(fg="black", bg="white", width=30, height = 1)
    button1 = tk.Button(
        text="Get matrix",
        width=10,
        height=1,
        bg="purple",
        fg="white",
        font = "bold"
    )
    button2 = tk.Button(
        text="Get score",
        width=10,
        height=1,
        bg="purple",
        fg="white",
        font = "bold"
    )
    button3 = tk.Button(
        text="Reset",
        width=10,
        height=1,
        bg="purple",
        fg="white",
        font = "bold"
    )
    greeting.place(relx = 0.5, rely = 0.05, anchor="center")

    seq1Label.place(relx = 0.32, rely = 0.15, anchor = "center")
    seq2Label.place(relx = 0.32, rely = 0.2, anchor = "center")

    textBox1.place(relx = 0.57, rely = 0.15, anchor = "center")

    textBox2.place(relx = 0.57, rely = 0.2, anchor = "center")
    
    button1.place(relx = 0.3, rely = 0.3, anchor = "center")
    
    button2.place(relx = 0.5, rely = 0.3, anchor = "center")

    button3.place(relx = 0.7, rely = 0.3, anchor = "center")
    
    button1.bind("<Button>", getDP)

    button2.bind("<Button>", getScore)

    button3.bind("<Button>", initialize)
    
def getDP(event):
    global matrix, seq1, seq2
    seq1 = seq2 = ""
    matrix = []

    seq1 = textBox1.get(1.0, "end-1c")
    seq2 = textBox2.get(1.0, "end-1c")
    
    matrix = dp.generateMatrix(len(seq1), len(seq2))
    dp.dot_plot(matrix, seq1, seq2)
    
    generateLabel(' ', 0, 0)
    for k in range(len(seq1)):
        generateLabel(seq1[k], k + 1, 0)
    
    for i in range (len(matrix)):
        generateLabel(seq2[i], 0, i + 1)
        for j in range (len(matrix[i])):
            generateLabel(matrix[i][j], j + 1, i + 1)
   
def getScore(event):
    score = tk.Label(text = "The alignment score is " + str(dp.scoring(matrix)), 
                     font=('Arial',15,'bold'), fg = "red")
    score.place(relx = 0.5, rely = 0.9, anchor="center")

def generateLabel(nuc, posX, posY):
    if nuc == 'A' or nuc == 'a':
        lb = tk.Label(
            text = 'A',
            bg = 'red',
            fg = 'white',
            width=2,
        )
    elif nuc == 'T' or nuc == 't':
        lb = tk.Label(
            text = 'T',
            bg = 'green',
            fg = 'white',
            width = 2
        )
    elif nuc == 'C' or nuc == 'c':
        lb = tk.Label(
            text = 'C',
            bg = 'orange',
            fg = 'white',
            width = 2
        )
    elif nuc == 'G' or nuc == 'g':
        lb = tk.Label(
            text = 'G',
            bg = 'blue',
            fg = 'white',
            width = 2
        )
    else:
        lb = tk.Label(
            text = nuc,
            bg = 'white',
            fg = 'black',
            width = 2
        )
    lb.config(anchor = 'center')
    lb.place(relx = (1-len(seq1) * 0.03)/2 + posX * 0.03, rely = 0.4 + posY * 0.05, anchor = "center")

window = tk.Tk() # create a window instance
initialize(1) # initialize all the starting widgets

window.title("Dot-Plot Simulation by Mike") # give it a title
window.geometry("800x500") # set dimensions
window.mainloop() # show the window