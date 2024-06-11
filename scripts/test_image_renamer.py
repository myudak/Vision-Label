import unittest
from unittest.mock import patch, MagicMock
import os
from dotenv import load_dotenv
from image_renamer import ImageRenamer
import sys


IMG_PROMPT = "You are a file renamer. Suggest a short new title for the image only. Don't respond with anything else."
load_dotenv()
class TestImageRenamer(unittest.TestCase):

    def setUp(self):
        # Set up environment variables for testing
        os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
        self.renamer = ImageRenamer()

    @patch('image_renamer.genai.GenerativeModel')
    def test_generate_image_name(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "Chicken Broccoli Rice Bowls.jpg"
        
        image_path = '../img/example2.webp'
        generated_name = self.renamer.generate_image_name(image_path, IMG_PROMPT)
        
        self.assertIsNotNone(generated_name.strip())
        print("OK", generated_name)

    @patch('image_renamer.genai.GenerativeModel')
    @patch('image_renamer.os.rename')
    def test_rename_image(self, mock_rename, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "Black.jpgs.jpg"
        
        image_path = '../img/example2.webp'
        new_image_path = os.path.join(os.path.dirname(image_path), "Black.jpgs.jpg")
        
        self.renamer.rename_image(image_path)
        
        self.assertIsNotNone(image_path)
        print("OK", image_path)

    # @patch('image_renamer.ImageRenamer.generate_reg_file')
    def test_generate_reg_file(self):
        python_exe_path = sys.executable.replace("\\", "\\\\")  
        main_py_path = os.path.abspath(__file__).replace("\\", "\\\\")
        current_script_path = os.path.dirname(os.path.abspath(__file__)).replace("\\", "\\\\")
        
        self.renamer.generate_reg_file(python_exe_path, main_py_path,current_script_path)
        
        reg_file_path = 'add_context_menu.reg'
        self.assertTrue(os.path.exists(reg_file_path))

if __name__ == '__main__':
    unittest.main()
