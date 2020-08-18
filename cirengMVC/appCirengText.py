"""
It is main entry
"""
from models.model import Bahan, Kemasan, Hasil
from views.viewText import View
from controllers.calculations import Calculations

header="""Menu Cireng Salju - Special
    by:fairuz"""

class AppCirengMvc:
    def __init__(self):

        #deklarasi variable
        self.bahan = Bahan()
        self.kemasan = Kemasan()
        self.hasil = Hasil()
        self.hitung = Calculations(self)
        self.view = View(self)
        self.jumlahCireng = 0
        self.hargaJual = 0

    def main(self):
        #nitialisasi
        self.initBahan()
        self.hitung.hitungHargaUnit()
        jawabanKeluar = 'N'
        while jawabanKeluar !='Y' :
            #Tulis program di sini
            print(header)

            self.view.viewInputCireng()

            self.hitung.hitungBiaya()
            self.hitung.hitungUtungRugi()
            self.view.viewHasil()
            #Batas program
            jawabanKeluar = input('\nwant to quit Y/N?: ') 

        #Finished 
        print('\nThankyou for use my program, see you later\n')
    
    def initBahan(self):
        #buatBahan(self,nama,desc,satuan,harga,faktorHarga)
        self.bahan.buatBahan('CJ','Cireng Jadi','biji',13,0,0)
        self.bahan.buatBahan('TT','Tepung Tapioka','gram',200,7000,1000)
        self.bahan.buatBahan('BP','Bawang Putih','siung',4,8000,80)
        self.bahan.buatBahan('DB','Daun Bawang','bt',2,7000,70)
        self.bahan.buatBahan('PA','Penyedap Rasa','sdt',1,500,2)
        self.bahan.buatBahan('AM','Air Mineral','ml',180,19000,19000)
        self.bahan.buatBahan('Gr','Garam Halus','cukup',0,8000,1000)
        self.bahan.buatBahan('Mr','Merica','cukup',0,8000,1000)
        self.bahan.buatBahan('GP','Gula Putih','cukup',0,8000,1000)

if __name__ == '__main__':
    cirengMVC = AppCirengMvc()
    cirengMVC.main()
