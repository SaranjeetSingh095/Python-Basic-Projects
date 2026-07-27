import random
import customtkinter as ctk

# ==================================================
#                VARIABLES
# ==================================================

width = 800
height = 500

words = [
    "Apple",
    "Car",
    "Book",
    "Tiger",
    "Laptop",
    "School",
    "Bus",
    "Orange",
    "Phone",
    "Mouse",
    "Keyboard",
    "Bottle",
    "Window",
    "Table",
    "Chair"
]

# ==================================================
#                WINDOW SETTINGS
# ==================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

win = ctk.CTk(fg_color="#0F1117")
win.title("Shadow Memory")
win.geometry(f"{width}x{height}")
win.resizable(False, False)

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

win.geometry(f"{width}x{height}+{x}+{y}")

# ==================================================
#                TITLE
# ==================================================

title = ctk.CTkLabel(
    win,
    text="🧠 SHADOW MEMORY",
    font=("Poppins", 34, "bold"),
    text_color="white"
)
title.pack(pady=(25,5))

subtitle = ctk.CTkLabel(
    win,
    text="Train Your Brain • Improve Your Memory",
    font=("Poppins",15),
    text_color="gray"
)
subtitle.pack()

level = ctk.CTkLabel(
    win,
    text="MEMORY BOOSTER ×5",
    font=("Poppins",22,"bold"),
    text_color="#00E5FF"
)
level.pack(pady=20)

# ==================================================
#                GAME
# ==================================================

selected_words = random.sample(words,5)

text = ctk.CTkLabel(
    win,
    text="   ".join(selected_words),
    font=("Poppins",24,"bold"),
    text_color="#00FF99"
)
text.pack(pady=20)

entry = ctk.CTkEntry(
    win,
    width=350,
    placeholder_text="Type all words here..."
)

result = ctk.CTkLabel(
    win,
    text="",
    font=("Poppins",18)
)

def check():
    user_words = entry.get().lower().split()
    correct = [w.lower() for w in selected_words]

    if user_words == correct:
        result.configure(
            text="🎉 Perfect! You remembered all words.",
            text_color="lime"
        )
    else:
        result.configure(
            text="❌ Wrong!\nCorrect: " + " ".join(selected_words),
            text_color="red"
        )

button = ctk.CTkButton(
    win,
    text="CHECK",
    width=180,
    height=40,
    fg_color="#00BFFF",
    hover_color="#009ACD",
    command=check
)

# Entry aur button ko pehle hide rakho
entry.pack_forget()
button.pack_forget()

def hide_words():
    text.configure(text="")

    entry.pack(pady=15)
    button.pack(pady=10)
    result.pack(pady=10)

# 5 second baad words hide
win.after(5000, hide_words)

# ==================================================
#                MAIN LOOP
# ==================================================

win.mainloop()
