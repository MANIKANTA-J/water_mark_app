import os
from PIL import Image
from watermark import Watermarker

def main():
    print("Welcome to the Watermarking Application!")
    
    # Get user input for image files
    image_files = input("Enter the paths of the images you want to watermark (comma-separated): ").split(',')
    image_files = [file.strip() for file in image_files]
    
    # Get user input for watermark type
    watermark_type = input("Do you want to add a text watermark or a logo? (text/logo): ").strip().lower()
    
    watermarker = Watermarker()
    
    if watermark_type == 'text':
        text = input("Enter the text for the watermark: ")
        for image_file in image_files:
            watermarker.add_text_watermark(image_file, text)
    elif watermark_type == 'logo':
        logo_path = input("Enter the path of the logo image: ")
        for image_file in image_files:
            watermarker.add_logo_watermark(image_file, logo_path)
    else:
        print("Invalid watermark type selected.")
    
    print("Watermarking process completed.")

if __name__ == "__main__":
    main()