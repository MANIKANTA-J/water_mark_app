def load_image(filepath):
    from PIL import Image
    try:
        image = Image.open(filepath)
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def save_image(image, output_path):
    try:
        image.save(output_path)
    except Exception as e:
        print(f"Error saving image: {e}")

def validate_file_path(filepath):
    import os
    return os.path.isfile(filepath) and filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))