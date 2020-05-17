import tkinter as tk
import requests
from tkinter import font

def getWeather(city) :
    apiKey = '8233ee406d8a49ed7163013ed6f90527'
    #api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
    url = 'https://api.openweathermap.org/data/2.5/weather'
    search = {'APPID': apiKey, 'q': city, 'units': 'metric'}
    try :
        response = requests.get(url, search)
        weather = response.json()

        output = []
        name = weather['name'] + " " + weather['sys']['country']
        status = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        windspeed = weather['wind']['speed']
        humidity = weather['main']['humidity']
        pressure = weather['main']['pressure']

        output.append(name)
        output.append(status)
        output.append(temperature)
        output.append(windspeed)
        output.append(humidity)
        output.append(pressure)
    except :
        output = []

    formattedOutput(output)

def formattedOutput(output) :
    try :
        text = "Weather status in : " + output[0] + "\n conditions : " + output[1] + "\ntemperature : " + str(output[2]) + "C"
        text += "\nwind speed : " + str(output[3]) + "m/sec\n" + "pressure : " + str(output[5]) + "mBar\n" + "humidity : " + str(output[4]) + "%\n" 
    except:
        text = "Error in getting response.\nCheck your input and network connection"
    label['text'] = text

SIZE = [550, 800]

root = tk.Tk()
root.title("Instant Weather Checker by Pavel Grigorev")
root.maxsize(800, 550)
root.minsize(650, 300)

canvas = tk.Canvas(root, height = SIZE[0], width = SIZE[1])
canvas.pack()

backgroung = tk.PhotoImage(file = 'media/weather.png')
backgroungLabel = tk.Label(root, image = backgroung)
backgroungLabel.place(relwidth = 1, relheight = 1, )

upperFrame = tk.Frame(root, bg = '#3B6EC9', bd = 5)
upperFrame.place(relx = 0.5, rely = 0.1, relwidth = 0.85, relheight = 0.1, anchor = "n")

textBox = tk.Entry(upperFrame, bg = "white", font = ('Courier New', 20))
textBox.insert(0,"Input City Name or Coordinates")
textBox.place(relwidth = 0.65, relheight = 1)

button = tk.Button(upperFrame, text="Check Weather", font = ('Courier New', 20), command = lambda: getWeather(textBox.get()))
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

lowerFrame = tk.Frame(root, bg = "#3B6EC9", bd = 10)
lowerFrame.place(relx = 0.5, rely = 0.25, relwidth = 0.85, relheight = 0.6, anchor = "n")

label = tk.Label(lowerFrame, text = "", bg = "white", font = ('Courier New', 20))
label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

root.mainloop()
