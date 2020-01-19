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

    def test_erasersWearOut(self):
        p = Pencil(length = 40, pointDurability = 1000, eraserDurability = 2)
        p.write("last on last night's schedule was immigration law")
        p.erase("la")
        self.assertTrue(p.getText() == "last on last night's schedule was immigration   w")
        p.erase("la")
        self.assertTrue(p.getText() == "last on last night's schedule was immigration   w")
        
    def test_textIsErasedFromTheRight(self):
        p = Pencil(length = 40, pointDurability = 1000, eraserDurability = 5)
        p.write("a Kafkaesque bureaucracy")
        p.erase("Kafkaesque")
        self.assertTrue(p.getText() == "a Kafka      bureaucracy")
        
    def test_whitespaceDoesntDepleteErasers(self):
        p = Pencil(length = 40, pointDurability = 1000, eraserDurability = 5)
        p.write("last on last night's schedule was immigration law")
        p.erase(" was ")
        self.assertTrue(p.getText() == "last on last night's schedule     immigration law")
        p.erase("la")
        self.assertTrue(p.getText() == "last on last night's schedule     immigration   w")
        
    def test_editingOverwritesErasedText(self):
        p = Pencil(length = 40, pointDurability = 1000, eraserDurability = 200)
        p.write("An apple a day keeps the doctor away")
        p.erase("apple")
        p.overwrite("onion")
        self.assertTrue(p.getText() == "An onion a day keeps the doctor away")
    
    def test_editingMarksCollisionsWithNonSpaceWithAt(self):
        p = Pencil(length = 40, pointDurability = 1000, eraserDurability = 200)
        p.write("An apple a day keeps the doctor away")
        p.erase("apple")
        p.overwrite("artichoke")
        self.assertTrue(p.getText() == "An artich@k@ay keeps the doctor away")


if __name__ == '__main__':
    unittest.main()
