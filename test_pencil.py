import unittest
from pencil import Pencil

class TestPencil(unittest.TestCase):

    def test_aPencilWithSufficientlyDurablePointCanWrite(self):
        p = Pencil(length = 40, pointDurability = 1000, eraserDurability = 200)
        text = "Four score and seven years ago"
        p.write(text)
        self.assertTrue(p.getText() == text)

    def test_aPencilWritesBlanksAfterPointLosesDurability(self):
        p = Pencil(length = 40, pointDurability = 4, eraserDurability = 200)
        p.write("ambidextrous")
        self.assertTrue(p.getText() == "ambi        ")
        
    def test_aSharpenedPencilCanWriteAgain(self):
       p = Pencil(length = 40, pointDurability = 4, eraserDurability = 200)
       p.write("ambi")
       p.sharpen()
       p.write("dextrous")
       self.assertTrue(p.getText() == "ambidext    ")
       
    def test_erasingTextReplacesItsLastOccurrenceWithSpaces(self):
        p = Pencil(length = 40, pointDurability = 1000, eraserDurability = 200)
        p.write("last on last night's schedule was immigration law")
        p.erase("la")
        self.assertTrue(p.getText() == "last on last night's schedule was immigration   w")
        p.erase("la")
        self.assertTrue(p.getText() == "last on   st night's schedule was immigration   w")

if __name__ == '__main__':
    unittest.main()
