class Pencil:
    def __init__(self, length, pointDurability, eraserDurability):
        self.pointDurability = pointDurability
        self.text = ''

    def write(self, text):
        for c in text:
            w = 0 if c.isspace() else 2 if c.isupper() else 1
            self.text += ' ' if self.pointDurability < w else c
            self.pointDurability = max(self.pointDurability - w, 0)

    def getText(self):
        return self.text
