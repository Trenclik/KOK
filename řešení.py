from PIL import Image, ImageOps
import os

def resize_to_fit_bezel(image):
    # Resize the image to fit inside the 720x720 bezel while maintaining its aspect ratio
    bezel_size = 800
    max_dimension = max(image.width, image.height)

    if max_dimension >= bezel_size:
        # If the image is larger than the bezel, scale it down
        ratio = bezel_size / max_dimension
        new_width = int(image.width * ratio)
        new_height = int(image.height * ratio)
        return image.resize((new_width, new_height), Image.LANCZOS)
    else:
        # If the image is smaller than the bezel, scale it up and add white padding
        ratio = bezel_size / max_dimension
        new_width = int(image.width * ratio)
        new_height = int(image.height * ratio)
        scaled_image = image.resize((new_width, new_height), Image.LANCZOS)
        pad_x = (bezel_size - scaled_image.width) // 2
        pad_y = (bezel_size - scaled_image.height) // 2
        padded_image = ImageOps.expand(scaled_image, (pad_x, pad_y, pad_x, pad_y), (0,0,0))
        return padded_image

def convert_to_png(image_path, output_folder):
    # Open the image and convert it to RGBA to support transparency
    image = Image.open(image_path).convert('RGBA')

    # Resize the image to fit inside the 720x720 bezel (if necessary)
    bezel_image = resize_to_fit_bezel(image)

    # Create a new 720x720 white background image
    bezel_size = 720
    new_image = Image.new('RGB', (bezel_size, bezel_size), (0,0,0))

    # Calculate the position to center the resized image within the bezel
    x_offset = (bezel_size - bezel_image.width) // 2
    y_offset = (bezel_size - bezel_image.height) // 2

    # Paste the resized image onto the bezel
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
    input_folder = "Jozi fotky"  # Replace with the path to your input folder
    output_folder = "upraveny_josi"  # Replace with the path to the output folder
    main(input_folder, output_folder)