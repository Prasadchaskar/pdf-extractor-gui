import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import PyPDF2

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instr = tk.Label(root, text="Select a PDF file from your computer", font='Raleway')
instr.grid(columnspan=3, column=0, row=1)

# browse button
browse_txt = tk.StringVar()
browse_btn = tk.Button( root, 
                        command=lambda:open_file(),
                        textvariable=browse_txt, 
                        font='Raleway', 
                        bg="#20bebe", 
                        fg="white", 
                        height=2, 
                        width=15)
browse_txt.set("Upload")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)


def open_file():
    browse_txt.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("PDF file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        page_content = page.extract_text()
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("ceneter", 1.0, "end")
        text_box.grid(column=1, row=3)
    browse_txt.set("Upload")

root.mainloop()