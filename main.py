import os
import argparse
import sys
from scripts.image_renamer import ImageRenamer

def main():
    parser = argparse.ArgumentParser(description="Rename an image file based on a generated name.")
    parser.add_argument("-d", "--directory", type=str, help="Path to the directory containing images to rename.")
    parser.add_argument("-f","--file",  nargs='+', help="Path to the image file to rename.")
    parser.add_argument("-rg","--reg", action="store_true", help="Generate the registry file.")
    parser.add_argument("-rm","--remove", action="store_true", help="Remove the registry entry.")

    args = parser.parse_args()
    renamer = ImageRenamer()

    if args.file:
        for file_path in args.file:
                print(f"The argument provided is: \n{file_path}")
                renamer.rename_image(file_path)
    
    if args.directory:
        print(f"Renaming all images in directory: {args.directory}")
        renamer.rename_images_in_directory(args.directory)
    
    if args.remove:
        print(f"The argument provided is: Remove the registry entry.")
        renamer.remove_registry_entry()
    
    if args.reg:
        print(f"The argument provided is: Generate the registry file.")

        python_exe_path = sys.executable.replace("\\", "\\\\")  
        main_py_path = os.path.abspath(__file__).replace("\\", "\\\\")
        current_script_path = os.path.dirname(os.path.abspath(__file__)).replace("\\", "\\\\")

        renamer.generate_reg_file(python_exe_path, main_py_path, current_script_path)

    os._exit(os.X_OK)

if __name__ == "__main__":
    main()