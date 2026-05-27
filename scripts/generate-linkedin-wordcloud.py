from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "images"
ASSET_OUT = ROOT / "src" / "content" / "assets"

FONT_BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


def main() -> None:
    image = Image.new("RGBA", (1600, 900), "#f8f7f2")
    draw = ImageDraw.Draw(image)

    ink = "#101217"
    muted = "#5f6772"
    red = "#ff4d3d"
    green = "#10b981"
    yellow = "#facc15"
    blue = "#0a66c2"

    draw.rectangle((70, 78, 1530, 822), fill=ink)
    draw.rectangle((112, 120, 1488, 216), fill="#f8f7f2")
    draw.ellipse((144, 150, 180, 186), fill=red)
    draw.ellipse((200, 150, 236, 186), fill=green)
    draw.ellipse((256, 150, 292, 186), fill=yellow)
    draw.text((1240, 147), "r/LinkedInLunatics", font=font(FONT_BOLD, 25), fill=muted)
    draw.rectangle((112, 248, 1488, 780), fill="#f8f7f2")

    draw.text((185, 304), "Hustle", font=font(FONT_BLACK, 132), fill=blue)
    draw.text((775, 304), "Founder", font=font(FONT_BLACK, 106), fill=ink)
    draw.text((254, 500), "Leadership", font=font(FONT_BLACK, 116), fill=red)
    draw.text((930, 492), "CEO", font=font(FONT_BLACK, 126), fill=green)
    draw.text((612, 646), "Mindset", font=font(FONT_BLACK, 76), fill=ink)
    draw.text((970, 264), "authentic", font=font(FONT_BLACK, 54), fill=yellow)
    draw.text((148, 292), "synergy", font=font(FONT_BOLD, 44), fill=muted)
    draw.text((1050, 682), "disruption", font=font(FONT_BOLD, 42), fill=muted)
    draw.text((160, 684), "lessons", font=font(FONT_BOLD, 38), fill=muted)

    rotated_growth = Image.new("RGBA", (180, 64), (255, 255, 255, 0))
    growth_draw = ImageDraw.Draw(rotated_growth)
    growth_draw.text((0, 0), "growth", font=font(FONT_BOLD, 36), fill=muted)
    image.alpha_composite(rotated_growth.rotate(90, expand=True), (124, 450))

    rotated_grindset = Image.new("RGBA", (220, 64), (255, 255, 255, 0))
    grind_draw = ImageDraw.Draw(rotated_grindset)
    grind_draw.text((0, 0), "grindset", font=font(FONT_BOLD, 42), fill=muted)
    image.alpha_composite(rotated_grindset.rotate(90, expand=True), (1250, 440))

    draw.rectangle((176, 474, 506, 490), fill=yellow)
    draw.rectangle((700, 645, 910, 659), fill=green)
    draw.rectangle((1128, 482, 1348, 496), fill=red)

    OUT.mkdir(parents=True, exist_ok=True)
    ASSET_OUT.mkdir(parents=True, exist_ok=True)

    image.save(OUT / "linkedin_lunatics_wordcloud.png")
    image.save(OUT / "linkedin-wordcloud.png")
    image.save(ASSET_OUT / "linkedin_lunatics_wordcloud.png")


if __name__ == "__main__":
    main()
