import time
import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk(fg_color="black")
app.geometry("400x200")

label = ctk.CTkLabel(app, text="00:00:000", font=("Arial", 40))
label.pack(pady=50)

start_time = time.perf_counter()

def stopwatch():
    elapsed = time.perf_counter() - start_time

    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed * 1000) % 1000)

    label.configure(
        text=f"{minutes:02}:{seconds:02}:{milliseconds:03}"
    )

    app.after(1, stopwatch)  # 1ms refresh

stopwatch()

app.mainloop()
