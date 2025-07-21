#!/usr/bin/env python3
"""
Test script for the watermark application
Creates sample images for testing if none are available
"""

import os
import sys
from PIL import Image, ImageDraw

def create_sample_images():
    """Create sample images for testing the watermark application"""
    
    # Create samples directory
    samples_dir = os.path.join(os.path.dirname(__file__), 'samples')
    os.makedirs(samples_dir, exist_ok=True)
    
    # Create sample images
    colors = [
        ('red', (255, 100, 100)),
        ('blue', (100, 100, 255)),
        ('green', (100, 255, 100)),
    ]
    
    for name, color in colors:
        # Create a simple colored image
        img = Image.new('RGB', (800, 600), color)
        draw = ImageDraw.Draw(img)
        
        # Add some text to make it interesting
        draw.text((50, 50), f"Sample {name.title()} Image", fill=(255, 255, 255))
        draw.text((50, 100), "This is a test image for watermarking", fill=(255, 255, 255))
        
        # Draw some shapes
        draw.rectangle([200, 200, 400, 400], outline=(255, 255, 255), width=3)
        draw.ellipse([450, 200, 650, 400], outline=(255, 255, 255), width=3)
        
        # Save the image
        img_path = os.path.join(samples_dir, f'sample_{name}.jpg')
        img.save(img_path, 'JPEG', quality=95)
        print(f"Created sample image: {img_path}")
    
    # Create a sample logo
    logo = Image.new('RGBA', (200, 100), (0, 0, 0, 0))  # Transparent background
    draw = ImageDraw.Draw(logo)
    
    # Draw a simple logo
    draw.rectangle([10, 10, 190, 90], fill=(255, 255, 255, 200), outline=(0, 0, 0, 255), width=2)
    draw.text((50, 35), "LOGO", fill=(0, 0, 0, 255))
    
    logo_path = os.path.join(samples_dir, 'sample_logo.png')
    logo.save(logo_path, 'PNG')
    print(f"Created sample logo: {logo_path}")
    
    print(f"\nSample files created in: {samples_dir}")
    print("You can now test the watermark application with these files!")

def main():
    print("Watermark Application Test Setup")
    print("=" * 40)
    
    # Check if PIL is available
    try:
        from PIL import Image
        print("✓ PIL/Pillow is available")
    except ImportError:
        print("✗ PIL/Pillow is not installed. Run: pip install -r requirements.txt")
        return
    
    # Check if tkinter is available
    try:
        import tkinter
        print("✓ tkinter is available")
    except ImportError:
        print("✗ tkinter is not available. Please install tkinter.")
        return
    
    # Create sample images
    print("\nCreating sample images...")
    create_sample_images()
    
    print("\nTo test the application:")
    print("1. Run: python run_gui.py")
    print("2. Use the sample images in the 'samples' directory")
    print("3. Try both text and logo watermarks")
    
    # Ask if user wants to run the GUI
    try:
        response = input("\nWould you like to run the GUI application now? (y/n): ")
        if response.lower() in ['y', 'yes']:
            print("Starting GUI application...")
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
            from gui_app import main as gui_main
            gui_main()
    except KeyboardInterrupt:
        print("\nTest setup completed.")

if __name__ == "__main__":
    main()