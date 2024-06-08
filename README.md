# Vision-Label
Rename images using Gemini

## Dependencies

- Python 3
- google-generativeai
- PIL

## Usage 

### 1) Get a Gemini API Key for Free

[api key](https://aistudio.google.com/app/apikey)

### 2) Add env

Replace `GOOGLE_API_KEY` value with your API KEY  in .env

## Usage

```
python --path path_to_image
```

EXAMPLE `python3 renamer.py /img/example.jpg`

NOTICE: Do not use a trailing slash in dir

## 4) Enjoy!

the image in the given directory will be renamed with meaningful names now. 



## How It was Built

1. Find the image in the given directory.
2. Images will be sent to the Gemini API. Gemini processes the image and sends back a caption.
3. Rename the files with a new name from the Gemini API.

## Disclaimer

It uploads the images to Google servers as it using gemini API, do not use it with personal images. (or use it with caution) 

## Credits
Gemini API
