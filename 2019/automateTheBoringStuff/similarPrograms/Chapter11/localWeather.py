#! python3
# input location and get a webpage with weather forecast
import webbrowser
loc = input('enter location| ')
webbrowser.open('https://openweathermap.org/find?q=' + loc)pw