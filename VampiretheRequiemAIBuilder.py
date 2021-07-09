from PIL import Image, ImageDraw, ImageFont
import random

#hallway is 2*img.size[1]/24
#doorway is 2*img.size[1]/24
#doors are 350 px each way
#upperroom text height n1o1d4/2
#middleroom text height (n29o1d48-(n1o1d4+2*n1o1d24))/2+(n1o1d4+2*n1o1d24)
#lowerroom text height (n15o1d16-(n29o1d48+2*n1o1d24))/2+(n29o1d48+2*n1o1d24)

img = Image.new('RGB', (3072, 2048), color = (255, 255, 255))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 50)

lefthall = (img.size[0]/2)-(img.size[1]/24)
righthall = (img.size[0]/2)+(img.size[1]/24)
n11o1d16 = 11*img.size[1]/16
n15o1d16 = 15*img.size[1]/16
n3o0d8 = 3*img.size[0]/8
n5o0d8 = 5*img.size[0]/8
n1o1d4 = img.size[1]/4
n1p4o0d48 = 1.4*(img.size[0]/48)
n3o0d48 = 3*img.size[0]/48
n5o0d48 = 5*img.size[0]/48
n11o0d48 = 11*img.size[0]/48
n13o0d48 = 13*img.size[0]/48
n19o0d48 = 19*img.size[0]/48
n21o0d48 = 21*img.size[0]/48
n27o0d48 = 27*img.size[0]/48
n29o0d48 = 29*img.size[0]/48
n35o0d48 = 35*img.size[0]/48
n37o0d48 = 37*img.size[0]/48
n43o0d48 = 43*img.size[0]/48
n45o0d48 = 45*img.size[0]/48
n29o1d48 = 29*img.size[1]/48
n1o1d3 = img.size[1]/3
n1o1d24 = img.size[1]/24

middleroomtextheight = (n29o1d48-(n1o1d4+2*n1o1d24))/2+(n1o1d4+2*n1o1d24)
lowerroomtextheight = (n15o1d16-(n29o1d48+2*n1o1d24))/2+(n29o1d48+2*n1o1d24)

mb = "ur2" #can be ur1 ur2 ur3 ur4 ur5 ur6 lr1 lr2 lr3 lr4
cr = "ur3" #can be ur1 ur2 ur3 ur4 ur5 ur6 mr1 mr2 mr3 mr4 mr5 mr6 lr1 lr2 lr3 lr4

darray = [True, True, True, True, True, True,  True, True, True, True, True, True,  True, True, True, True, True, True,  True, True, True, True]
warray = [True, True, True, True, True, True,  True, True, True, True, True, True,  True, True, True, True, True, True,  True, True, True, True]

numur = [random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3)]
nummr = [random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3)]
numlr = [random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3)]

#beginning of exterior
draw.line((0, 0, img.size[0], 0), fill=256, width=25)
draw.line((0, 0, 0, n15o1d16), fill=256, width=25)
draw.line((img.size[0], 0, img.size[0], n15o1d16), fill=256, width=25)
draw.line((0, n15o1d16, n3o0d8, n15o1d16), fill=256, width=13)
draw.line((n5o0d8, n15o1d16, img.size[0], n15o1d16), fill=256, width=13)
draw.line((n3o0d8, n15o1d16, n3o0d8, img.size[1]), fill=256, width=13)
draw.line((n5o0d8, n15o1d16, n5o0d8, img.size[1]), fill=256, width=13)
#beginning of front door
draw.line((n3o0d8, img.size[1], 15*img.size[0]/32, img.size[1]), fill=256, width=25)
draw.line((17*img.size[0]/32, img.size[1], n5o0d8, img.size[1]), fill=256, width=25)
#end of front door
#end of exterior

#beginning of entryway
draw.line((n3o0d8, n11o1d16, n3o0d8, img.size[1]), fill=256, width=13)
draw.line((n5o0d8, n11o1d16, n5o0d8, img.size[1]), fill=256, width=13)
#entryway doorway
draw.line((n3o0d8, n11o1d16, 15*img.size[0]/32, n11o1d16), fill=256, width=13)
draw.line((17*img.size[0]/32, n11o1d16, n5o0d8, n11o1d16), fill=256, width=13)
#foyer
draw.text((img.size[0]/2-65, 27*img.size[1]/32), "Foyer", fill=256, font=font)
#end of entryway

#beginning of upper set of rooms
draw.line((0, n1o1d4, n3o0d48, n1o1d4), fill=256, width=13)
draw.line((n5o0d48, n1o1d4, img.size[0]/6, n1o1d4), fill=256, width=13)
draw.line((img.size[0]/6, 0, img.size[0]/6, n1o1d4), fill=256, width=13)
draw.line((img.size[0]/6, n1o1d4, n11o0d48, n1o1d4), fill=256, width=13)
draw.line((n13o0d48, n1o1d4, 2*img.size[0]/6, n1o1d4), fill=256, width=13)
draw.line((2*img.size[0]/6, 0, 2*img.size[0]/6, n1o1d4), fill=256, width=13)
draw.line((2*img.size[0]/6, n1o1d4, n19o0d48, n1o1d4), fill=256, width=13)
draw.line((n21o0d48, n1o1d4, 3*img.size[0]/6, n1o1d4), fill=256, width=13)
draw.line((3*img.size[0]/6, 0, 3*img.size[0]/6, n1o1d4), fill=256, width=13)
draw.line((3*img.size[0]/6, n1o1d4, n27o0d48, n1o1d4), fill=256, width=13)
draw.line((n29o0d48, n1o1d4, 4*img.size[0]/6, n1o1d4), fill=256, width=13)
draw.line((4*img.size[0]/6, 0, 4*img.size[0]/6, n1o1d4), fill=256, width=13)
draw.line((4*img.size[0]/6, n1o1d4, n35o0d48, n1o1d4), fill=256, width=13)
draw.line((n37o0d48, n1o1d4, 5*img.size[0]/6, n1o1d4), fill=256, width=13)
draw.line((5*img.size[0]/6, 0, 5*img.size[0]/6, n1o1d4), fill=256, width=13)
draw.line((5*img.size[0]/6, n1o1d4, n43o0d48, n1o1d4), fill=256, width=13)
draw.line((n45o0d48, n1o1d4, img.size[0], n1o1d4), fill=256, width=13)
#beginning of doors1-6
if darray[0]:
    draw.line((n3o0d48, n1o1d4, n5o0d48, n1o1d4+n1p4o0d48), fill=256, width=13)
if darray[1]:
    draw.line((n11o0d48, n1o1d4, n13o0d48, n1o1d4+n1p4o0d48), fill=256, width=13)
if darray[2]:
    draw.line((n19o0d48, n1o1d4, n21o0d48, n1o1d4+n1p4o0d48), fill=256, width=13)
if darray[3]:
    draw.line((n27o0d48, n1o1d4, n29o0d48, n1o1d4+n1p4o0d48), fill=256, width=13)
if darray[4]:
    draw.line((n35o0d48, n1o1d4, n37o0d48, n1o1d4+n1p4o0d48), fill=256, width=13)
if darray[5]:
    draw.line((n43o0d48, n1o1d4, n45o0d48, n1o1d4+n1p4o0d48), fill=256, width=13)
#end of doors1-6
#beginning of walls1-6
if warray[0]:
    draw.line((n3o0d48, n1o1d4, n5o0d48, n1o1d4), fill=256, width=13)
if warray[1]:
    draw.line((n11o0d48, n1o1d4, n13o0d48, n1o1d4), fill=256, width=13)
if warray[2]:
    draw.line((n19o0d48, n1o1d4, n21o0d48, n1o1d4), fill=256, width=13)
if warray[3]:
    draw.line((n27o0d48, n1o1d4, n29o0d48, n1o1d4), fill=256, width=13)
if warray[4]:
    draw.line((n35o0d48, n1o1d4, n37o0d48, n1o1d4), fill=256, width=13)
if warray[5]:
    draw.line((n43o0d48, n1o1d4, n45o0d48, n1o1d4), fill=256, width=13)
#end of walls1-6
#r1
if mb == "ur1":
    draw.text((75, n1o1d4/2), "Master Bedroom", fill=256, font=font)
elif cr == "ur1":
    draw.text((100, n1o1d4/2), "Common Room", fill=256, font=font)
else:
    if numur[0] == 0:
        draw.text((150, n1o1d4/2), "Bedroom", fill=256, font=font)
    elif numur[0] == 1:
        draw.text((130, n1o1d4/2), "Coffinroom", fill=256, font=font)
    elif numur[0] == 2:
        draw.text((100, n1o1d4/2), "Common Room", fill=256, font=font)
    elif numur[0] ==3:
        draw.text((140, n1o1d4/2), "Washroom", fill=256, font=font)
#r2
if mb == "ur2":
    draw.text((75+img.size[0]/6, n1o1d4/2), "Master Bedroom", fill=256, font=font)
elif cr == "ur2":
    draw.text((100+img.size[0]/6, n1o1d4/2), "Common Room", fill=256, font=font)
else:
    if numur[1] == 0:
        draw.text((150+img.size[0]/6, n1o1d4/2), "Bedroom", fill=256, font=font)
    elif numur[1] == 1:
        draw.text((130+img.size[0]/6, n1o1d4/2), "Coffinroom", fill=256, font=font)
    elif numur[1] == 2:
        draw.text((100+img.size[0]/6, n1o1d4/2), "Common Room", fill=256, font=font)
    elif numur[1] ==3:
        draw.text((140+img.size[0]/6, n1o1d4/2), "Washroom", fill=256, font=font)
#r3
if mb == "ur3":
    draw.text((75+2*img.size[0]/6, n1o1d4/2), "Master Bedroom", fill=256, font=font)
elif cr == "ur3":
    draw.text((100+2*img.size[0]/6, n1o1d4/2), "Common Room", fill=256, font=font)
else:
    if numur[2] == 0:
        draw.text((150+2*img.size[0]/6, n1o1d4/2), "Bedroom", fill=256, font=font)
    elif numur[2] == 1:
        draw.text((130+2*img.size[0]/6, n1o1d4/2), "Coffinroom", fill=256, font=font)
    elif numur[2] == 2:
        draw.text((100+2*img.size[0]/6, n1o1d4/2), "Common Room", fill=256, font=font)
    elif numur[2] == 3:
        draw.text((140+2*img.size[0]/6, n1o1d4/2), "Washroom", fill=256, font=font)
#r4
if mb == "ur4":
    draw.text((75+3*img.size[0]/6, n1o1d4/2), "Master Bedroom", fill=256, font=font)
elif cr == "ur4":
    draw.text((100+3*img.size[0]/6, n1o1d4/2), "Common Room", fill=256, font=font)
else:
    if numur[3] == 0:
        draw.text((150+3*img.size[0]/6, n1o1d4/2), "Bedroom", fill=256, font=font)
    elif numur[3] == 1:
        draw.text((130+3*img.size[0]/6, n1o1d4/2), "Coffinroom", fill=256, font=font)
    elif numur[3] == 2:
        draw.text((100+3*img.size[0]/6, n1o1d4/2), "Common Room", fill=256, font=font)
    elif numur[3] ==3:
        draw.text((140+3*img.size[0]/6, n1o1d4/2), "Washroom", fill=256, font=font)
#r5
if mb == "ur5":
    draw.text((75+4*img.size[0]/6, n1o1d4/2), "Master Bedroom", fill=256, font=font)
elif cr == "ur5":
    draw.text((100+4*img.size[0]/6, n1o1d4/2), "Common Room", fill=256, font=font)
else:
    if numur[4] == 0:
        draw.text((150+4*img.size[0]/6, n1o1d4/2), "Bedroom", fill=256, font=font)
    elif numur[4] == 1:
        draw.text((130+4*img.size[0]/6, n1o1d4/2), "Coffinroom", fill=256, font=font)
    elif numur[4] == 2:
        draw.text((100+4*img.size[0]/6, n1o1d4/2), "Common Room", fill=256, font=font)
    elif numur[4] ==3:
        draw.text((140+4*img.size[0]/6, n1o1d4/2), "Washroom", fill=256, font=font)
#r6
if mb == "ur6":
    draw.text((75+5*img.size[0]/6, n1o1d4/2), "Master Bedroom", fill=256, font=font)
elif cr == "ur6":
    draw.text((100+5*img.size[0]/6, n1o1d4/2), "Common Room", fill=256, font=font)
else:
    if numur[5] == 0:
        draw.text((150+5*img.size[0]/6, n1o1d4/2), "Bedroom", fill=256, font=font)
    elif numur[5] == 1:
        draw.text((130+5*img.size[0]/6, n1o1d4/2), "Coffinroom", fill=256, font=font)
    elif numur[5] == 2:
        draw.text((100+5*img.size[0]/6, n1o1d4/2), "Common Room", fill=256, font=font)
    elif numur[6] ==3:
        draw.text((140+5*img.size[0]/6, n1o1d4/2), "Washroom", fill=256, font=font)
#end of upper set of rooms

#beginning of middle set of rooms it goes upper doorframe lower doorframe divider repeat
draw.line((0, n1o1d3, ((lefthall)/6)-(n1o1d24), n1o1d3), fill=256, width=13)
draw.line((((lefthall)/6)+(n1o1d24), n1o1d3, (lefthall)/3, n1o1d3), fill=256, width=13)

draw.line((0, n29o1d48, ((lefthall)/6)-(n1o1d24), n29o1d48), fill=256, width=13)
draw.line((((lefthall)/6)+(n1o1d24), n29o1d48, (lefthall)/3, n29o1d48), fill=256, width=13)

draw.line(((lefthall)/3, n1o1d3, (lefthall)/3, n29o1d48), fill=256, width=13)

draw.line((lefthall/3, n1o1d3, (lefthall/2)-(n1o1d24), n1o1d3), fill=256, width=13)
draw.line((((lefthall)/2)+(n1o1d24), n1o1d3, 2*(lefthall)/3, n1o1d3), fill=256, width=13)

draw.line((lefthall/3, n29o1d48, (lefthall/2)-(n1o1d24), n29o1d48), fill=256, width=13)
draw.line((((lefthall)/2)+(n1o1d24), n29o1d48, 2*(lefthall)/3, n29o1d48), fill=256, width=13)

draw.line((2*(lefthall)/3, n1o1d3, 2*(lefthall)/3, n29o1d48), fill=256, width=13)

draw.line((2*lefthall/3, n1o1d3, (5*lefthall/6)-(n1o1d24), n1o1d3), fill=256, width=13)
draw.line(((5*(lefthall)/6)+(n1o1d24), n1o1d3, (lefthall), n1o1d3), fill=256, width=13)

draw.line((2*lefthall/3, n29o1d48, (5*lefthall/6)-(n1o1d24), n29o1d48), fill=256, width=13)
draw.line(((5*(lefthall)/6)+(n1o1d24), n29o1d48, (lefthall), n29o1d48), fill=256, width=13)


draw.line((righthall, n1o1d3, ((lefthall)/6)-(n1o1d24)+(righthall), n1o1d3), fill=256, width=13)
draw.line((((lefthall)/6)+(n1o1d24)+(righthall), n1o1d3, (lefthall/3)+(righthall), n1o1d3), fill=256, width=13)

draw.line((righthall, n29o1d48, ((lefthall)/6)-(n1o1d24)+(righthall), n29o1d48), fill=256, width=13)
draw.line((((lefthall)/6)+(n1o1d24)+(righthall), n29o1d48, (lefthall/3)+(righthall), n29o1d48), fill=256, width=13)

draw.line((((lefthall)/3)+(righthall), n1o1d3, ((lefthall)/3)+(righthall), n29o1d48), fill=256, width=13)

draw.line((lefthall/3+(righthall), n1o1d3, (lefthall/2)-(n1o1d24)+(righthall), n1o1d3), fill=256, width=13)
draw.line((((lefthall)/2)+(n1o1d24)+(righthall), n1o1d3, 2*(lefthall)/3+(righthall), n1o1d3), fill=256, width=13)

draw.line((lefthall/3+(righthall), n29o1d48, (lefthall/2)-(n1o1d24)+(righthall), n29o1d48), fill=256, width=13)
draw.line((((lefthall)/2)+(n1o1d24)+(righthall), n29o1d48, 2*(lefthall)/3+(righthall), n29o1d48), fill=256, width=13)

draw.line(((2*(lefthall)/3)+(righthall), n1o1d3, (2*(lefthall)/3)+(righthall), n29o1d48), fill=256, width=13)

draw.line((2*lefthall/3+(righthall), n1o1d3, (5*lefthall/6)-(n1o1d24)+(righthall), n1o1d3), fill=256, width=13)
draw.line(((5*(lefthall)/6)+(n1o1d24)+(righthall), n1o1d3, (lefthall)+(righthall), n1o1d3), fill=256, width=13)

draw.line((2*lefthall/3+(righthall), n29o1d48, (5*lefthall/6)-(n1o1d24)+(righthall), n29o1d48), fill=256, width=13)
draw.line(((5*(lefthall)/6)+(n1o1d24)+(righthall), n29o1d48, (lefthall)+(righthall), n29o1d48), fill=256, width=13)
#beginning of upper doors1-6
if darray[6]:
    draw.line((((lefthall)/6)-(n1o1d24), n1o1d3, ((lefthall)/6)+(n1o1d24), n1o1d3-n1p4o0d48), fill=256, width=13)
if darray[7]:
    draw.line(((lefthall/2)-(n1o1d24), n1o1d3, (lefthall/2)+(n1o1d24), n1o1d3-n1p4o0d48), fill=256, width=13)
if darray[8]:
    draw.line(((5*lefthall/6)-(n1o1d24), n1o1d3, (5*lefthall/6)+(n1o1d24), n1o1d3-n1p4o0d48), fill=256, width=13)
if darray[9]:
    draw.line((((lefthall)/6)-(n1o1d24)+(righthall), n1o1d3, ((lefthall)/6)+(n1o1d24)+(righthall), n1o1d3-n1p4o0d48), fill=256, width=13)
if darray[10]:
    draw.line(((lefthall/2)-(n1o1d24)+(righthall), n1o1d3, (lefthall/2)+(n1o1d24)+(righthall), n1o1d3-n1p4o0d48), fill=256, width=13)
if darray[11]:
    draw.line(((5*lefthall/6)-(n1o1d24)+(righthall), n1o1d3, (5*lefthall/6)+(n1o1d24)+(righthall), n1o1d3-n1p4o0d48), fill=256, width=13)
#end of upper doors1-6
#beginning of upper walls1-6
if warray[6]:
    draw.line((((lefthall)/6)-(n1o1d24), n1o1d3, ((lefthall)/6)+(n1o1d24), n1o1d3), fill=256, width=13)
if warray[7]:
    draw.line(((lefthall/2)-(n1o1d24), n1o1d3, (lefthall/2)+(n1o1d24), n1o1d3), fill=256, width=13)
if warray[8]:
    draw.line(((5*lefthall/6)-(n1o1d24), n1o1d3, (5*lefthall/6)+(n1o1d24), n1o1d3), fill=256, width=13)
if warray[9]:
    draw.line((((lefthall)/6)-(n1o1d24)+(righthall), n1o1d3, ((lefthall)/6)+(n1o1d24)+(righthall), n1o1d3), fill=256, width=13)
if warray[10]:
    draw.line(((lefthall/2)-(n1o1d24)+(righthall), n1o1d3, (lefthall/2)+(n1o1d24)+(righthall), n1o1d3), fill=256, width=13)
if warray[11]:
    draw.line(((5*lefthall/6)-(n1o1d24)+(righthall), n1o1d3, (5*lefthall/6)+(n1o1d24)+(righthall), n1o1d3), fill=256, width=13)
#end of upper walls1-6
#beginning of lower doors1-6
if darray[12]:
    draw.line((((lefthall)/6)-(n1o1d24), n29o1d48, ((lefthall)/6)+(n1o1d24), n29o1d48+n1p4o0d48), fill=256, width=13)
if darray[13]:
    draw.line(((lefthall/2)-(n1o1d24), n29o1d48, (lefthall/2)+(n1o1d24), n29o1d48+n1p4o0d48), fill=256, width=13)
if darray[14]:
    draw.line(((5*lefthall/6)-(n1o1d24), n29o1d48, (5*lefthall/6)+(n1o1d24), n29o1d48+n1p4o0d48), fill=256, width=13)
if darray[15]:
    draw.line((((lefthall)/6)-(n1o1d24)+(righthall), n29o1d48, ((lefthall)/6)+(n1o1d24)+(righthall), n29o1d48+n1p4o0d48), fill=256, width=13)
if darray[16]:
    draw.line(((lefthall/2)-(n1o1d24)+(righthall), n29o1d48, (lefthall/2)+(n1o1d24)+(righthall), n29o1d48+n1p4o0d48), fill=256, width=13)
if darray[17]:
    draw.line(((5*lefthall/6)-(n1o1d24)+(righthall), n29o1d48, (5*lefthall/6)+(n1o1d24)+(righthall), n29o1d48+n1p4o0d48), fill=256, width=13)
#end of lower doors1-6
#beginning of lower walls1-6
if warray[12]:
    draw.line((((lefthall)/6)-(n1o1d24), n29o1d48, ((lefthall)/6)+(n1o1d24), n29o1d48), fill=256, width=13)
if warray[13]:
    draw.line(((lefthall/2)-(n1o1d24), n29o1d48, (lefthall/2)+(n1o1d24), n29o1d48), fill=256, width=13)
if warray[14]:
    draw.line(((5*lefthall/6)-(n1o1d24), n29o1d48, (5*lefthall/6)+(n1o1d24), n29o1d48), fill=256, width=13)
if warray[15]:
    draw.line((((lefthall)/6)-(n1o1d24)+(righthall), n29o1d48, ((lefthall)/6)+(n1o1d24)+(righthall), n29o1d48), fill=256, width=13)
if warray[16]:
    draw.line(((lefthall/2)-(n1o1d24)+(righthall), n29o1d48, (lefthall/2)+(n1o1d24)+(righthall), n29o1d48), fill=256, width=13)
if warray[17]:
    draw.line(((5*lefthall/6)-(n1o1d24)+(righthall), n29o1d48, (5*lefthall/6)+(n1o1d24)+(righthall), n29o1d48), fill=256, width=13)
#end of lower walls1-6
#r1
if cr == "mr1":
    draw.text((50, middleroomtextheight), "Common Room", fill=256, font=font)
else:
    if nummr[0] == 0:
        draw.text((75, middleroomtextheight), "Bedroom", fill=256, font=font)
    elif nummr[0] == 1:
        draw.text((65, middleroomtextheight), "Coffinroom", fill=256, font=font)
    elif nummr[0] == 2:
        draw.text((50, middleroomtextheight), "Common Room", fill=256, font=font)
    elif nummr[0] == 3:
        draw.text((70, middleroomtextheight), "Washroom", fill=256, font=font)
#r2
if cr == "mr2":
    draw.text((75+img.size[0]/6, middleroomtextheight), "Common Room", fill=256, font=font)
else:
    if nummr[1] == 0:
        draw.text((100+img.size[0]/6, middleroomtextheight), "Bedroom", fill=256, font=font)
    elif nummr[1] == 1:
        draw.text((100+img.size[0]/6, middleroomtextheight), "Coffinroom", fill=256, font=font)
    elif nummr[1] == 2:
        draw.text((75+img.size[0]/6, middleroomtextheight), "Common Room", fill=256, font=font)
    elif nummr[1] == 3:
        draw.text((105+img.size[0]/6, middleroomtextheight), "Washroom", fill=256, font=font)
#r3
if cr == "mr3":
    draw.text((30+2*img.size[0]/6, middleroomtextheight), "Common Room", fill=256, font=font)
else:
    if nummr[2] == 0:
        draw.text((80+2*img.size[0]/6, middleroomtextheight), "Bedroom", fill=256, font=font)
    elif nummr[2] == 1:
        draw.text((75+2*img.size[0]/6, middleroomtextheight), "Coffinroom", fill=256, font=font)
    elif nummr[2] == 2:
        draw.text((30+2*img.size[0]/6, middleroomtextheight), "Common Room", fill=256, font=font)
    elif nummr[2] == 3:
        draw.text((80+2*img.size[0]/6, middleroomtextheight), "Washroom", fill=256, font=font)
#r4
if cr == "mr4":
    draw.text((125+3*img.size[0]/6, middleroomtextheight), "Common Room", fill=256, font=font)
else:
    if nummr[3] == 0:
        draw.text((175+3*img.size[0]/6, middleroomtextheight), "Bedroom", fill=256, font=font)
    elif nummr[3] == 1:
        draw.text((150+3*img.size[0]/6, middleroomtextheight), "Coffinroom", fill=256, font=font)
    elif nummr[3] == 2:
        draw.text((125+3*img.size[0]/6, middleroomtextheight), "Common Room", fill=256, font=font)
    elif nummr[3] == 3:
        draw.text((160+3*img.size[0]/6, middleroomtextheight), "Washroom", fill=256, font=font)
#r5
if cr == "mr5":
    draw.text((100+4*img.size[0]/6, middleroomtextheight), "Common Room", fill=256, font=font)
else:
    if nummr[4] == 0:
        draw.text((150+4*img.size[0]/6, middleroomtextheight), "Bedroom", fill=256, font=font)
    elif nummr[4] == 1:
        draw.text((130+4*img.size[0]/6, middleroomtextheight), "Coffinroom", fill=256, font=font)
    elif nummr[4] == 2:
        draw.text((100+4*img.size[0]/6, middleroomtextheight), "Common Room", fill=256, font=font)
    elif nummr[4] == 3:
        draw.text((140+4*img.size[0]/6, middleroomtextheight), "Washroom", fill=256, font=font)
#r6
if cr == "mr6":
    draw.text((100+5*img.size[0]/6, middleroomtextheight), "Common Room", fill=256, font=font)
else:
    if nummr[5] == 0:
        draw.text((150+5*img.size[0]/6, middleroomtextheight), "Bedroom", fill=256, font=font)
    elif nummr[5] == 1:
        draw.text((130+5*img.size[0]/6, middleroomtextheight), "Coffinroom", fill=256, font=font)
    elif nummr[5] == 2:
        draw.text((100+5*img.size[0]/6, middleroomtextheight), "Common Room", fill=256, font=font)
    elif nummr[5] == 3:
        draw.text((140+5*img.size[0]/6, middleroomtextheight), "Washroom", fill=256, font=font)
#end of middle set of rooms

#beginning of lower set of rooms
draw.line((0, n11o1d16, img.size[0]/16, n11o1d16), fill=256, width=13)
draw.line((2*img.size[0]/16, n11o1d16, 3*img.size[0]/16, n11o1d16), fill=256, width=13)
draw.line((3*img.size[0]/16, n11o1d16, 3*img.size[0]/16, n15o1d16), fill=256, width=13)
draw.line((3*img.size[0]/16, n11o1d16, 4*img.size[0]/16, n11o1d16), fill=256, width=13)
draw.line((5*img.size[0]/16, n11o1d16, n3o0d8, n11o1d16), fill=256, width=13)


draw.line((10*img.size[0]/16, n11o1d16, 11*img.size[0]/16, n11o1d16), fill=256, width=13)
draw.line((12*img.size[0]/16, n11o1d16, 13*img.size[0]/16, n11o1d16), fill=256, width=13)
draw.line((13*img.size[0]/16, n11o1d16, 13*img.size[0]/16, n15o1d16), fill=256, width=13)
draw.line((13*img.size[0]/16, n11o1d16, 14*img.size[0]/16, n11o1d16), fill=256, width=13)
draw.line((15*img.size[0]/16, n11o1d16, img.size[0], n11o1d16), fill=256, width=13)
#beginning of doors1-4
if darray[18]:
    draw.line((img.size[0]/16, n11o1d16, 2*img.size[0]/16, n11o1d16-n1p4o0d48), fill=256, width=13)
if darray[19]:
    draw.line((4*img.size[0]/16, n11o1d16, 5*img.size[0]/16, n11o1d16-n1p4o0d48), fill=256, width=13)
if darray[20]:
    draw.line((11*img.size[0]/16, n11o1d16, 12*img.size[0]/16, n11o1d16-n1p4o0d48), fill=256, width=13)
if darray[21]:
    draw.line((14*img.size[0]/16, n11o1d16, 15*img.size[0]/16, n11o1d16-n1p4o0d48), fill=256, width=13)
#end of doors1-4
#beginning of walls1-4
if warray[18]:
    draw.line((img.size[0]/16, n11o1d16, 2*img.size[0]/16, n11o1d16), fill=256, width=13)
if warray[19]:
    draw.line((4*img.size[0]/16, n11o1d16, 5*img.size[0]/16, n11o1d16), fill=256, width=13)
if warray[20]:
    draw.line((11*img.size[0]/16, n11o1d16, 12*img.size[0]/16, n11o1d16), fill=256, width=13)
if warray[21]:
    draw.line((14*img.size[0]/16, n11o1d16, 15*img.size[0]/16, n11o1d16), fill=256, width=13)
#end of walls1-4
#r1
if mb == "lr1":
    draw.text((75, lowerroomtextheight), "Master Bedroom", fill=256, font=font)
elif cr == "lr1":
    draw.text((100, lowerroomtextheight), "Common Room", fill=256, font=font)
else:
    if numlr[0] == 0:
        draw.text((150, lowerroomtextheight), "Bedroom", fill=256, font=font)
    elif numlr[0] == 1:
        draw.text((130, lowerroomtextheight), "Coffinroom", fill=256, font=font)
    elif numlr[0] == 2:
        draw.text((100, lowerroomtextheight), "Common Room", fill=256, font=font)
    elif numlr[0] == 3:
        draw.text((140, lowerroomtextheight), "Washroom", fill=256, font=font)
#r2
if mb == "lr2":
    draw.text((125+img.size[0]/6, lowerroomtextheight), "Master Bedroom", fill=256, font=font)
elif cr == "lr2":
    draw.text((150+img.size[0]/6, lowerroomtextheight), "Common Room", fill=256, font=font)
else:
    if numlr[1] == 0:
        draw.text((200+img.size[0]/6, lowerroomtextheight), "Bedroom", fill=256, font=font)
    elif numlr[1] == 1:
        draw.text((180+img.size[0]/6, lowerroomtextheight), "Coffinroom", fill=256, font=font)
    elif numlr[1] == 2:
        draw.text((150+img.size[0]/6, lowerroomtextheight), "Common Room", fill=256, font=font)
    elif numlr[1] == 3:
        draw.text((190+img.size[0]/6, lowerroomtextheight), "Washroom", fill=256, font=font)
#r3
if mb == "lr3":
    draw.text((4*img.size[0]/6, lowerroomtextheight), "Master Bedroom", fill=256, font=font)
elif cr == "lr3":
    draw.text((4*img.size[0]/6, lowerroomtextheight), "Common Room", fill=256, font=font)
else:
    if numlr[2] == 0:
        draw.text((50+4*img.size[0]/6, lowerroomtextheight), "Bedroom", fill=256, font=font)
    elif numlr[2] == 1:
        draw.text((30+4*img.size[0]/6, lowerroomtextheight), "Coffinroom", fill=256, font=font)
    elif numlr[2] == 2:
        draw.text((4*img.size[0]/6, lowerroomtextheight), "Common Room", fill=256, font=font)
    elif numlr[2] == 3:
        draw.text((40+4*img.size[0]/6, lowerroomtextheight), "Washroom", fill=256, font=font)
#r4
if mb == "lr4":
    draw.text((100+5*img.size[0]/6, lowerroomtextheight), "Master Bedroom", fill=256, font=font)
elif cr == "lr4":
    draw.text((125+5*img.size[0]/6, lowerroomtextheight), "Common Room", fill=256, font=font)
else:
    if numlr[3] == 0:
        draw.text((150+5*img.size[0]/6, lowerroomtextheight), "Bedroom", fill=256, font=font)
    elif numlr[3] == 1:
        draw.text((130+5*img.size[0]/6, lowerroomtextheight), "Coffinroom", fill=256, font=font)
    elif numlr[3] == 2:
        draw.text((100+5*img.size[0]/6, lowerroomtextheight), "Common Room", fill=256, font=font)
    elif numlr[3] == 3:
        draw.text((140+5*img.size[0]/6, lowerroomtextheight), "Washroom", fill=256, font=font)
#end of lower set of rooms

# #beginning of vert hallway
draw.line((lefthall, n1o1d3, lefthall, n29o1d48), fill=256, width=13)
draw.line((righthall, n1o1d3, righthall, n29o1d48), fill=256, width=13)
# #end of vert hallway

img.save('layout.png')
