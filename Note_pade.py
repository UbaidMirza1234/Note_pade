import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = tk.Tk()
root.title("MyNotePad")
root.rowconfigure(0, minsize=800)
root.columnconfigure(1, minsize=800)

text_editor = tk.Text(root)
text_editor.grid(row=0, column=1)

frame_button = tk.Frame(root, relief=tk.RAISED, bd=2)
frame_button.grid(row=0, column=0)

button_open = tk.Button(frame_button, text="Open")
button_open.grid(row=0, column=0, padx=5, pady=5)

button_save = tk.Button(frame_button, text="Save")
button_save.grid(row=1, column=0, padx=5, pady=5)

frame_button

root.mainloop()