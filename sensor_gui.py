#!/usr/bin/env python
# Graphical User Interface for the DHT sensor

# Imports
import time
import Adafruit_DHT
import serial
from Tkinter import *
sensor = Adafruit_DHT.DHT11 #DHT11/DHT22/AM2302
pin = 4

class Application(Frame):

	# Measure data from the sensor
	def measure(self):
                hum, temp = Adafruit_DHT.read_retry(sensor, pin)
		data = (str(temp) + "," + str(hum))
		# If the answer is not empty, process & display data
		if (data != ""):
			processed_data = data.split(",")

			self.hum_data.set(str(processed_data[1]))
			self.humidity.pack()
			
			self.temp_data.set("% Humedad:" )
			self.temperature.pack()

		# Wait 1 second between each measurement
		self.after(10000,self.measure)

	# Create display elements
	def createWidgets(self):

		self.humidity = Label(self, textvariable=self.hum_data, font=('Verdana', 230, 'bold'))
		self.hum_data.set("Humidity")
		self.humidity.pack()
		
		self.temperature = Label(self, textvariable=self.temp_data, font=('Verdana', 40, 'bold'))
		self.temp_data.set("Temperature")
		self.temperature.pack()

	# Init the variables & start measurements
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.temp_data = StringVar()
		self.hum_data = StringVar()
		self.createWidgets()
		self.pack()
		self.measure()


# Create and run the GUI
root = Tk()
root.attributes('-fullscreen', True)
app = Application(master=root)
app.mainloop()
