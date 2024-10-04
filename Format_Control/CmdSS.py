from PIL import Image, ImageDraw, ImageFont


class ScreenShotOutput:

    def __init__(self):
        """
        Use only create_command_image
        """
        pass

    def read_ouput(self):
        text = ""
        with open("output.txt", "r") as f:
            text = f.read()
        return text



    def crop_image_from_bottom(self, img):
        """
        Function to crop the image to fit the text\n
        Used to crop from bottom
        """
        # Convert the image to grayscale
        grayscale_img = img.convert('L')
        
        # Get the bounding box of non-black pixels (content area)
        bbox = grayscale_img.getbbox()
        
        if bbox:
            # Crop only the bottom part based on the bounding box (+20 for buffer)
            left, top, right, bottom = 0, 0, img.width, bbox[3]+20
            img = img.crop((left, top, right, bottom))
        
        return img


    def create_command_image(self, user_name, file_name, output_image_path='command_image_final.png'):
        """
        Function to create an image with black background and user-defined text
        - user_name: Name of student
        - file_name: Name of C or CPP file
        """

        text = self.read_ouput()
        size = text.count('\n')

        # check os notebook
        # 20 size of font + 7.8 size of space (vertically)
        height = int(27.8 + (size * 27.8) + 27.8 + 27.8)

        print("height: ", height, "Size: ", size)


        img_width, img_height = 800, height
        background_color = (0, 0, 0)  # Black 
        text_color = (255, 255, 255)  # White 

        cmd_text = f"C:\\Users\\{user_name}>gcc {file_name}.c -o {file_name}.exe && {file_name}.exe\n{text}"

        # Create a new image with black background
        img = Image.new('RGB', (img_width, img_height), color=background_color)

        d = ImageDraw.Draw(img)

        # Load a font or use a default one
        try:
            font = ImageFont.truetype("CascadiaMono.ttf", 20)  # Command prompt font
        except Exception as e:
            print("Loading default Font\n\nexception....", e)
            font = ImageFont.load_default()

        # Position the text towards the top-left corner
        position = (10, 10) 

        # Add text to image
        d.text(position, cmd_text, fill=text_color, font=font)

        img = self.crop_image_from_bottom(img)

        
        img.save(output_image_path)
        print(f"Image saved as {output_image_path}")



if __name__ == "__main__":
    user_name = "manas-bisht"
    file_name = "matrix"

    # Generate the command-line image with the given user name and file name
    ScreenShotOutput().create_command_image(user_name, file_name)
