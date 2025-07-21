# Python Watermark Application

A user-friendly GUI application for adding watermarks to images. Supports both text and logo watermarks with customizable options.

## Features

- **GUI Interface**: Easy-to-use graphical interface built with tkinter
- **Multiple Image Support**: Process multiple images at once
- **Text Watermarks**: Add custom text with adjustable font size, color, and position
- **Logo Watermarks**: Add logo/image watermarks with transparency control
- **Preview Function**: Preview watermarks before applying to all images
- **Flexible Positioning**: Choose from 5 different watermark positions
- **Batch Processing**: Apply watermarks to multiple images simultaneously
- **Progress Tracking**: Visual progress bar during batch processing

## Installation

1. Make sure you have Python 3.6+ installed
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### GUI Application (Recommended)

Run the GUI application:
```bash
python run_gui.py
```

#### Using the GUI:

1. **Select Images**: Click "Select Images" to choose one or more image files
2. **Choose Watermark Type**: Select either "Text Watermark" or "Logo Watermark"
3. **Configure Options**:
   - **For Text**: Enter text, adjust font size, choose color
   - **For Logo**: Browse and select a logo file, adjust transparency
4. **Set Position**: Choose where to place the watermark (top-left, top-right, bottom-left, bottom-right, or center)
5. **Preview**: Click "Generate Preview" to see how the watermark will look
6. **Apply**: Click "Apply Watermark to All Images" and select an output directory

### Command Line Application

For command-line usage, run:
```bash
python src/main.py
```

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- GIF (.gif)

## File Structure

```
python-watermark-app/
├── src/
│   ├── main.py          # Command-line interface
│   ├── gui_app.py       # GUI application
│   ├── watermark.py     # Core watermarking functionality
│   └── utils.py         # Utility functions
├── run_gui.py           # GUI launcher script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Examples

### Text Watermark
- Add custom text like "© 2024 Your Name" or "CONFIDENTIAL"
- Customize font size (10-100)
- Choose any color
- Semi-transparent background for better visibility

### Logo Watermark
- Add company logos or personal branding
- Adjustable transparency (0-255)
- Automatic resizing to 20% of image size
- Supports PNG logos with transparency

## Tips

1. **For best results with text watermarks**: Use contrasting colors and appropriate font sizes
2. **For logo watermarks**: Use PNG files with transparent backgrounds
3. **Preview first**: Always generate a preview before applying to all images
4. **Backup originals**: The app creates new files with "_watermarked" suffix, preserving originals

## Troubleshooting

- **Font issues**: The app will fallback to default fonts if system fonts aren't available
- **Large images**: Processing may take longer for high-resolution images
- **Memory usage**: Processing many large images simultaneously may require more RAM

## License

This project is open source and available under the MIT License.