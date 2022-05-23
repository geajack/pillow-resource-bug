import importlib.resources
from PIL import Image, ImageFont, ImageDraw
from PIL import _imagingft as core

class Font:

    def __init__(self, path):
        self.font = core.getfont(
            str(path),
            30,
            0,
            "",
            layout_engine=ImageFont.Layout.BASIC
        )

if __name__ == "__main__":
    with importlib.resources.path("font_demo", "OpenSans-Regular.ttf") as path:
        font = Font(path)
        