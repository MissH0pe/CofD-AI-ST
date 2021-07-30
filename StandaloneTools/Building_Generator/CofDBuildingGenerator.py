from PIL import Image, ImageDraw, ImageFont
import sys
# import random

def genlwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
    draw.line((x * imgsizex / xroomsf, y * imgsizey / yroomsf, x * imgsizex / xrooms, (y + 1) * imgsizey / yrooms), fill=256, width=innerlinewidthf)

def genrwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
    draw.line(((x+1) * imgsizex / xroomsf, y * imgsizey / yroomsf, (x+1) * imgsizex / xrooms, (y + 1) * imgsizey / yrooms), fill=256, width=innerlinewidthf)

def gentwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
    draw.line((x * imgsizex / xroomsf, y * imgsizey / yroomsf, (x+1) * imgsizex / xrooms, y * imgsizey / yrooms), fill=256, width=innerlinewidthf)

def genbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
    draw.line((x * imgsizex / xroomsf, (y+1) * imgsizey / yroomsf, (x+1) * imgsizex / xrooms, (y + 1) * imgsizey / yrooms), fill=256, width=innerlinewidthf)

# def gentlwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
#     gentwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genlwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#
# def gentrwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
#     gentwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genrwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#
# def gentbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
#     gentwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#
# def genlrwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
#     genlwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genrwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#
# def genlbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
#     genlwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#
# def gerbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
#     genrwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#
# def gentlrwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
#     gentwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genlwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genrwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#
# def gentlbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
#     gentwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genlwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#
# def genlrbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
#     genlwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genrwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#
# def gentrbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
#     gentwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genrwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#
# def gentlrbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
#     gentwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genlwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genrwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)
#     genbwall(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf)

def genldoor(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
    draw.line((x * imgsizex / xroomsf, y * imgsizey / yroomsf, x * imgsizex / xrooms, (y + 0.3333) * imgsizey / yrooms), fill=256, width=innerlinewidthf)
    draw.line((x * imgsizex / xroomsf, (y + 0.6667) * imgsizey / yroomsf, x * imgsizex / xrooms, (y + 1) * imgsizey / yrooms), fill=256, width=innerlinewidthf)

def genrdoor(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
    draw.line(((x+1) * imgsizex / xroomsf, y * imgsizey / yroomsf, (x+1) * imgsizex / xrooms, (y + 0.3333) * imgsizey / yrooms), fill=256, width=innerlinewidthf)
    draw.line(((x+1) * imgsizex / xroomsf, (y + 0.6667) * imgsizey / yroomsf, (x+1) * imgsizex / xrooms, (y + 1) * imgsizey / yrooms), fill=256, width=innerlinewidthf)

def gentdoor(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
    draw.line((x * imgsizex / xroomsf, y * imgsizey / yroomsf, (x + 0.3333) * imgsizex / xrooms, y * imgsizey / yrooms), fill=256, width=innerlinewidthf)
    draw.line(((x + 0.6667) * imgsizex / xroomsf, y * imgsizey / yroomsf, (x+1) * imgsizex / xrooms, y * imgsizey / yrooms), fill=256, width=innerlinewidthf)

def genbdoor(x, y, xroomsf, yroomsf, imgsizex, imgsizey, outerlinewidthf, innerlinewidthf):
    draw.line((x * imgsizex / xroomsf, (y+1) * imgsizey / yroomsf, (x + 0.3333) * imgsizex / xrooms, (y+1) * imgsizey / yrooms), fill=256, width=innerlinewidthf)
    draw.line(((x + 0.6667) * imgsizex / xroomsf, (y+1) * imgsizey / yroomsf, (x+1) * imgsizex / xrooms, (y+1) * imgsizey / yrooms), fill=256, width=innerlinewidthf)

xdim = int(sys.argv[1])
ydim = int(sys.argv[2])

xrooms = int(sys.argv[3])
yrooms = int(sys.argv[4])

filename = sys.argv[5]
extension = sys.argv[6]

linewidthmod = int(sys.argv[7])

outerlinewidth = int((((xdim + ydim) / 2) / 50) * linewidthmod)
innerlinewidth = int(outerlinewidth / 2)

img = Image.new('RGB', (xdim, ydim), color = (255, 255, 255))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 50)

genbdoor(0, 0, xrooms, yrooms, img.size[0], img.size[1], outerlinewidth, innerlinewidth)
# gentlrbwall(1, 0, xrooms, yrooms, img.size[0], img.size[1], outerlinewidth, innerlinewidth)

img.save(filename+'.'+extension)
