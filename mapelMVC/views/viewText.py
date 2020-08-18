# import only system from os 
from os import system, name 

class View:

    def __init__(self,app):
        self.app = app

    # define our clear screen function 
    def clearScreen(self): 
    
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
    
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 

    def viewTabelMapel(self,tblMapel):
        hari = True
        i = 0
        for mplList in tblMapel:
            if hari:
                mplText = 'Hari'
                hari = False
            else:
                i += 1
                key = self.app.mapel.KEY 
                mplText = f'{key}{i}'
            for mpl in mplList:
                mplText += f'\t{mpl}'
            print(f'{mplText}')

    def viewSekolah(self,dataSekolah):
        print('\n\n')
        for data in dataSekolah:
            print(f'\t\t{dataSekolah[data]}')
        print('\n\t\t<<JADUAL MATA PELAJARAN>>')

    def viewInputMenu(self,menu):
        print('\n')
        for mn in menu:
            print(f'\t{mn}')
        jawaban = input('Pilih Menu : ')
        return jawaban
