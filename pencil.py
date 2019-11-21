class Pencil:
    def __init__(self, length, pointDurability, eraserDurability):
        self.length = length
        self.initPointDurability = self.pointDurability = pointDurability
        self.eraserDurability = eraserDurability
        self.text = ''

    def write(self, text):
        for c in text:
            wear = 0 if c.isspace() else 2 if c.isupper() else 1
            self.text += ' ' if self.pointDurability < wear else c
            self.pointDurability = max(self.pointDurability - wear, 0)
            
    def sharpen(self):
        if self.length > 0:
            self.pointDurability = self.initPointDurability
            self.length -= 1
            
    def _eraseWear(c):
        return 
            
    def erase(self, text):
        tPos = self.text.rfind(text)
        if tPos == -1:
            return
        numErased = 0
        for c in reversed(text):
            if self.eraserDurability <= 0:
                break
            numErased += 1
            self.eraserDurability -= 0 if c.isspace() else 1
        suffixPos = tPos + len(text)
        self.text = (self.text[:suffixPos - numErased] + (numErased * ' ') +
                     self.text[suffixPos:])

    def getText(self):
        return self.text
