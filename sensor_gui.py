#Humidity and Temperature Reader for Honeywell Sensors
# Graphical User Interface for the Honeywell humidity sensors HIH####

# Imports
import time
import subprocess
from Tkinter import *

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

			self.hum_data.set(str(processed_data[0]))
                        self.humidity.pack()

                        self.label_data.set("% Humedad:")
                        self.label.pack()

                        self.temp_data.set("Temperatura: " + str(processed_data[1]) + " C")
                        self.temperature.pack()
                
		# Wait time in milliseconds between each measurement
		self.after(30000,self.measure)

	# Create display elements
	def createWidgets(self):

                self.label = Label(self, textvariable=self.label_data, font=('Verdana', 40, 'bold'))
                self.label.pack()
		
		self.humidity = Label(self, textvariable=self.hum_data, background='red', foreground='yellow', font=('Verdana', 240, 'bold'))
#                self.humidity = Label(self, textvariable=self.hum_data,  font=('Verdana', 240, 'bold'))
		self.humidity.pack()                

                self.temperature = Label(self, textvariable=self.temp_data, font=('Verdana', 30))
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
