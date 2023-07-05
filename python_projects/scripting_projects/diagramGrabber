import os
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from PIL import ImageTk, Image


class_diagram = None  # Initialize the variable
image_label = None  # Initialize the image label

def handle_button_click():
    global class_diagram, image_label  # Access the global variables

    # Get the text from the input text box
    text = entry.get()
    image_path = get_image_path(text)

    if image_path:
        # Open the image file using PIL
        image = Image.open(image_path)

        # Resize the image if needed
        # image = image.resize((desired_width, desired_height))

        # Create a PhotoImage object from the PIL image
        class_diagram = ImageTk.PhotoImage(image)

        if image_label:
            # Update the existing image label
            image_label.configure(image=class_diagram)
        else:
            # Create the image label
            image_label = tk.Label(window, image=class_diagram)

        # Place the image label at the center of the window
        image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Resize the window to 720x800
        window.geometry("720x800")

        # Clear the text from the entry widget
        entry.delete(0, tk.END)


def get_image_path(passed_text):
    file_name = passed_text + ".PNG"
    root = "../VisioDiagram/class_diagrams/"
    path = os.path.join(root, file_name)
    return path


def handle_enter_key(event):
    handle_button_click()


def clear_placeholder(event):
    # Clear the placeholder text when the user clicks inside the entry widget
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)
        entry.configure(foreground="black")  # Reset the text color




################
# --- MAIN --- #
################

window = tk.Tk()

style = ttk.Style()
style.theme_use("clam")

window.title("DiagramGrabber")
window.geometry("275x80")
window.configure(bg="#483D8B")

# --INPUT LABEL-- #
bold = Font()

style.configure("Colored.TLabel", foreground="white")
label = ttk.Label(window, text="Grab a Visio Diagram", style="Colored.TLabel", background="#483D8B", padding=(2, 2))
label.pack()

# --TEXT BOX-- #
entry = tk.Entry(window, width=30, justify="center")
entry.pack(padx=4, pady=4)

placeholder_text = "Enter room number..."
entry.insert(0, placeholder_text)  # Set the initial placeholder text
entry.configure(foreground="#999999")  # Set the text color to a lighter shade


## -- BOTTOM LABEL -- ##
bottom_style = ttk.Style()
bottom_style.configure("Custom.TLabel", foreground="white", font=("TkDefaultFont", 7))
bottom_label = ttk.Label(window, text="Written by: Eric lovell | mccScripts\u2122", style="Custom.TLabel", justify="center", background="#483D8B", padding=(2, 2))
bottom_label.pack(side=tk.BOTTOM, anchor=tk.S)

# Bind the Enter key event to the entry widget
entry.bind("<Return>", handle_enter_key)

# Bind the FocusIn event to clear the placeholder text
entry.bind("<FocusIn>", clear_placeholder)

# Start the main event loop
window.mainloop()
