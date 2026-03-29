import secrets
import customtkinter as ctk

# Character List
characters_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters_lowercase = "abcdefghijklmnopqrstuvwxyz"
characters_numbers = "0123456789"
characters_special = "!@#$%^&*()-_=+[]{}|;:,.<>?"


def generate_password(number_of_characters, character_list):
    password = ""
    for i in range (number_of_characters):
        password += secrets.choice(character_list)
    return(password)


def update_slider_password_value(value):
    label_password_length.configure(text = "Number of Characters: " + str(int(slider_password_length.get())))


def create_charakter_list():
    character_list=""
    if checkbox_lowercase.get() == 1:
        character_list += characters_lowercase
    if checkbox_uppercase.get() == 1:
        character_list += characters_uppercase
    if checkbox_numbers.get() == 1:
        character_list += characters_numbers
    if checkbox_special.get() == 1:
        character_list += characters_special
    return character_list


def onclick_generate_password():
    character_list = create_charakter_list()
    if character_list == "":
        entry_output.configure(state="normal")
        entry_output.delete(0, "end")
        entry_output.configure(state="readonly")
        return
    
    password = generate_password(int(slider_password_length.get()), character_list)
    entry_output.configure(state="normal")
    entry_output.delete(0, "end")
    entry_output.insert(0, password)
    entry_output.configure(state="readonly")

    if checkbox_autocopy.get() == 1:
        copy_to_clipboard()

def copy_to_clipboard():
    gui.clipboard_clear()
    gui.clipboard_append(entry_output.get())

gui = ctk.CTk()
gui.geometry ("320x437")
gui.title ("Password Generator")
gui.resizable(False, False)


# Frame with Password Length Slider and Label
frame_slider = ctk.CTkFrame(gui, width=300, height=60)
frame_slider.pack(pady = 10)
frame_slider.propagate(False)

label_password_length = ctk.CTkLabel(frame_slider, text="")
label_password_length.pack(padx=10, pady=5, anchor="w")

slider_password_length = ctk.CTkSlider(frame_slider, from_=10, to=30, command = update_slider_password_value, number_of_steps=20)
slider_password_length.pack(pady=0, fill="x", padx=5)
slider_password_length.set(20)

update_slider_password_value(0)


# Frame for Checkboxes
frame_checkboxes = ctk.CTkFrame(gui, width=300, height=245)
frame_checkboxes.pack()
frame_checkboxes.propagate(False)

label_include = ctk.CTkLabel(frame_checkboxes, text="Include:")
label_include.pack(anchor="w", padx=10, pady=3)

checkbox_uppercase = ctk.CTkCheckBox(frame_checkboxes, text = "Uppercase Letters",)
checkbox_uppercase.pack(anchor="w", padx=10, pady=5)
checkbox_uppercase.select()

checkbox_lowercase = ctk.CTkCheckBox(frame_checkboxes, text = "Lowercase Letters",)
checkbox_lowercase.pack(anchor="w", padx=10, pady = 5)
checkbox_lowercase.select()

checkbox_numbers = ctk.CTkCheckBox(frame_checkboxes, text = "Numbers")
checkbox_numbers.pack(anchor="w", padx=10, pady = 5)
checkbox_numbers.select()

checkbox_special = ctk.CTkCheckBox(frame_checkboxes, text = "Special Characters")
checkbox_special.pack(anchor="w", padx=10, pady = 5)
checkbox_special.select()

label_options = ctk.CTkLabel(frame_checkboxes, text="Options:")
label_options.pack(anchor="w", padx=10, pady=3)

checkbox_autocopy = ctk.CTkCheckBox(frame_checkboxes, text = "Copy to Clipboard Automatically")
checkbox_autocopy.pack(anchor="w", padx=10, pady = 5)


# Button to generate password
button_generate = ctk.CTkButton(gui, text="Generate Secure Password", width=300, height=40, command=onclick_generate_password)
button_generate.pack(pady=10)


# Password Box with copy button
frame_output = ctk.CTkFrame(gui, fg_color="transparent")
frame_output.pack()

entry_output = ctk.CTkEntry(frame_output, width=250, height=40,justify="center", state="readonly")
entry_output.pack(side="left", padx=(0, 5))

button_copy_password = ctk.CTkButton(
    frame_output,
    text="Copy",
    width=45,
    height=40,
    command=copy_to_clipboard,
    fg_color="green"
)

button_copy_password.pack(side="left")


gui.mainloop()