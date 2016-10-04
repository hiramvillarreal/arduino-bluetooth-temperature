# Humidity and Temperature Reader for Honeywell Sensors
# Graphical User Interface for the Honeywell humidity sensors HIH####

# Imports
import time
import subprocess
from Tkinter import *
limit = 45  # Humidity porcentage limit to display a red background and yellow text label
wait = 180000 # Wait time in milliseconds between each measurement
# Main Tkinter application
class Application(Frame):

	# Measure data from the sensor
	def measure(self):

		# Request data and read the answer. Call the Honeywell script at home directory, the original C file was modified to output like: (32,32) hum,temp.
		output = subprocess.Popen(['/home/pi/i2cHoneywellHumidity/i2cHoneywellHumidity'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                data =  output.communicate()[0]

		# If the answer is not empty, process & display data
		if (data != ""):
			processed_data = data.split(",")

			if (float(processed_data[0]) > 100): #Some times the sensor gives an error value  > 100 this reload the function until get a correct read			
				self.after(wait,self.measure)

                        self.label_data.set( "% Humedad:")
                        self.label.pack()

			self.hum_data.set(str(processed_data[0]))
			#condition to set the humidity text and background color based oon "limit" variable

			if (float(processed_data[0]) > limit):
				self.humidity.configure(bg = 'red', foreground='yellow')
			else:
			        self.humidity.configure(bg = '#d9d9d9', foreground='black')

                        self.humidity.pack()

                        self.temp_data.set("Temperatura: " + str(processed_data[1]) + " C")
                        self.temperature.pack()
                

		self.after(wait,self.measure)

	# Create display elements
	def createWidgets(self):

                self.label = Label(self, textvariable=self.label_data, font=('Verdana', 70, 'bold'))
                self.label.pack()
		
                self.humidity = Label(self, textvariable=self.hum_data,  font=('Verdana', 480, 'bold'))
		self.humidity.pack()                

                self.temperature = Label(self, textvariable=self.temp_data, font=('Verdana',70, 'bold'))
                self.temperature.pack()


	# Init the variables & start measurements
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.temp_data = StringVar()
		self.hum_data = StringVar()
                self.label_data = StringVar()
		self.createWidgets()
		self.pack()
		self.measure()

# Create and run the GUI
root = Tk()
root.attributes('-fullscreen', True) #Comment this to disable fullscreen display
app = Application(master=root)
app.mainloop()
