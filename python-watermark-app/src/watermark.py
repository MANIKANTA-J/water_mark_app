class Watermarker:
    def __init__(self):
        pass

    def add_text_watermark(self, image_path, text, position=(0, 0), font_size=20, color=(255, 255, 255)):
        from PIL import Image, ImageDraw, ImageFont
        import os
        
        # Load the image
        image = Image.open(image_path).convert("RGBA")
        width, height = image.size
        
        # Create a transparent overlay
        overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        # Try to load a better font
        try:
            # Try to use a system font
            if os.name == 'nt':  # Windows
                font = ImageFont.truetype("arial.ttf", font_size)
            else:  # Linux/Mac
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
        except:
            # Fallback to default font
            font = ImageFont.load_default()

        # Add semi-transparent background for better text visibility
        text_bbox = draw.textbbox(position, text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Draw semi-transparent background
        bg_color = (0, 0, 0, 100)  # Semi-transparent black
        draw.rectangle([position[0]-5, position[1]-5, 
                       position[0]+text_width+5, position[1]+text_height+5], 
                      fill=bg_color)

        # Draw the text on the overlay
        draw.text(position, text, fill=color + (255,), font=font)

        # Combine the overlay with the original image
        watermarked = Image.alpha_composite(image, overlay)

        # Convert back to RGB
        watermarked = watermarked.convert("RGB")
        return watermarked

    def add_logo_watermark(self, image_path, logo_path, position=(0, 0), transparency=128):
        from PIL import Image

        # Load the image and logo
        image = Image.open(image_path).convert("RGBA")
        logo = Image.open(logo_path).convert("RGBA")

        # Resize logo if needed
        logo = logo.resize((int(image.width * 0.2), int(image.height * 0.2)))  # Resize logo to 20% of the image size

        # Create a transparent overlay for the logo
        logo_with_transparency = logo.copy()
        logo_with_transparency.putalpha(transparency)

        # Paste the logo onto the image
        image.paste(logo_with_transparency, position, logo_with_transparency)

        # Save the watermarked image
        return image.convert("RGB")  # Convert back to RGB before saving