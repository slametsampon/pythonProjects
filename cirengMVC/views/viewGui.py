import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    PAD = 10

    def __init__(self, app):
        super().__init__()

        self.title('cirengGUI1.0')
        self.app = app

        self.entInput = tk.StringVar()
        self.entHargaJual = tk.StringVar()
        self.radioInput = tk.IntVar()

        self.__buatFrameUtama() #call local funtion/methode
        self.__buatFrameDua() #call local funtion/methode

    #global function/methode
    def main(self):
        self.__displayHasil(0,0) #call local funtion/methode
        self.__displayInput(0,0) #call local funtion/methode
        self.__displayUntungRugi(0,1) #call local funtion/methode
        self.mainloop()

    #private function/methode
    def __buatFrameUtama(self):
        self.frmUtama = ttk.Frame(self)
        self.frmUtama.grid(row = 0, column = 0, padx=self.PAD, pady=self.PAD)

    #private function/methode
    def __buatFrameDua(self):
        self.frmDua = ttk.Frame(self)
        self.frmDua.grid(row = 1, column = 0)

    #private function/methode
    def __displayHasil(self,rw,cl):
        colUang = [5,9,10,11]
        colFloat = [6]
        frmHasil = tk.LabelFrame(self.frmUtama, text='Menu Cireng Special')
        data2D = self.app.bahan.bacaSemuaBahan()
        header = True
        i = 0
        for layerSatu in data2D:
            col = 0
            if header:
                header = False
                colHeader = 0
                keysLayerDua = data2D[layerSatu].keys()
                ttk.Label(frmHasil,text = f'No.').grid(row=i,column=colHeader, sticky=(tk.W ),padx=self.PAD)
                for key in keysLayerDua:
                    colHeader += 1
                    ttk.Label(frmHasil,text = f'{key}').grid(row=i,column=colHeader, sticky=(tk.W ),padx=self.PAD)
                i += 1
            ttk.Label(frmHasil,text = f'{i}').grid(row=i,column=col, sticky=(tk.W ),padx=self.PAD)
            col += 1
            for layerDua in data2D[layerSatu]:
                if col in colUang:
                    ttk.Label(frmHasil,text = f'{data2D[layerSatu][layerDua]:,d}').grid(row=i,column=col, sticky=(tk.W ),padx=self.PAD)
                elif col in colFloat:
                    ttk.Label(frmHasil,text = f'{data2D[layerSatu][layerDua]:.3f}').grid(row=i,column=col, sticky=(tk.W ),padx=self.PAD)
                else:
                    ttk.Label(frmHasil,text = f'{data2D[layerSatu][layerDua]}').grid(row=i,column=col, sticky=(tk.W ),padx=self.PAD)
                col += 1
            i += 1
        #display total
        ttk.Label(frmHasil,text = f'Total').grid(row=i,column=4, sticky=(tk.W ),padx=self.PAD)
        ttk.Label(frmHasil,text = f'{int(self.app.bahan.bacaNilaiBahan("CJ","biayaUnit")):,d}').grid(row=i,column=5, sticky=(tk.W ),padx=self.PAD)
        ttk.Label(frmHasil,text = f'{int(self.app.bahan.bacaNilaiBahan("CJ","Biaya")):,d}').grid(row=i,column=8, sticky=(tk.W ),padx=self.PAD)

        frmHasil.grid(row=rw, column=cl, sticky=(tk.W + tk.E),padx=self.PAD)

    #private function/methode
    def __hitungCireng(self):

        self.app.onClickHitung(self.radioInput.get(),int(self.entInput.get()),int(self.entHargaJual.get()))
        self.__displayHasil(0,0)
        self.__displayUntungRugi(0,1)
        
    def __displayInput(self,rw,cl):
        frmInput = tk.LabelFrame(self.frmDua, text="Input Parameter")

        ttk.Radiobutton(frmInput, text="Cireng (biji)", variable=self.radioInput, value=1).grid(row=0,column=0, sticky=(tk.W ),padx=10)
        ttk.Radiobutton(frmInput, text="Bahan Baku (gram)", variable=self.radioInput, value=2).grid(row=1,column=0, sticky=(tk.W ),padx=10)

        ttk.Label(frmInput,text = 'Masukkan Angka : ').grid(row=0,column=1, sticky=(tk.W),padx=10)
        ttk.Entry(frmInput, textvariable=self.entInput,width=10).grid(row=1,column=1, sticky=(tk.W),padx=10)

        ttk.Label(frmInput, text="Biaya per kemasan :").grid(row=0,column=2, sticky=(tk.W ),padx=10)
        ttk.Label(frmInput, text=f'{int(self.app.kemasan.bacaNilaiKemasan("biayaTotal")):,d}').grid(row=0,column=3, sticky=(tk.W ),padx=10)

        ttk.Label(frmInput, text="Harga Jual per kemasan").grid(row=1,column=2, sticky=(tk.W ),padx=10)
        ttk.Entry(frmInput, textvariable=self.entHargaJual,width=10).grid(row=1,column=3, sticky=(tk.W),padx=10)

        ttk.Button(
            frmInput,text = 'Hitung',
            command=self.__hitungCireng
            #command=(lambda selVal=self.radioInput.get(),val=self.entInput.get():self.app.onClickHitung(selVal,val))
            ).grid(row=2,column=2,columnspan = 2, sticky=(tk.W),padx=10)
        '''
        ttk.Button(
            frmInput,text = 'Hitung',
            command=(lambda selVal=self.radioInput.get(),val=int(self.entInput.get()):self.app.onClickHitung(selVal,val))
            ).grid(row=2,column=2,columnspan = 2, sticky=(tk.W),padx=10)
        '''
        frmInput.grid(row=rw, column=cl, sticky=(tk.W + tk.E), padx=self.PAD, pady=self.PAD)

    def __displayUntungRugi(self,rw,cl):
        jumlahCireng = f'{self.app.hitung.getJumlahCireng()}'
        jumlahKemasan = f'{self.app.hasil.bacaNilaiHasil("jumlahKemasan")}'
        sisaCireng = f'{self.app.hasil.bacaNilaiHasil("sisaCireng")}'
        hargaJualTotal = f'Rp.{int(self.app.hasil.bacaNilaiHasil("hargaJualTotal")):,d}'
        biayaTotal = f'Rp.{int(self.app.hasil.bacaNilaiHasil("biayaTotal")):,d}'
        untungRugi = f'Rp.{abs(int(self.app.hasil.bacaNilaiHasil("untungRugi"))):,d}'

        frmUntungRugi = tk.LabelFrame(self.frmDua, text="Untung Rugi")

        ttk.Label(frmUntungRugi, text="Jumlah Cireng :").grid(row=0,column=4, sticky=(tk.W ),padx=10)
        ttk.Label(frmUntungRugi, text=jumlahCireng).grid(row=0,column=5, sticky=(tk.W ),padx=10)

        ttk.Label(frmUntungRugi, text="Jumlah Kemasan :").grid(row=1,column=4, sticky=(tk.W ),padx=10)
        ttk.Label(frmUntungRugi, text=jumlahKemasan).grid(row=1,column=5, sticky=(tk.W ),padx=10)

        ttk.Label(frmUntungRugi, text="Sisa Cireng (biji) :").grid(row=2,column=4, sticky=(tk.W ),padx=10)
        ttk.Label(frmUntungRugi, text=sisaCireng).grid(row=2,column=5, sticky=(tk.W ),padx=10)

        ttk.Label(frmUntungRugi, text="Harga Jual :").grid(row=0,column=6, sticky=(tk.W ),padx=10)
        ttk.Label(frmUntungRugi, text=hargaJualTotal).grid(row=0,column=7, sticky=(tk.W ),padx=10)

        ttk.Label(frmUntungRugi, text="Total Biaya :").grid(row=1,column=6, sticky=(tk.W ),padx=10)
        ttk.Label(frmUntungRugi, text=biayaTotal).grid(row=1,column=7, sticky=(tk.W ),padx=10)

        ttk.Label(frmUntungRugi, text="Rugi :").grid(row=2,column=6, sticky=(tk.W ),padx=10)
        if self.app.hasil.bacaNilaiHasil("untungRugi") > 0:
            ttk.Label(frmUntungRugi, text="Untung :").grid(row=2,column=6, sticky=(tk.W ),padx=10)

        ttk.Label(frmUntungRugi, text=untungRugi).grid(row=2,column=7, sticky=(tk.W ),padx=10)
        frmUntungRugi.grid(row=rw, column=cl, sticky=(tk.W + tk.E), padx=self.PAD, pady=self.PAD)

