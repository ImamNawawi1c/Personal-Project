import customtkinter as ctk
from scanner import scan_file

def start_scan():
    file = entry.get()
    result = scan_file(file)
    label_result.configure(text=result)

app = ctk.CTk()
app.geometry("400x250")
app.title("Virus Detector")

entry = ctk.CTkEntry(app,width=300)
entry.pack(pady=20)

btn = ctk.CTkButton(app,text="Scan File",command=start_scan)
btn.pack()

label_result = ctk.CTkLabel(app,text="")
label_result.pack(pady=20)

app.mainloop()