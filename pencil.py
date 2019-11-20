class Pencil:
    def __init__(self, length, pointDurability, eraserDurability):
        self.length = length
        self.initPointDurability = self.pointDurability = pointDurability
        self.eraserDurability = eraserDurability
        self.text = ''

    def write(self, text):
        for c in text:
            w = 0 if c.isspace() else 2 if c.isupper() else 1
            self.text += ' ' if self.pointDurability < w else c
            self.pointDurability = max(self.pointDurability - w, 0)
            
    def sharpen(self):
        if self.length > 0:
            self.pointDurability = self.initPointDurability
            self.length -= 1
            
    def erase(self, text):
        tPos = self.text.rfind(text)
        if tPos != -1:
            tLen = min(len(text), self.eraserDurability)
            if tLen > 0:
                self.text = f'{self.text[0:tPos]}{" ":{tLen}}{self.text[tPos + tLen:]}'
                self.eraserDurability -= tLen

    def getText(self):
        return self.text
