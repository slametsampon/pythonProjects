import tkinter as tk
from tkinter import ttk, messagebox


class View(tk.Tk):
    
    PAD = 10
    MAX_BUTTON_ROW = 4

    buttonCaptions =[
        'C','+/-','%','/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]

    def __init__(self,controller):

        super().__init__()
        self.title('Izan Calculator 1.0')

        self.valueVar = tk.StringVar()

        self.config(bg = 'black')
        self._configureButtonStyle()

        self.controller = controller
        self._buatFrameUtama()
        self._buatLabel()
        self._buatButton()
        self._buatMenu()
        self._centerWindow()

    def _configureButtonStyle(self):
        style = ttk.Style()
        style.theme_use('alt')

        #style for number buttons
        style.configure(
            'N.TButton', background='orenge'
        )

        #style for operator buttons
        style.configure(
            'O.TButton', foreground='white', background='orenge'
        )

        #style for miscellaneous buttons
        style.configure(
            'M.TButton', background='orenge'
        )

    def main(self):
        self.mainloop()

    def _buatFrameUtama(self):
        self.frmUtama = ttk.Frame(self)
        self.frmUtama.pack(padx = self.PAD, pady = self.PAD)

    def _buatLabel(self):
        lbl = tk.Label(
            self.frmUtama,
            textvariable = self.valueVar,
            anchor = 'e',
            bg='black', fg='white', font=('Arial',30)
            )
        lbl.pack(fill = 'x')

    def _buatButton(self):
        outerFrm = ttk.Frame(self.frmUtama)
        outerFrm.pack()
        isFirstRow = True
        buttonInRow = 0
        for cap in self.buttonCaptions:
            if isFirstRow or buttonInRow == self.MAX_BUTTON_ROW:
                isFirstRow = False
                frm = ttk.Frame(outerFrm)
                frm.pack(fill = 'x')
                buttonInRow = 0
            
            if isinstance(cap,int):
                stylePrefix = 'N'
            elif self._isOperator(cap):
                stylePrefix = 'O'
            else:
                stylePrefix = 'M'
            styleName = f'{stylePrefix}.TButton'
            #print(f'{cap} => {styleName}')

            btn = ttk.Button(
                frm,
                text = cap,
                #style=styleName,
                command = (
                    lambda button=cap: self.controller.onButtonClick(button)
                    ))
            if cap == 0:
                fill = 'x'
                expand = 1
            else:
                fill = 'none'
                expand = 0

            btn.pack(fill = fill, expand = expand, side='left')
            buttonInRow += 1

    def _buatMenu(self):
        menu = tk.Menu(self.frmUtama)
        self.config(menu=menu)

        # create the file object)
        file = tk.Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self._exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)


        # create the file object)
        help = tk.Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is _onInfo
        help.add_command(label="Info",command=self._onInfo)

        #added "file" to our menu
        menu.add_cascade(label="Help", menu=help)

    def _exit(self):
        exit()

    def _onInfo(self):
       messagebox.showinfo("Information", "It is build by Izan")

    
    def _isOperator(self,buttonCap):
        return buttonCap in ['/', '*', '-', '+', '=']

    def _centerWindow(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth()-width)//2
        y_offset = (self.winfo_screenheight()-height)//2

        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
        )