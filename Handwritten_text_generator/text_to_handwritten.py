import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

def text_to_handwritten(text, font_path="Pacifico-Regular.ttf", output_path="output.png"):
    font_path = os.path.join(os.path.dirname(__file__), font_path)
    font_size = 40
    max_width = 800
    margin = 20

    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"Font file not found at: {font_path}")
        return

    # Wrap text to fit image width
    wrapper = textwrap.TextWrapper(width=40)
    wrapped_text = wrapper.fill(text)

    # Calculate height dynamically using getbbox
    lines = wrapped_text.count('\n') + 1
    bbox = font.getbbox("A")
    line_height = (bbox[3] - bbox[1]) + 10  # height + line spacing
    height = margin * 2 + lines * line_height

    # Create image
    img = Image.new("RGB", (max_width, height), color="white")
    draw = ImageDraw.Draw(img)
    draw.text((margin, margin), wrapped_text, fill="black", font=font)

    # Save image
    img.save(output_path)
    print(f"✅ Image saved as '{output_path}'")

# Run the function
if __name__ == "__main__":
    user_input = input("Enter text to convert to handwritten: ")
    text_to_handwritten(user_input)
