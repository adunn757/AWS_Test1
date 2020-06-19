import tkinter as tk
from tkinter import filedialog, Text
import os

header_font = "ariel 12 bold"

root = tk.Tk()
'''
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/",
                                      title="Select File",
                                      filetypes= (("exicutables", "*.exe"),
                                                  ("all files", "*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()

'''
canvas = tk.Canvas(root, height=500, width=700, bg="CadetBlue3")
canvas.pack()
'''
def runApps():
    for app in apps:
        print(app)
        os.startfile(app)
'''

def upload_excell():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select File",
                                          filetypes=(("Excell Files", "*.xlsx"),
                                                     ("all files", "*.*")))
    label2 = tk.Label(frame, text=filename, anchor="w")
    label2.place(relwidth=1, relheight=1, relx=0, rely=0.5, anchor=tk.W)


'''    
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely=0.1)
'''
upload = tk.Button(root, text="Browse", padx=10, pady=5,
                     fg='black', bg="white", command=upload_excell)
upload.place(relwidth=0.1, relheight=0.05, relx=0.8, rely=0.3, anchor=tk.NW)

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.7, relheight=0.05, relx=0.1, rely=0.3)
label1 = tk.Label(root, text="Import From:", font=header_font, bg="CadetBlue3")
label1.place(relx=0.1, rely=0.25, anchor=tk.W)


label3 = tk.Label(root, text="Sampling Frequency:", font=header_font, bg="CadetBlue3")
label3.place(relx=0.1, rely=0.45, anchor=tk.W)
frequency = tk.StringVar(root)
frequency_options = {'100Hz', '250Hz', '500Hz', '1000Hz'}
frequency.set('500Hz')
popupMenu = tk.OptionMenu(root, frequency, *frequency_options)
popupMenu.place(relx=0.1, rely=0.5)

upload = tk.Button(root, text="Analyze", font=header_font, padx=10, pady=5,
                     fg='white', bg="CadetBlue4", command=upload_excell)
upload.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
'''
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5,
                     fg='white', bg="#263042", command=runApps)
runApps.pack()
'''
root.mainloop()