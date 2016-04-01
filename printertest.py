from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

printer.println("Your printer can print one line")
printer.println("and anouther, it works!")
printer.println("It doesn't really need to do")
printer.println("anything else for this totorial")
printer.println("but if you want, you can find a more complete demo at:")
printer.println("https://github.com/adafruit/Python-Thermal-Printer")
printer.println("the printertest.py there shows all the features of the printer")
printer.println("including printing barcodes and qr codes.")
printer.println("for a totorial on adafruit's github go to ")
printer.println("https://learn.adafruit.com/pi-thermal-printer/overview")
printer.println("")
printer.println("One last thing in order to show everything you've printed you need to print a few blank lines: ")
printer.println("")
printer.println("you can also use the button to")
printer.println("dispense extra paper to see all you've printed")
printer.println("That's all,")
printer.println("Bye.")
printer.println("")