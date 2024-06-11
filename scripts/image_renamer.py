import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import sys
import winreg
import ctypes

# Colors
GREEN_COLOR = "\033[92m" 
RED_COLOR = "\033[91m"
RESET_COLOR = "\033[0m"

# Name
IMG_PROMPT = "You are a file renamer. Suggest a short new title for the image only. Don't respond with anything else."
REG_FILE = "add_context_menu.reg"
GEMINI_MODEL = "gemini-1.5-flash"
APP_NAME = "Vision-Label"
REG_PATH = "HKEY_CLASSES_ROOT\SystemFileAssociations\image\shell"
IMAGE_EXTENSION = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

class ImageRenamer:
    def __init__(self):
        # TODO : use OPENAI_API_KEY
        load_dotenv()
        self.api_key = os.getenv('GOOGLE_API_KEY')
        self.img_prompt = IMG_PROMPT
        self.reg_file = REG_FILE
        self.model = genai.GenerativeModel(GEMINI_MODEL)
        self.app_name = APP_NAME
        self.reg_path = REG_PATH
        self.image_extension = IMAGE_EXTENSION

        if not self.api_key:
            raise ValueError("Google API key not found in environment variables.")
        
        genai.configure(api_key=self.api_key)
    
    def print_success_message(self, content):
        print(f"{GREEN_COLOR}{content}{RESET_COLOR}")
    
    def print_error_message(self, content):
        print(f"{RED_COLOR}{content}{RESET_COLOR}")

    def generate_content(self, prompt):
        return self.model.generate_content(prompt)

    def generate_image_name(self, image_path, prompt):
        img = Image.open(image_path)
        response = self.model.generate_content([prompt, img])
        return response.text.strip()

    def rename_image(self, file_path, title="TODO", subject="TODO", tags="TODO"):
        new_name = self.generate_image_name(file_path, self.img_prompt)
        if new_name:
            new_file_path = os.path.join(os.path.dirname(file_path), f"{new_name}{os.path.splitext(file_path)[1]}")
            try:
                os.rename(file_path, new_file_path)
                self.print_success_message(f"Renamed to: {new_file_path}")
                # TODO update metadata function
                # self.update_image_metadata(new_file_path, title, subject, tags)
            except Exception as e:
                print(f"Error renaming file: {e}")
    
    def generate_reg_file(self, python_exe_path, main_py_path, current_script_path):
        reg_content = f"""Windows Registry Editor Version 5.00

[{self.reg_path}\{self.app_name}]
@="Rename with {self.app_name}"
"Icon"="{current_script_path}\\\img\\\icon.ico"

[{self.reg_path}\{self.app_name}\\command]
@="cmd /c start \\"\\" \\"{python_exe_path}\\" \\"{main_py_path}\\" --path \\"%1\\""
        """

        with open(self.reg_file, "w") as reg_file:
            reg_file.write(reg_content)

        print(f"reg path: {self.reg_path}\{self.app_name}")
        print(f"Please initialize the {self.reg_file}")
        self.print_success_message(f"Registry file generated successfully.")
    
    def remove_registry_entry(self):
        if not ctypes.windll.shell32.IsUserAnAdmin():
            self.print_error_message("Please run this script as administrator!")
            sys.exit(1)
        try:
            key_path = rf"SystemFileAssociations\image\shell\{self.app_name}"
            command_key_path = key_path + r"\command"
            
            # Delete the command key first
            try:
                with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, command_key_path, 0, winreg.KEY_WRITE) as key:
                    winreg.DeleteKey(key, "")
                    self.print_success_message("Command registry entry removed successfully.")
            except FileNotFoundError:
                self.print_error_message("Command registry entry does not exist.")
            
            # Delete the main key
            try:
                with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_path, 0, winreg.KEY_WRITE) as key:
                    winreg.DeleteKey(key, "")
                    self.print_success_message("Registry entry removed successfully.")
            except FileNotFoundError:
                self.print_error_message("Registry entry does not exist.")
        except Exception as e:
            self.print_error_message(f"Error removing registry entry: {e}")
    
    def rename_images_in_directory(self, directory_path):
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.lower().endswith(self.image_extension):
                    file_path = os.path.join(root, file)
                    self.rename_image(file_path)
    