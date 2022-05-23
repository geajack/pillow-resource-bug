import importlib.resources
from PIL import Image, ImageFont, ImageDraw

if __name__ == "__main__":
    with importlib.resources.path("font_demo", "OpenSans-Regular.ttf") as path:
        pil_image = Image.new("RGB", (200, 100))
        text_artist = ImageDraw.Draw(pil_image)
        font = ImageFont.truetype(str(path), 30)
        text_artist.text(
            (10, 10),
            "Hello, world!",
            font=font,
            fill=(0, 255, 0)
        )
    pil_image.show()