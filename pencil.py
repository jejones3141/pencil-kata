class Pencil:
    def __init__(self, length, pointDurability, eraserDurability):
        self.length = length
        self.initPointDurability = self.pointDurability = pointDurability
        self.eraserDurability = eraserDurability
        self.text = ''
        self.erasedPos = None
    
    def _writeChar(self, c):
        wear = 0 if c.isspace() else 2 if c.isupper() else 1
        c = ' ' if self.pointDurability < wear else c
        self.pointDurability = max(self.pointDurability - wear, 0)
        return c
    
    def _insert(self, prefixLen, text, suffixPos):
        self.text = self.text[:prefixLen] + text + self.text[suffixPos:]

    def write(self, text):
        for c in text:
            self.text += self._writeChar(c)
            
    def sharpen(self):
        if self.length > 0:
            self.pointDurability = self.initPointDurability
            self.length -= 1
            
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
        self.erasedPos = suffixPos - numErased
        self._insert(self.erasedPos, numErased * ' ', suffixPos)

    def overwrite(self, text):
        if self.erasedPos is not None:
            replacement = ''
            selfTextPos = self.erasedPos
            for c in text:
                rc = c if self.text[selfTextPos].isspace() else '@'
                replacement += self._writeChar(rc)
                selfTextPos += 1
            suffixPos = self.erasedPos + len(text)
            self._insert(self.erasedPos, replacement, suffixPos)

    def getText(self):
        return self.text
