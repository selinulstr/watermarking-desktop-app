from tkinter import *
from PIL import Image, ImageDraw, ImageFont
from tkinter.filedialog import askopenfilename
from tkinter import messagebox


root = Tk()
root.title("Watermarking App")
root.configure(background="#474E68")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
img_file = ""


def open_file():
    global img_file
    img_file = askopenfilename()


def watermark(img_input, img_output, text_watermark, xy_pos):
    image = Image.open(img_input)
    watermark_image = image.copy()
    draw = ImageDraw.Draw(watermark_image)
    font = ImageFont.truetype("arial.ttf", 60)
    draw.text(xy_pos, text_watermark, font=font, fill=(255, 255, 255))
    watermark_image.show()
    watermark_image.save(img_output)


def watermark_img():
    if img_file == "":
        messagebox.showerror("No image found", "Please select an image first.")
    else:
        img_output = f"watermarked.jpg"
        text_watermark = text_entry.get()
        watermark(img_file, img_output, text_watermark=text_watermark, xy_pos=(100, 100))
        messagebox.showinfo("Complete", "Successfully watermarked!")


title_label = Label(text="IMG Watermark", font=("Courier", 50, "bold"), fg="white", bg="#474E68")
title_label.grid(column=0, row=0, columnspan=2, padx=50, pady=50)
b1 = Button(text="Choose Image", font=20, width=15, command=open_file, bg="#404258", foreground="white")
b1.grid(column=0, row=1, columnspan=2)
text_label = Label(text="Watermark Text", font=("Courier", 14), bg="#474E68", foreground="white")
text_label.grid(column=0, row=2, columnspan=2, padx=25, pady=25)
text_entry = Entry(width=26, bg="white", fg="#404258")
text_entry.grid(column=0, row=3)
b2 = Button(text="Watermark IMG", font=20, width=15,
            command=watermark_img, bg="#404258", foreground="white")
b2.grid(column=0, row=4, columnspan=2, padx=25, pady=30)


root.mainloop()