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

<br>
<p align="center">
<img width="720px" src="" alt=""></img>
</p><br>

## Dependencies

- Python 3
- google-generativeai
- PIL

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
python main.py --path path_to_image
```

**Example:**

```bash
python main.py --path ./img/example.jpg
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

Now, you can right-click on any image and select `Rename with Gemini` to rename the image using the Gemini API.

#### Remove the Context Menu Entry

If you want to remove the context menu entry, run:

```bash
python main.py --remove
```

## How It Was Built

1. Find the image in the given directory.
2. Images are sent to the Gemini API, where they are processed, and a caption is returned.
3. Rename the files with a new name from the Gemini API.

## Disclaimer

This application uploads images to Google servers for processing using the Gemini API. Use caution and avoid using personal images.

## Credits

- Gemini API
- Google AI Studio
