from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

# Function to check selected language and load appropriate UI
def check_func():
    global language_box
    global enter_text
    try:
        # Try to remove previous widgets if they exist
        change_btn.destroy()
        enter_text.destroy()
        
        # Check selected option and call corresponding function
        if language_box.get() == "Persian to English":
            combo_persian()
        else:
            combo_english()
    except:
        # If widgets don't exist yet, just load based on selection
        if language_box.get() == "Persian to English":
            combo_persian()
        else:
            combo_english()

# Function to copy result text to clipboard and close result window
def copy_func():
    global window_result
    global label_result
    window_result.clipboard_append(label_result.cget("text"))
    window_result.destroy()

# Function to convert English keyboard input to Persian
def eng_to_per():
    global window_result
    global enter_text
    global label_result
    
    # Dictionary mapping English keys to Persian characters
    english_dict = {
        'q': 'ض', 'w': 'ص', 'e': 'ث', 'r': 'ق', 't': 'ف', 'y': 'غ',
        'u': 'ع', 'i': 'ه', 'o': 'خ', 'p': 'ح', '[': 'ج', ']': 'چ',
        'a': 'ش', 's': 'س', 'd': 'ی', 'f': 'ب', 'g': 'ل', 'h': 'ا',
        'j': 'ت', 'k': 'ن', 'l': 'م', ';': 'ک', "'": 'گ',
        'z': 'ظ', 'x': 'ط', 'c': 'ز', 'v': 'ر', 'b': 'ذ',
        'n': 'د', 'm': 'پ', ',': 'و', '.': '.', '/': '/',
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹',
        ' ': ' '
    }

    # Get user input from text box
    value = enter_text.get("1.0", "end-1c")
    new_text = value

    # Replace characters using dictionary
    for key in english_dict.keys():
        new_text = new_text.replace(key, english_dict[key])

    # Create result window
    window_result = Tk()
    window_result.geometry("500x500")
    window_result.resizable(False, False)
    window_result.title("change language")
    window_result.config(cursor="pencil")

    # Display converted text
    label_result = Label(window_result,
                         text=new_text,
                         font=("Bnazanin", 20),
                         background="#FFFFFF",
                         foreground="#000000")
    label_result.place(relx=0.5, rely=0.5, anchor="center")

    # Copy button
    copy_btn = Button(window_result,
                      text="کپی",
                      font=("Bnazanin", 20),
                      command=copy_func)
    copy_btn.place(relx=0.5, y=450, anchor="center")

    window_result.mainloop()

# Function to convert Persian keyboard input to English
def per_to_eng():
    global window_result
    global enter_text
    global label_result

    # Dictionary mapping Persian characters to English keys
    persian_dict = {
        'ض': 'q', 'ص': 'w', 'ث': 'e', 'ق': 'r', 'ف': 't',
        'غ': 'y', 'ع': 'u', 'ه': 'i', 'خ': 'o', 'ح': 'p',
        'ج': '[', 'چ': ']',
        'ش': 'a', 'س': 's', 'ی': 'd', 'ب': 'f', 'ل': 'g',
        'ا': 'h', 'ت': 'j', 'ن': 'k', 'م': 'l', 'ک': ';', 'گ': "'",
        'ظ': 'z', 'ط': 'x', 'ز': 'c', 'ر': 'v', 'ذ': 'b',
        'د': 'n', 'پ': 'm', 'و': ',', '.': '.', '/': '/',
        ' ': ' '
    }

    # Get user input
    value = enter_text.get("1.0", "end-1c")
    new_text = value

    # Replace characters using dictionary
    for key in persian_dict.keys():
        new_text = new_text.replace(key, persian_dict[key])

    # Create result window
    window_result = Tk()
    window_result.geometry("500x500")
    window_result.resizable(False, False)
    window_result.title("change language")
    window_result.config(cursor="pencil")

    # Display result
    label_result = Label(window_result,
                         text=new_text,
                         font=("Arial", 20),
                         background="#FFFFFF",
                         foreground="#000000")
    label_result.place(relx=0.5, rely=0.5, anchor="center")

    # Copy button
    copy_btn = Button(window_result,
                      text="کپی",
                      font=("Bnazanin", 20),
                      command=copy_func)
    copy_btn.place(relx=0.5, y=450, anchor="center")

    window_result.mainloop()

# UI setup for Persian input mode
def combo_persian():
    global enter_text
    enter_text = Text(window,
                      font=("Bnazanin", 20),
                      foreground="#85C0ED")
    enter_text.place(relx=0.5, y=140, anchor="center", width=300, height=150)

    # Button to trigger conversion
    change_btn = Button(window,
                        text="تغییر",
                        font=("Bnazanin", 20),
                        command=per_to_eng)
    change_btn.place(relx=0.5, y=250, anchor="center")

# UI setup for English input mode
def combo_english():
    global enter_text
    global change_btn

    enter_text = Text(window,
                      font=("Arial", 20),
                      foreground="#85C0ED")
    enter_text.place(relx=0.5, y=140, anchor="center", width=300, height=150)

    # Button to trigger conversion
    change_btn = Button(window,
                        text="change",
                        font=("Arial", 20),
                        command=eng_to_per)
    change_btn.place(relx=0.5, y=250, anchor="center")

# Main application window
window = Tk()
window.geometry("500x500")
window.resizable(False, False)
window.title("change language")
window.config(cursor="pencil")

# Dropdown for language selection
language_box = Combobox(window,
                        font=("Bnazanin", 14),
                        width=30,
                        state="readonly",
                        justify="center")

# Options for conversion direction
language_box["value"] = ("Persian to English", "انگلیسی به فارسی")
language_box.set("Persian to English")
language_box.place(relx=0.5, y=30, anchor="center")

# Start button
check_language = Button(window,
                        text="Start",
                        font=("Arial", 20),
                        command=check_func)
check_language.place(relx=0.5, y=400, anchor="center", width=100, height=100)

# Run application
window.mainloop()