
import requests

def get_weather(city):
    url = f"http://wttr.in/{city}?format=j1"
    try:
        data = requests.get(url).json()
        current = data['current_condition'][0]
        condition = current['weatherDesc'][0]['value']
        temp = current['temp_C']
        humidity = current['humidity']
        wind = current['windspeedKmph']
        report = f"Weather in {city}:\nCondition: {condition}\nTemperature: {temp}°C\nHumidity: {humidity}%\nWind Speed: {wind} kmph"
        return report
    except:
        return "Unable to fetch weather data."

def get_weather_telugu(city):
    url = f"http://wttr.in/{city}?format=j1"
    try:
        data = requests.get(url).json()
        current = data['current_condition'][0]
        condition = current['weatherDesc'][0]['value']
        temp = current['temp_C']
        humidity = current['humidity']
        wind = current['windspeedKmph']
        report = f"{city}లో వాతావరణ నివేదిక:\nపరిస్థితి: {condition}\nఉష్ణోగ్రత: {temp}°C\nతేమ: {humidity}%\nగాలివేగం: {wind} కి.మీ/గం"
        return report
    except:
        return "వాతావరణ సమాచారం పొందలేకపోయాం."

def get_weather_hindi(city):
    url = f"http://wttr.in/{city}?format=j1"
    try:
        data = requests.get(url).json()
        current = data['current_condition'][0]
        condition = current['weatherDesc'][0]['value']
        temp = current['temp_C']
        humidity = current['humidity']
        wind = current['windspeedKmph']
        report = f"{city} के लिए मौसम:\nस्थिति: {condition}\nतापमान: {temp}°C\nनमी: {humidity}%\nहवा की गति: {wind} किमी/घंटा"
        return report
    except:
        return "मौसम डेटा लाने में विफल।"
