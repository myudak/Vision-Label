<h1 align="center">Vision-Label</h1><br>

<p align="center">
simply describe what is in the image, then rename the file to something understandable to a human.
</p><br>

<p align="center">
  <!-- <a href="#"><img alt="Android OS" src="https://img.shields.io/badge/OS-Android-3DDC84?style=flat-square&logo=android"></a>
  <a href="#"><img alt="Languages-Kotlin" src="https://flat.badgen.net/badge/Language/Kotlin?icon=https://raw.githubusercontent.com/binaryshrey/Awesome-Android-Open-Source-Projects/master/assets/Kotlin_Logo_icon_white.svg&color=f18e33"/></a> -->
  <a href="#"><img alt="Languages-Python" src="https://img.shields.io/badge/Language-Python-1DA1F2?style=flat-square&logo=java"></a>
    <a href="#"><img alt="OpenSource" src="https://flat.badgen.net/badge/Open-Source/HacktoberFest?icon=https://raw.githubusercontent.com/binaryshrey/Awesome-Android-Open-Source-Projects/master/assets/DO_Logo_icon_white.svg&color=f18e33"/></a>
  <a href="#"><img alt="PRs" src="https://img.shields.io/badge/PRs-Welcome-3DDC84?style=flat-square"></a>
</p>
<p align="center">
  <a href="https://github.com/myudak/Vision-Label"><img alt="Github - myudak" src="https://img.shields.io/badge/GitHub-VisionLabel-181717?style=flat-square&logo=github"></a>
</p>

<br/>

[demo][DEMO]

VisionLabel is a powerful Python-based command-line utility tool designed to rename image files using the capabilities of the Gemini API. Descriptive filenames are generated based on the content of the image.

## Features

- Automatically rename image files with descriptive names generated by the Gemini API
- Right-click context menu integration for quick and easy file renaming
- Customizable name generation based on user-defined templates
- Create and utilize a mapping file for batch renaming operations
- Validate generated names with the Gemini API before applying changes
- Retry attempts for name generation and validation in case of errors
- Supports various image file types: `.png`, `.jpeg`, `.jpg`, `.webp`, `.bmp`,`.gif` (non-animated)

## Dependencies

- Python 3.x
- Google-generativeai
- PIL Library

## Setup

### 1. Get a Gemini API Key for Free

Sign up and get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 2. Add Environment Variables

Create a `.env` file in the root directory of your project and replace `GOOGLE_API_KEY` with your actual API key:

```
GOOGLE_API_KEY=your_api_key_here
```

### 3. Install Dependencies

Run the following command to install all required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### From the Command Line

You can rename an image by specifying the path to the image:

```bash
python main.py --file path_to_image
```

You can also rename all the image in a directory by specifying the path to the directory:

```bash
python main.py --directory path_to_directory
```

**Example:**

```bash
python main.py --file ./img/example.jpg
```

### From the Windows Context Menu

#### Generate the `add_context_menu.reg` File

Run the following command to generate the registry file:

```bash
python main.py --reg
```

#### Initialize the Registry File

Add the context menu entry by running:

```bash
regedit add_context_menu.reg
```

note: you may need to run `regedit` as an administrator. Alternatively you can doube click the file to run it

Now, you can right-click on any image and select `Rename with Vision-Label` to rename the image using the Gemini API.

#### Remove the Context Menu Entry

If you want to remove the context menu entry, run:

```bash
python main.py --remove
```

## How It Was Built

1. Find the image in the given directory.
2. Images are sent to the Gemini API, where they are processed, and a caption is returned.
3. Rename the files with a new name from the Gemini API.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This application uploads images to Google servers for processing using the Gemini API. Use caution and avoid using personal images. This tool is not affiliated with Google. The functionality is subject to change based on updates to the Gemini API or the terms of service of Google.

## Credits

- Gemini API
- Google AI Studio

[DEMO]: https://github.com/myudak/Vision-Label/assets/69108782/5878884a-e753-48c9-835b-59224fff9ce6
