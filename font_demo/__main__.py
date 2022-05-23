import importlib.resources
from PIL import ImageFont
from PIL import _imagingft as core


if __name__ == "__main__":
    with importlib.resources.path("font_demo", "OpenSans-Regular.ttf") as path:
        font = core.getfont(
            str(path),
            30,
            0,
            "",
            layout_engine=ImageFont.Layout.BASIC
        )
        