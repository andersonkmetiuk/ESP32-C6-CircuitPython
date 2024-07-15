import time
import neopixel
import board
import sys, os

def cycleNeopixel(wait):
    print("RED")
    for r in range(255):
        pixel[0] = (r, 0, 0)
        time.sleep(wait)
    for r in range(255, 0, -1):
        pixel[0] = (r, 0, 0)
        time.sleep(wait)
        
    print("GREEN")
    for g in range(255):
        pixel[0] = (0, g, 0)
        time.sleep(wait)
    for g in range(255, 0, -1):
        pixel[0] = (0, g, 0)
        time.sleep(wait)
        
    print("BLUE")
    for b in range(255):
        pixel[0] = (0, 0, b)
        time.sleep(wait)
    for b in range(255, 0, -1):
        pixel[0] = (0, 0, b)
        time.sleep(wait)
        
print("=========================================")
print("CircuitPython NeoPixel exercise")
print("to control onboard RGB NeoPixel")
print("-----------------------------------------")
print(sys.implementation[0], os.uname()[3],
      "\nrun on", os.uname()[4])
print(neopixel.__name__, neopixel.__version__)
print("board.NEOPIXEL: ", board.NEOPIXEL)
print("=========================================")
print()

# Create the NeoPixel object
pixel = neopixel.NeoPixel(board.NEOPIXEL,
                          1,
                          pixel_order=neopixel.GRB)
pixel[0] = (0, 0, 0)
time.sleep(2.0)

cycleNeopixel(0.005)

pixel[0] = (0, 0, 0)
time.sleep(2.0)

print("- bye -\n")