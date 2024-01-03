from tkinter import Tk, Label, Button, Text, filedialog
from PIL import Image, ImageTk
from pytesseract import pytesseract

class TextExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Extractor")
        self.root.configure(bg='light green')

        self.text_area = Text(root, wrap="word", height=10, width=40)
        self.text_area.grid(row=0, column=0, padx=10, pady=10)

        browse_button = Button(root, text="Masukan Gambar", command=self.browse_image)
        browse_button.grid(row=0, column=1, padx=10, pady=10)

        extract_button = Button(root, text="Convert Text", command=self.extract_text, bg='white')
        extract_button.grid(row=1, column=1, padx=10, pady=10)

        self.label_name = Label(root, text="RAHMA SYIFATUN NABILAH", bg='white')
        self.label_name.grid(row=1, column=0, columnspan=2)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        self.image_path = file_path
        self.display_image()

    def display_image(self):
        if hasattr(self, 'image_path'):
            img = Image.open(self.image_path)
            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(img)
            panel = Label(self.root, image=img)
            panel.image = img
            panel.grid(row=2, column=0, columnspan=2)

    def extract_text(self):
        if hasattr(self, 'image_path'):
            pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            img = Image.open(self.image_path)
            text = pytesseract.image_to_string(img)
            self.text_area.delete(1.0, 'end-1c')  # Clear existing text
            self.text_area.insert('end', text)

if __name__ == '__main__':
    root = Tk()
    app = TextExtractorApp(root)
    root.mainloop()
