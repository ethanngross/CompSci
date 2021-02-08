#   encode.py
#   Note this will not run in the code editor and must be downloaded
import tkinter as tk
import turtle as trtl
from PIL import ImageGrab, Image, ImageDraw
#message that is going to be encoded
message = input("Enter message: ") # Change this to encode a different message. Length limit 20 characters.
str(message)
#take in message and seperate characters into different ints from ascii chart
characters_as_ints = []
for cha in message:
  characters_as_ints.append(ord(cha))
print(characters_as_ints)
#take in ints and store in array as bytes
characters_as_bits = []
for integ in characters_as_ints:
  characters_as_bits.append('{0:08b}'.format(integ))
print(characters_as_bits)
#sperate each byte into bits in an array
bits_as_ints = []
for index in range(0,len(characters_as_bits)):
  for bit in characters_as_bits[index]:
    bits_as_ints.append(bit)
print(bits_as_ints)
#create turtle
screen = trtl.getscreen()
drawer = trtl.Turtle()
#set up turtle 
drawer.penup()
drawer.goto(-200,221)
drawer.shape("square")
drawer.color("green")
#draw out the picture according to the message entered
message_length = len(bits_as_ints)
index = 0
while index < message_length:
  if index % 8 == 0:
    drawer.goto(-200, drawer.ycor()-21)
  if bits_as_ints[index]=='1':
    drawer.stamp()
  drawer.forward(21)
  index = index + 1
#more screen setup
screen = drawer.getscreen()
root = trtl.getcanvas().winfo_toplevel()

# draw the message instead of taking a screenshot for macOS users
def draw_message(im_size, x, y):
    im = Image.new("RGBA", im_size, (255,255,255,0))
    draw = ImageDraw.Draw(im)
    message_length = len(bits_as_ints)
    index = 0
    while index < message_length:
      if index % 8 == 0:
        x = im_size[0]/2-200-10.5
        y += 21
      if bits_as_ints[index]=='1':
        draw.rectangle([x,y,x+21,y+21], fill="blue") #stamp
      x += 21
      index = index + 1
    im.save("macOutput.gif")
#creates a screenshot of the encoded code
def create_image(widget):
    x=root.winfo_rootx()
    y=root.winfo_rooty()
    x1=x+widget.window_width()
    y1=y+widget.window_height()
    im = ImageGrab.grab().crop((x,y,x1,y1))
    im.save("output.gif")
    print(im.size)

    # create an image for macOS users
    draw_message(im.size,im.size[0]/2-200-10.5,im.size[1]/2-221-10.5) # (149.5,98) in ImageDraw is equivalent to (205,275) in PIL 


create_image(screen)

#screen.mainloop()