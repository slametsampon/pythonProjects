"""
It is main entry
"""
from models.mapel import Mapel, Sekolah, Menu
from views.viewText import View
from controllers.controller import Controller

class AppMapelText:
    def __init__(self):

        #deklarasi variable
        self.mapel = Mapel()
        self.sekolah = Sekolah()
        self.menu = Menu()
        self.view = View(self)
        self.controller = Controller(self)

    def main(self):
        #nitialisasi
        self.initAppMapel()

        jawabanKeluar = 'N'
        while jawabanKeluar !='Q':
            #Tulis program di sini

            self.view.viewSekolah(self.sekolah.bacaDataSekolah())
            self.view.viewTabelMapel(self.mapel.bacaTabelMapel())

            jawabanKeluar = self.view.viewInputMenu(self.menu.bacaMenu())

            #Batas program
        #Finished 
        print('\nThankyou for use my program, see you later\n')
    
    def initAppMapel(self):
        self.sekolah.buatDataSekolah(
            'SMA Negri Satu Genteng',
            'Genteng - Banyuwangi',
            'MIPA 4'
        )

        self.menu.buatMapel(
            '1. Buat Jadual',
            '2. Ubah Jadual',
            '3. Lihat Jadual',
            '4. Buat Data Sekolah',
            'Q. Keluar'
        )
        self.mapel.buatMapel('Ahad','libur')
        self.mapel.buatMapel('Senin','Upacara','Lit','Biologi','IPA','Bader','PJOK')
        self.mapel.buatMapel('Selasa','Ngaji','BIN','Biologi','IPA','MTK')
        self.mapel.buatMapel('Rabo','Ngaji','IPS','Bader','Seni','Bimbel')
        self.mapel.buatMapel('Kamis','Ngaji','MTK','Pra','PAI','BIN')
        self.mapel.buatMapel("Jum'at",'Ngaji','PKN','IPS','Sholat','Bimbel')
        self.mapel.buatMapel('Sabtu','libur')

if __name__ == '__main__':
    appMapelText = AppMapelText()
    appMapelText.main()
