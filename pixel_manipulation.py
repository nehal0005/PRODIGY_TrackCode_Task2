import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk


class ImageEncryptionApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Manipulation Tool")
        self.root.geometry("600x650")
        self.root.configure(bg="#1e1e2e")  # Sleek dark purple/grey theme
        self.root.resizable(False, False)

        # Force window focus on startup
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.after(1, lambda: self.root.attributes("-topmost", False))

        self.image_path = None
        self.preview_img = None

        self.setup_ui()

    def setup_ui(self):
        # 1. Header Title
        lbl_title = tk.Label(
            self.root,
            text="PIXEL MANIPULATION TOOL",
            font=("Helvetica", 18, "bold"),
            fg="#89b4fa",
            bg="#1e1e2e",
        )
        lbl_title.pack(pady=20)

        # 2. Image Selection & Preview Frame
        self.frame_preview = tk.Frame(
            self.root,
            width=350,
            height=250,
            bg="#313244",
            highlightbackground="#45475a",
            highlightthickness=2,
        )
        self.frame_preview.pack_propagate(False)
        self.frame_preview.pack(pady=10)

        self.lbl_preview = tk.Label(
            self.frame_preview,
            text="No Image Selected\n\nClick 'Select Image' Below",
            font=("Helvetica", 10),
            fg="#a6adc8",
            bg="#313244",
        )
        self.lbl_preview.pack(expand=True)

        # Select Image Button
        btn_select = tk.Button(
            self.root,
            text="Select Image File",
            command=self.load_image,
            font=("Helvetica", 11, "bold"),
            bg="#89b4fa",
            fg="#11111b",
            activebackground="#b4befe",
            cursor="hand2",
            padx=15,
            pady=5,
        )
        btn_select.pack(pady=10)

        # 3. Settings Frame (Key entry)
        frame_settings = tk.Frame(self.root, bg="#1e1e2e")
        frame_settings.pack(pady=15)

        lbl_key = tk.Label(
            frame_settings,
            text="Encryption/Decryption Key (0-255):",
            font=("Helvetica", 10, "bold"),
            fg="#cdd6f4",
            bg="#1e1e2e",
        )
        lbl_key.pack(side="left", padx=10)

        self.entry_key = tk.Entry(
            frame_settings,
            width=8,
            font=("Helvetica", 11, "bold"),
            bg="#313244",
            fg="#cdd6f4",
            insertbackground="white",
            justify="center",
        )
        self.entry_key.pack(side="left")
        self.entry_key.insert(0, "42")  # Default key

        # 4. Action Buttons (Encrypt and Decrypt)
        frame_actions = tk.Frame(self.root, bg="#1e1e2e")
        frame_actions.pack(pady=15)

        btn_encrypt = tk.Button(
            frame_actions,
            text="🔒 Encrypt Image",
            command=lambda: self.process_image("encrypt"),
            font=("Helvetica", 12, "bold"),
            bg="#f38ba8",
            fg="#11111b",
            activebackground="#f2cdcd",
            cursor="hand2",
            width=15,
            pady=8,
        )
        btn_encrypt.pack(side="left", padx=15)

        btn_decrypt = tk.Button(
            frame_actions,
            text="🔓 Decrypt Image",
            command=lambda: self.process_image("decrypt"),
            font=("Helvetica", 12, "bold"),
            bg="#a6e3a1",
            fg="#11111b",
            activebackground="#94e2d5",
            cursor="hand2",
            width=15,
            pady=8,
        )
        btn_decrypt.pack(side="left", padx=15)

        # Footer Status Label
        self.lbl_status = tk.Label(
            self.root,
            text="Ready",
            font=("Helvetica", 9, "italic"),
            fg="#6c7086",
            bg="#1e1e2e",
        )
        self.lbl_status.pack(side="bottom", pady=15)

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if file_path:
            self.image_path = file_path
            self.lbl_status.config(
                text=f"Selected: {os.path.basename(file_path)}"
            )

            # Generate scaled preview
            img = Image.open(file_path)
            img.thumbnail((340, 240))
            self.preview_img = ImageTk.PhotoImage(img)

            self.lbl_preview.config(image=self.preview_img, text="")
            self.lbl_preview.image = self.preview_img

    def process_image(self, action_type):
        if not self.image_path:
            messagebox.showwarning(
                "Missing File", "Please select an image file first!"
            )
            return

        # Validate Key
        try:
            key = int(self.entry_key.get())
            if not (0 <= key <= 255):
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Invalid Key", "Please enter a key integer value between 0 and 255."
            )
            return

        try:
            # Open Image and load pixels
            img = Image.open(self.image_path)
            img = img.convert("RGB")  # Ensure standard format
            pixels = img.load()

            width, height = img.size

            # Manipulate every pixel using XOR bitwise calculation
            for x in range(width):
                for y in range(height):
                    r, g, b = pixels[x, y]
                    # Applying XOR operation on each channel
                    pixels[x, y] = (r ^ key, g ^ key, b ^ key)

            # Ask user where to save the output file
            default_name = f"{action_type}ed_image.png"
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                initialfile=default_name,
                filetypes=[("PNG Image", "*.png")],
            )

            if save_path:
                img.save(save_path)
                messagebox.showinfo(
                    "Success", f"Image {action_type}ed successfully and saved!"
                )
                self.lbl_status.config(
                    text=f"Saved output to {os.path.basename(save_path)}"
                )

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptionApp(root)
    root.mainloop()