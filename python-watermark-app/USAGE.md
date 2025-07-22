# Python Watermark Application Usage Guide

This document explains how to use the Python Watermark Application, including both the GUI and command-line interfaces.

## Overview
This app allows users to add watermarks (text or logo) to images with customizable options. It supports batch processing, preview, and flexible positioning.

## Installation
1. Ensure Python 3.6+ is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## GUI Usage
1. Launch the GUI:
   ```bash
   python run_gui.py
   ```
2. Steps in the GUI:
   - Select images to watermark.
   - Choose watermark type: Text or Logo.
   - Configure options:
     - For Text: Enter text, set font size, color.
     - For Logo: Select logo file, set transparency.
   - Set watermark position (top-left, top-right, bottom-left, bottom-right, center).
   - Preview watermark before applying.
   - Apply watermark to all images and select output directory.

## Command-Line Usage
1. Run the CLI:
   ```bash
   python src/main.py
   ```
2. Follow prompts or use command-line arguments to specify images, watermark type, options, and output.

## Supported Formats
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- GIF (.gif)

## Example Workflows
### Text Watermark
- Add text like "© 2024 Your Name" or "CONFIDENTIAL".
- Customize font size (10-100), color, and background transparency.

### Logo Watermark
- Add a logo (PNG recommended for transparency).
- Set transparency (0-255), auto-resize to 20% of image size.

## Tips
- Use contrasting colors for text watermarks.
- Use transparent PNGs for logo watermarks.
- Always preview before applying to all images.
- Originals are preserved; output files have "_watermarked" suffix.

## Troubleshooting
- Font issues: Defaults to system fonts if unavailable.
- Large images: May take longer to process.
- High memory usage: Batch processing of large images may require more RAM.

## License
MIT License.
