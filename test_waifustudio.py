# test_waifustudio.py
"""
Tests for WaifuStudio module.
"""

import unittest
from waifustudio import WaifuStudio

class TestWaifuStudio(unittest.TestCase):
    """Test cases for WaifuStudio class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WaifuStudio()
        self.assertIsInstance(instance, WaifuStudio)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WaifuStudio()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
