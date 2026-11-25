from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'src'))
from review import fingerprint

class DraftTest(unittest.TestCase):
    def test_whitespace_reuse(self):
        self.assertEqual(fingerprint('Seed Soil'),fingerprint('Seed  Soil\n'))
    def test_a_change_is_detectable(self):
        self.assertNotEqual(fingerprint('Seed Soil'),fingerprint('Seed Roots'))
    def test_empty_is_rejected(self):
        with self.assertRaises(ValueError):
            fingerprint('   ')
