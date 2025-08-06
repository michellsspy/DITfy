import unittest
from src.converter import markdown_to_docx

class TestConversion(unittest.TestCase):
    def test_basic_conversion(self):
        result = markdown_to_docx("# Test", "output.docx")
        self.assertTrue(result)