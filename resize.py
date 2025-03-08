from PIL import Image
from pathlib import Path

def resize_image(input_file, output_dir, new_size, quality=95):
    """
    Resize an image to specified dimensions.
    
    Args:
        input_file (str): Path to the image file
        output_dir (str): Resized files directory
        new_size (tuple): New dimensions as (width, height)
        quality (int): Quality of the new image
        
    Returns:
        None
    """

    try:
        file = Path(input_file)
        name = file.parts[-1]

        # Open the image file
        with Image.open(file) as img:
            print(f"Original size: {img.size}")
            
            # Resize the image
            resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Save the resized image
            new_file = f"resized_{name}"
            output_file = Path(output_dir, new_file)
            resized_img.save(output_file, 'JPEG', quality=quality)
            
            print(f"New size: {resized_img.size}")
            print(f"Resized image saved as: {output_file}")
            
    except FileNotFoundError:
        print(f"Error: Could not find image file '{input_file}'")
    except ValueError as e:
        if "Invalid quality" in str(e):
            print("Error: Quality must be between 1 and 95")
        else:
            print(f"An error occurred: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
