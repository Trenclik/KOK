from PIL import Image, ImageOps
import os
import tkinter as tk
root = tk.Tk()
velikos = float(root.winfo_screenheight() /6)* 5
velikost =  round(velikos)
def resize_to_fit_bezel(image):
    bezel_size = velikost #velikost rámečku
    max_dimension = max(image.width, image.height)

    if max_dimension >= bezel_size:
        # zmenšení
        ratio = bezel_size / max_dimension
        new_width = int(image.width * ratio)
        new_height = int(image.height * ratio)
        return image.resize((new_width, new_height), Image.LANCZOS)
    else:
        # zvětšení
        ratio = bezel_size / max_dimension
        new_width = int(image.width * ratio)
        new_height = int(image.height * ratio)
        scaled_image = image.resize((new_width, new_height), Image.LANCZOS)
        pad_x = (bezel_size - scaled_image.width) // 2
        pad_y = (bezel_size - scaled_image.height) // 2
        padded_image = ImageOps.expand(scaled_image, (pad_x, pad_y, pad_x, pad_y), (0,0,0))
        return padded_image

def convert_to_png(image_path, output_folder):
    #konvertuje do rgba
    image = Image.open(image_path).convert('RGBA')

    #změní velikost rámečku
    bezel_image = resize_to_fit_bezel(image)

    #vytvoří rámeček
    bezel_size = velikost
    new_image = Image.new('RGB', (bezel_size, bezel_size), (0,0,0))

    #vypočítá střed rámečku
    x_offset = (bezel_size - bezel_image.width) // 2
    y_offset = (bezel_size - bezel_image.height) // 2

    #vloží předimenzovaný obrázek
    new_image.paste(bezel_image, (x_offset, y_offset))

    # Save the bezel image as PNG in the output folder
    output_path = os.path.join(output_folder, os.path.basename(image_path)[:-4] + '.png')
    new_image.save(output_path, format='PNG')

def main(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            image_path = os.path.join(input_folder, filename)
            convert_to_png(image_path, output_folder)

if __name__ == "__main__":
    input_folder = "jozi_fotky"  # Replace with the path to your input folder
    output_folder = "upraveny_josi"  # Replace with the path to the output folder
    main(input_folder, output_folder)