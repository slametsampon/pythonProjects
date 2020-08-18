class Controller:
    def __init__(self,app):
        self.app = app
        self.__tabelMapel = []

    def buatTabelMapel(self,dafMpl):
        maxMapel = self.app.mapel.bacaMaxMapel()
        key = self.app.mapel.KEY
        self.__tabelMapel.append(list(dafMpl.keys()))

        i = 0
        tblMpl = []
        for i in range(1, maxMapel+1):            
            for hari in dafMpl:
                hariMapel = len(dafMpl[hari])
                if i <= hariMapel:
                    tblMpl.append(dafMpl[hari][f'{key}{i}'])
                else:
                    tblMpl.append('')
            
            tblTemp = tblMpl.copy()
            self.__tabelMapel.append(tblTemp)
            tblMpl.clear()

        return(self.__tabelMapel)

