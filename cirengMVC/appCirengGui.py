"""
It is __main entry
"""
from models.model import Bahan, Kemasan, Hasil
from views.viewGui import View
from controllers.calculations import Calculations

header="""Menu Cireng Salju - Special
    by:fairuz"""

class AppCirengGui:
    def __init__(self):

        #deklarasi variable
        self.bahan = Bahan()
        self.kemasan = Kemasan()
        self.hasil = Hasil()
        self.hitung = Calculations(self)

        self.view = View(self)

    #global function/methode
    def main(self):
        #nitialisasi
        self.__initBahan()
        self.hitung.hitungHargaUnit()

        self.view.main()

    def onClickHitung(self,selVal,val,harga):
        if selVal == 1:
            self.hitung.setJumlahCireng(val)
        elif selVal == 2:
            self.app.hitung.setJumlahCireng(int((val * self.bahan.bacaNilaiBahan("CJ","QtyMenu")) / self.bahan.bacaNilaiBahan("TT","QtyMenu")))
        self.hitung.setHargaJual(harga)
        self.hitungCireng()
    
    #global function/methode
    def hitungCireng(self):
        self.hitung.hitungBiaya()
        self.hitung.hitungUtungRugi()

    #private function/methode
    def __initBahan(self):
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
    cirengGUI = AppCirengGui()
    cirengGUI.main() #call global function/methode
