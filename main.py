import os
import argparse
import sys
from scripts.image_renamer import ImageRenamer

def main():
    parser = argparse.ArgumentParser(description="Rename an image file based on a generated name.")
    parser.add_argument("--path",  type=str, help="Path to the image file to rename.")
    parser.add_argument("--reg", action="store_true", help="Generate the registry file.")
    parser.add_argument("--remove", action="store_true", help="Remove the registry entry.")

    args = parser.parse_args()
    renamer = ImageRenamer()

    if args.path:
        print(f"The argument provided is: \nRename {args.path}")
        renamer.rename_image(args.path)
    
    if args.remove:
        print(f"The argument provided is: Remove the registry entry.")
        renamer.remove_registry_entry()
    
    if args.reg:
        print(f"The argument provided is: Generate the registry file.")

        python_exe_path = sys.executable.replace("\\", "\\\\")  
        main_py_path = os.path.abspath(__file__).replace("\\", "\\\\")
        current_script_path = os.path.abspath(__file__).replace("\\", "\\\\")

        renamer.generate_reg_file(python_exe_path, main_py_path, current_script_path)

    os._exit(os.X_OK)

if __name__ == "__main__":
    main()