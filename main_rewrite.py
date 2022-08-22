import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("400x250")

def open_app():
    app = customtkinter.CTkToplevel()
    app.geometry("400x450")

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

    customtkinter.CTkButton(frame, text="Plan", text_font=("JetBrains Mono", 10)).pack(pady=10)

frame = customtkinter.CTkFrame(root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

customtkinter.CTkLabel(frame, text="Meet Meetings", text_font=("JetBrains Mono", 18)).pack(pady=20)
customtkinter.CTkLabel(frame, text="The best way to plan your meetings for", text_font=("JetBrains Mono", 10)).pack()
customtkinter.CTkLabel(frame, text="you, your co-workers and your employees.", text_font=("JetBrains Mono", 10)).pack()

customtkinter.CTkButton(frame, text="Open Application", text_font=("JetBrains Mono", 10), command=open_app).pack(pady=20)

root.mainloop()