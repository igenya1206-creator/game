from PIL import Image, ImageDraw, ImageFont

W, H = 800, 1600

def font(size):
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
    except Exception:
        return ImageFont.load_default()

def label(draw, text, y, size=34, color=(255, 255, 255, 230)):
    f = font(size)
    bbox = draw.textbbox((0, 0), text, font=f)
    w = bbox[2] - bbox[0]
    draw.text(((W - w) / 2, y), text, font=f, fill=color)

def base_layer():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    skin = (232, 179, 154, 255)
    shadow = (196, 132, 109, 255)
    # head
    d.ellipse([320, 60, 480, 240], fill=skin)
    # neck
    d.rectangle([370, 220, 430, 280], fill=skin)
    # torso
    d.rounded_rectangle([300, 280, 500, 620], radius=60, fill=skin, outline=shadow, width=4)
    # hips
    d.rounded_rectangle([280, 600, 520, 780], radius=70, fill=skin, outline=shadow, width=4)
    # legs
    d.rounded_rectangle([310, 760, 400, 1420], radius=40, fill=skin, outline=shadow, width=4)
    d.rounded_rectangle([400, 760, 490, 1420], radius=40, fill=skin, outline=shadow, width=4)
    # arms
    d.rounded_rectangle([190, 300, 300, 700], radius=40, fill=skin, outline=shadow, width=4)
    d.rounded_rectangle([500, 300, 610, 700], radius=40, fill=skin, outline=shadow, width=4)
    # underwear (simple placeholder shapes)
    ub = (255, 255, 255, 90)
    d.rounded_rectangle([320, 330, 480, 430], radius=20, fill=ub)
    d.rounded_rectangle([300, 620, 500, 740], radius=30, fill=ub)
    label(d, "BASE / UNDERWEAR", 1460, 30, (124, 224, 255, 255))
    label(d, "(placeholder)", 1500, 22, (200, 200, 200, 200))
    return img

def hair_layer(name, twin=False):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    hair = (40, 26, 20, 255)
    # back hair
    if twin:
        d.rounded_rectangle([300, 40, 500, 260], radius=60, fill=hair)
        d.rounded_rectangle([190, 200, 270, 620], radius=40, fill=hair)
        d.rounded_rectangle([530, 200, 610, 620], radius=40, fill=hair)
    else:
        d.rounded_rectangle([290, 30, 510, 560], radius=70, fill=hair)
    # front bangs
    d.rounded_rectangle([310, 55, 490, 150], radius=30, fill=hair)
    label(d, f"HAIR: {name.upper()}", 1460, 30, (124, 224, 255, 255))
    label(d, "(placeholder)", 1500, 22, (200, 200, 200, 200))
    return img

def costume_layer(name, top_color, skirt_color, sock=False):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # top
    d.rounded_rectangle([280, 270, 520, 630], radius=60, fill=top_color)
    d.rounded_rectangle([180, 290, 310, 700], radius=40, fill=top_color)
    d.rounded_rectangle([490, 290, 620, 700], radius=40, fill=top_color)
    # skirt (fixed length)
    d.rounded_rectangle([270, 600, 530, 980], radius=40, fill=skirt_color)
    if sock:
        d.rounded_rectangle([305, 1150, 405, 1420], radius=20, fill=(255, 255, 255, 220))
        d.rounded_rectangle([395, 1150, 495, 1420], radius=20, fill=(255, 255, 255, 220))
    label(d, f"COSTUME: {name.upper()}", 1460, 30, (124, 224, 255, 255))
    label(d, "(placeholder)", 1500, 22, (200, 200, 200, 200))
    return img

base_layer().save("/tmp/costume-app/assets/base/underwear.png")
hair_layer("default").save("/tmp/costume-app/assets/hair/default.png")
hair_layer("twin", twin=True).save("/tmp/costume-app/assets/hair/twin.png")
costume_layer("school", (35, 46, 74, 255), (26, 45, 77, 255), sock=True).save("/tmp/costume-app/assets/costume/school.png")
costume_layer("nurse", (255, 255, 255, 255), (243, 246, 251, 255)).save("/tmp/costume-app/assets/costume/nurse.png")
costume_layer("maid", (17, 17, 17, 255), (21, 21, 21, 255)).save("/tmp/costume-app/assets/costume/maid.png")

print("done")
