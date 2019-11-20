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

if __name__ == '__main__':
    unittest.main()
