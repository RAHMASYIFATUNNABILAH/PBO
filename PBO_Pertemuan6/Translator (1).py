from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("700x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Masukkan teks:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Hasil Terjemahan:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        
        # pasang textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, width=50) 
        self.txtHasil.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate to englihs',
            command=lambda: self.onTranslate('en'))
        self.btnTranslate.grid(row=1, column=0, padx=5, pady=5) 

        self.btnTranslate = Button(mainFrame, text='Translate to japanese',
            command=lambda: self.onTranslate('ja'))
        self.btnTranslate.grid(row=1, column=1, padx=5, pady=5) 
        
        self.btnTranslate = Button(mainFrame, text='Translate to arabic',
            command=lambda: self.onTranslate('ar'))
        self.btnTranslate.grid(row=1, column=2, padx=5, pady=5) 

        self.btnTranslate = Button(mainFrame, text='Translate to turkish',
            command=lambda: self.onTranslate('tr'))
        self.btnTranslate.grid(row=1, column=3, padx=5, pady=5) 

        
    def onTranslate(self, dest_lang):
        # membuat instance object
        penterjemah = Translator()

        # menterjemahkan
        hasil = penterjemah.translate(self.txtSumber.get(), dest=dest_lang) 
       
       #mEnghapus isi texTboX hasil sebelumnya
        self.txtHasil.delete(0, END)

        # menampilkan hasil terjemahan
        self.txtHasil.insert(END,hasil.text)

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop() 