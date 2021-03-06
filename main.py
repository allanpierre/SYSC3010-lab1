from sense_hat import SenseHat
import time
import sense_hat

"""

  Sense HAT Sensors Display
  
  Select Temperature, Pressure, or Humidity  with the Joystick
  to visualize the current sensor values on the LED.
  
  Note: Requires sense_hat 2.2.0 or later

"""

sense = SenseHat()

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)


def show_first():
  sense.show_letter("A", back_colour = blue)
  time.sleep(.5)

def show_last():
  sense.show_letter("P", back_colour = green)
  time.sleep(.5)

def update_screen(mode, show_letter = False):
  if mode == "temp":
    if show_letter:
      show_t()
    pixels = [white for i in range(64)]

  elif mode == "pressure":
    if show_letter:
      show_p()
    pixels = [white for i in range(64)]


  sense.set_pixels(pixels)

####
# Intro Animation
####

up_key = sense_hat.DIRECTION_UP
pressed = sense_hat.ACTION_PRESSED

if events:
    for e in events:
      debug_message("Processing joystick events")
      if e.direction ==  up_key and e.action == pressed:
        # User pressed up: move bird up and columns over
        debug_message("Joystick up press detected")
        show_first()
       
  else:
    moved = False

show_last()

update_screen("temp")

index = 0
sensors = ["temp", "pressure", "humidity"]

####
# Main game loop
####

up_key = sense_hat.DIRECTION_UP
pressed = sense_hat.ACTION_PRESSED

while True:
  selection = False
  events = sense.stick.get_events()
  for event in events:
    # Skip releases
    if event.action != "released":
      if event.direction == "left":
        index -= 1
        selection = True
      elif event.direction == "right":
        index += 1
        selection = True
      if selection:
        current_mode = sensors[index % 3]
        update_screen(current_mode, show_letter = True)
  
  if not selection:      
    current_mode = sensors[index % 3]
    update_screen(current_mode)
