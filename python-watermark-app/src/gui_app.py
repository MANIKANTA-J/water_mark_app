import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
from PIL import Image, ImageTk
import os
from watermark import Watermarker

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermark Application")
        self.root.geometry("1200x700")  # Wider window for split view
        self.root.configure(bg='#f0f0f0')
        
        # Initialize variables
        self.selected_images = []
        self.watermarker = Watermarker()
        self.preview_image = None
        self.watermark_type = tk.StringVar(value="text")
        self.text_color = (255, 255, 255)  # Default white
        self.logo_path = ""
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main title (top of window)
        title_label = tk.Label(
            self.root, 
            text="Image Watermark Application", 
            font=("Arial", 20, "bold"), 
            bg='#f0f0f0', 
            fg='#333'
        )
        title_label.pack(pady=10)

        # Create PanedWindow for resizable split view
        paned_window = tk.PanedWindow(
            self.root, 
            orient=tk.HORIZONTAL, 
            sashrelief=tk.RAISED,
            sashwidth=8
        )
        paned_window.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Left Frame (Controls)
        left_frame = ttk.Frame(paned_window, width=500)
        paned_window.add(left_frame, minsize=400)

        # Right Frame (Preview)
        right_frame = ttk.Frame(paned_window)
        paned_window.add(right_frame, minsize=400)

        # Setup controls in left frame
        self.setup_controls(left_frame)

        # Setup preview in right frame
        self.setup_preview_section(right_frame)

    def setup_controls(self, parent):
        # Image selection section
        self.setup_image_selection(parent)
        
        # Watermark type selection
        self.setup_watermark_type(parent)
        
        # Watermark options
        self.setup_watermark_options(parent)
        
        # Action buttons
        self.setup_action_buttons(parent)
        
        # Progress bar
        self.progress = ttk.Progressbar(parent, mode='determinate')
        self.progress.pack(fill=tk.X, pady=10)

    def setup_image_selection(self, parent):
        img_frame = ttk.LabelFrame(parent, text="Select Images", padding=10)
        img_frame.pack(fill=tk.X, pady=5)
        
        btn_frame = ttk.Frame(img_frame)
        btn_frame.pack(fill=tk.X)
        
        ttk.Button(btn_frame, text="Select Images", command=self.select_images).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Clear Selection", command=self.clear_images).pack(side=tk.LEFT, padx=5)
        
        self.images_listbox = tk.Listbox(img_frame, height=4)
        self.images_listbox.pack(fill=tk.X, pady=5)
        
        scrollbar = ttk.Scrollbar(img_frame, orient=tk.VERTICAL, command=self.images_listbox.yview)
        self.images_listbox.configure(yscrollcommand=scrollbar.set)

    def setup_watermark_type(self, parent):
        type_frame = ttk.LabelFrame(parent, text="Watermark Type", padding=10)
        type_frame.pack(fill=tk.X, pady=5)
        
        ttk.Radiobutton(
            type_frame, 
            text="Text Watermark", 
            variable=self.watermark_type, 
            value="text",
            command=self.on_watermark_type_change
        ).pack(side=tk.LEFT, padx=10)
        
        ttk.Radiobutton(
            type_frame, 
            text="Logo Watermark", 
            variable=self.watermark_type, 
            value="logo",
            command=self.on_watermark_type_change
        ).pack(side=tk.LEFT, padx=10)

    def setup_watermark_options(self, parent):
        # Options frame
        self.options_frame = ttk.LabelFrame(parent, text="Watermark Options", padding=10)
        self.options_frame.pack(fill=tk.X, pady=5)
        
        # Text options
        self.text_options_frame = ttk.Frame(self.options_frame)
        self.text_options_frame.pack(fill=tk.X)
        
        # Text input
        ttk.Label(self.text_options_frame, text="Text:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.text_entry = ttk.Entry(self.text_options_frame, width=30)
        self.text_entry.grid(row=0, column=1, padx=5, pady=2)
        self.text_entry.insert(0, "Sample Watermark")
        
        # Font size
        ttk.Label(self.text_options_frame, text="Font Size:").grid(row=1, column=0, sticky=tk.W, padx=5)
        self.font_size_var = tk.IntVar(value=20)
        ttk.Spinbox(
            self.text_options_frame, 
            from_=10, 
            to=100, 
            textvariable=self.font_size_var, 
            width=10
        ).grid(row=1, column=1, padx=5, pady=2, sticky=tk.W)
        
        ttk.Label(self.text_options_frame, text="Text Color:").grid(row=2, column=0, sticky=tk.W, padx=5)
        self.color_button = ttk.Button(
            self.text_options_frame, 
            text="Choose Color", 
            command=self.choose_color
        )
        self.color_button.grid(row=2, column=1, padx=5, pady=2, sticky=tk.W)
        
        # Logo options frame
        self.logo_options_frame = ttk.Frame(self.options_frame)
        
        ttk.Label(self.logo_options_frame, text="Logo File:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.logo_entry = ttk.Entry(self.logo_options_frame, width=40)
        self.logo_entry.grid(row=0, column=1, padx=5, pady=2)
        ttk.Button(
            self.logo_options_frame, 
            text="Browse", 
            command=self.select_logo
        ).grid(row=0, column=2, padx=5)
        
        ttk.Label(self.logo_options_frame, text="Transparency:").grid(row=1, column=0, sticky=tk.W, padx=5)
        self.transparency_var = tk.IntVar(value=128)
        ttk.Scale(
            self.logo_options_frame, 
            from_=0, 
            to=255, 
            variable=self.transparency_var, 
            orient=tk.HORIZONTAL
        ).grid(row=1, column=1, padx=5, pady=2, sticky=tk.EW)
        
        # Position options (common for both)
        position_frame = ttk.Frame(self.options_frame)
        position_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(position_frame, text="Position:").pack(side=tk.LEFT, padx=5)
        self.position_var = tk.StringVar(value="bottom-right")
        positions = [
            ("Top Left", "top-left"), 
            ("Top Right", "top-right"), 
            ("Bottom Left", "bottom-left"), 
            ("Bottom Right", "bottom-right"),
            ("Center", "center")
        ]
        
        for text, value in positions:
            ttk.Radiobutton(
                position_frame, 
                text=text, 
                variable=self.position_var, 
                value=value
            ).pack(side=tk.LEFT, padx=5)
        
        self.on_watermark_type_change()

    def setup_preview_section(self, parent):
        preview_frame = ttk.LabelFrame(parent, text="Preview", padding=10)
        preview_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Preview canvas (expands to fill space)
        self.preview_canvas = tk.Canvas(
            preview_frame, 
            bg='white', 
            highlightthickness=0
        )
        self.preview_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Preview button (centered below canvas)
        btn_frame = ttk.Frame(preview_frame)
        btn_frame.pack(pady=5)
        
        ttk.Button(
            btn_frame, 
            text="Generate Preview", 
            command=self.generate_preview
        ).pack()

    def setup_action_buttons(self, parent):
        action_frame = ttk.Frame(parent)
        action_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(
            action_frame, 
            text="Apply Watermark to All Images", 
            command=self.apply_watermark, 
            style='Accent.TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            action_frame, 
            text="Exit", 
            command=self.root.quit
        ).pack(side=tk.RIGHT, padx=5)
        
    def select_images(self):
        filetypes = [
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif"),
            ("JPEG files", "*.jpg *.jpeg"),
            ("PNG files", "*.png"),
            ("All files", "*.*")
        ]
        
        files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=filetypes
        )
        
        if files:
            self.selected_images = list(files)
            self.update_images_listbox()
            
    def clear_images(self):
        self.selected_images = []
        self.update_images_listbox()
        
    def update_images_listbox(self):
        self.images_listbox.delete(0, tk.END)
        for img_path in self.selected_images:
            filename = os.path.basename(img_path)
            self.images_listbox.insert(tk.END, filename)
            
    def on_watermark_type_change(self):
        if self.watermark_type.get() == "text":
            self.logo_options_frame.pack_forget()
            self.text_options_frame.pack(fill=tk.X)
        else:
            self.text_options_frame.pack_forget()
            self.logo_options_frame.pack(fill=tk.X)
            
    def choose_color(self):
        color = colorchooser.askcolor(title="Choose text color")
        if color[0]:  # color[0] is RGB tuple, color[1] is hex
            self.text_color = tuple(int(c) for c in color[0])
            
    def select_logo(self):
        filetypes = [
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif"),
            ("PNG files", "*.png"),
            ("All files", "*.*")
        ]
        
        file = filedialog.askopenfilename(
            title="Select Logo",
            filetypes=filetypes
        )
        
        if file:
            self.logo_path = file
            self.logo_entry.delete(0, tk.END)
            self.logo_entry.insert(0, file)
            
    def get_position_coordinates(self, image_size, watermark_size=None):
        width, height = image_size
        position = self.position_var.get()
        
        if watermark_size:
            w_width, w_height = watermark_size
        else:
            w_width, w_height = 100, 30  # Default text size estimate

        padding = 30  # Space from edges
        if watermark_size:
            padding = 10
        # Define positions based on selected option
        positions = {
            "top-left": (padding, padding),
            "top-right": (width - w_width - (3*padding), padding),
            "bottom-left": (padding, height - w_height - padding),
            "bottom-right": (width - w_width - (3*padding), height - w_height - padding),
            "center": ((width - w_width) // 2, (height - w_height) // 2),
        }
        return positions.get(position, (0, 0))
    
    def get_logo_position_coordinates(self, image_size, watermark_size=None):
        width, height = image_size
        position = self.position_var.get()
        
        if watermark_size:
            w_width, w_height = watermark_size
        else:
            w_width, w_height = 100, 30  # Default text size estimate

        padding = 30  # Space from edges
        if watermark_size:
            padding = 10
        # Define positions based on selected option
        positions = {
            "top-left": (padding, padding),
            "top-right": (width - w_width - (3*padding), padding),
            "bottom-left": (padding, height - w_height - (3*padding)),
            "bottom-right": (width - w_width - (3*padding), height - w_height - (3*padding)),
            "center": ((width - w_width) // 2, (height - w_height) // 2),
        }
        return positions.get(position, (0, 0))
    
    def generate_preview(self):
        if not self.selected_images:
            messagebox.showwarning("Warning", "Please select at least one image first.")
            return
            
        try:
            # Use the first selected image for preview
            image_path = self.selected_images[0]
            image = Image.open(image_path)
            
            # Create watermarked preview
            if self.watermark_type.get() == "text":
                text = self.text_entry.get()
                if not text:
                    messagebox.showwarning("Warning", "Please enter watermark text.")
                    return
                    
                font_size = self.font_size_var.get()
                position = self.get_position_coordinates(image.size)
                
                watermarked = self.watermarker.add_text_watermark(
                    image_path, text, position, font_size, self.text_color
                )
            else:
                if not self.logo_path:
                    messagebox.showwarning("Warning", "Please select a logo file.")
                    return
                    
                position = self.get_logo_position_coordinates(image.size)
                transparency = self.transparency_var.get()
                
                watermarked = self.watermarker.add_logo_watermark(
                    image_path, self.logo_path, position, transparency
                )
            
            # Resize for preview
            watermarked.thumbnail((400, 300), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage for display
            self.preview_image = ImageTk.PhotoImage(watermarked)
            
            # Clear canvas and display preview
            self.preview_canvas.delete("all")
            canvas_width = self.preview_canvas.winfo_width()
            canvas_height = self.preview_canvas.winfo_height()
            
            x = (canvas_width - watermarked.width) // 2
            y = (canvas_height - watermarked.height) // 2
            
            self.preview_canvas.create_image(x, y, anchor=tk.NW, image=self.preview_image)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate preview: {str(e)}")
            
    def apply_watermark(self):
        if not self.selected_images:
            messagebox.showwarning("Warning", "Please select at least one image first.")
            return
            
        # Get output directory
        output_dir = filedialog.askdirectory(title="Select Output Directory")
        if not output_dir:
            return
            
        try:
            total_images = len(self.selected_images)
            self.progress['maximum'] = total_images
            self.progress['value'] = 0
            
            for i, image_path in enumerate(self.selected_images):
                # Update progress
                self.progress['value'] = i
                self.root.update_idletasks()
                
                # Generate watermarked image
                if self.watermark_type.get() == "text":
                    text = self.text_entry.get()
                    if not text:
                        messagebox.showwarning("Warning", "Please enter watermark text.")
                        return
                        
                    font_size = self.font_size_var.get()
                    image = Image.open(image_path)
                    position = self.get_position_coordinates(image.size)
                    
                    watermarked = self.watermarker.add_text_watermark(
                        image_path, text, position, font_size, self.text_color
                    )
                else:
                    if not self.logo_path:
                        messagebox.showwarning("Warning", "Please select a logo file.")
                        return
                        
                    image = Image.open(image_path)
                    position = self.get_logo_position_coordinates(image.size)
                    transparency = self.transparency_var.get()
                    
                    watermarked = self.watermarker.add_logo_watermark(
                        image_path, self.logo_path, position, transparency
                    )
                
                # Save watermarked image
                filename = os.path.basename(image_path)
                name, ext = os.path.splitext(filename)
                output_filename = f"{name}_watermarked{ext}"
                output_path = os.path.join(output_dir, output_filename)
                
                watermarked.save(output_path, quality=95)
                
            # Complete progress
            self.progress['value'] = total_images
            self.root.update_idletasks()
            
            messagebox.showinfo("Success", 
                              f"Successfully watermarked {total_images} images!\n"
                              f"Output directory: {output_dir}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply watermark: {str(e)}")
        finally:
            self.progress['value'] = 0

def main():
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()