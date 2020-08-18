class Model:

    def __init__(self):
        self.value = ''
        self.operator = ''
        self.previousValue = ''

    def calculate(self,caption):
        if caption == 'C':
            self.value = ''
            self.previousValue = ''
            self.operator = ''

        elif isinstance(caption, int):
            self.value += str(caption)

        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value

        elif caption == '.':
            if not caption in self.value:
                self.value += caption

        elif caption == '=':
            value = self._evaluate()

            if '.0' in str(value):
                value = int(value)

            self.value = str(value)
        
        elif caption == '%':
            value = float(self.value) if '.' in self.value else int(self.value)
            self.value = str(value/100)

        else:
            if self.value:
                self.operator = caption
                self.previousValue = self.value
                self.value = ''


        return self.value

    def _evaluate(self):
        return eval(self.previousValue+self.operator+self.value)

    