import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("400x350")
root.iconbitmap("Main.ico")
root.title("Meet Meetings")

def dark_theme():
    customtkinter.set_appearance_mode("dark")

def light_theme():
    customtkinter.set_appearance_mode("light")


def open_app():
    def plan():
        planned = customtkinter.CTkToplevel()
        planned.geometry("500x200")
        planned.iconbitmap("Main.ico")
        planned.title("Meet Meetings")

        frame = customtkinter.CTkFrame(planned)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        plannedMeeting = open(f"{file_name.get()}.txt", "w")
        plannedMeeting.write(f"Date & Time: {time.get()}")
        plannedMeeting.write(f"\nKey Point 1: {key1.get()}")
        plannedMeeting.write(f"\nKey Point 2: {key2.get()}")
        plannedMeeting.write(f"\nKey Point 3: {key3.get()}")
        plannedMeeting.write(f"\nNotes: {notes.get()}")

        customtkinter.CTkLabel(frame, text=f"Your meeting has been planned and saved to file {file_name.get()}.txt!", text_color="#219145", text_font=("JetBrains Mono", 10)).pack()

        customtkinter.CTkLabel(frame, text=f"Date & Time: {time.get()}", text_font=("JetBrains Mono", 10)).pack()
        customtkinter.CTkLabel(frame, text=f"Key Point 1: {key1.get()}", text_font=("JetBrains Mono", 10)).pack()
        customtkinter.CTkLabel(frame, text=f"Key Point 2: {key2.get()}", text_font=("JetBrains Mono", 10)).pack()
        customtkinter.CTkLabel(frame, text=f"Key Point 3: {key3.get()}", text_font=("JetBrains Mono", 10)).pack()
        customtkinter.CTkLabel(frame, text=f"Notes: {notes.get()}", text_font=("JetBrains Mono", 10)).pack()

    app = customtkinter.CTkToplevel()
    app.geometry("400x500")
    app.iconbitmap("Main.ico")
    app.title("Meet Meetings")

    frame = customtkinter.CTkFrame(app)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    file_name = customtkinter.CTkEntry(frame, placeholder_text="File Name", text_font=("JetBrains Mono", 10))
    file_name.pack(pady=20)

    time = customtkinter.CTkEntry(frame, placeholder_text="Date & Time", text_font=("JetBrains Mono", 10))
    time.pack(pady=20)

    key1 = customtkinter.CTkEntry(frame, placeholder_text="Key Point 1", text_font=("JetBrains Mono", 10))
    key1.pack(pady=20)

    key2 = customtkinter.CTkEntry(frame, placeholder_text="Key Point 2", text_font=("JetBrains Mono", 10))
    key2.pack(pady=20)

    key3 = customtkinter.CTkEntry(frame, placeholder_text="Key Point 3", text_font=("JetBrains Mono", 10))
    key3.pack(pady=20)

    notes = customtkinter.CTkEntry(frame, placeholder_text="Notes", text_font=("JetBrains Mono", 10))
    notes.pack(pady=20)

    customtkinter.CTkButton(frame, text="Plan", text_font=("JetBrains Mono", 10), command=plan).pack(pady=10)

frame = customtkinter.CTkFrame(root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

customtkinter.CTkLabel(frame, text="Meet Meetings", text_font=("JetBrains Mono", 18)).pack(pady=20)
customtkinter.CTkLabel(frame, text="v2.0.0", text_font=("JetBrains Mono", 10)).pack()

customtkinter.CTkLabel(frame, text="The best way to plan your meetings for", text_font=("JetBrains Mono", 10)).pack()
customtkinter.CTkLabel(frame, text="you, your co-workers and your employees.", text_font=("JetBrains Mono", 10)).pack()

customtkinter.CTkButton(frame, text="Open Application", text_font=("JetBrains Mono", 10), command=open_app).pack(pady=10)
customtkinter.CTkButton(frame, text="Dark Theme", text_font=("JetBrains Mono", 10), command=dark_theme).pack(pady=10)
customtkinter.CTkButton(frame, text="Light Theme", text_font=("JetBrains Mono", 10), command=light_theme).pack(pady=10)

root.mainloop()