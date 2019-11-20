class Pencil:
    def __init__(self, length, pointDurability, eraserDurability):
        self.text = ''

    def write(self, text):
        self.text += text

    def getText(self):
        return self.text
