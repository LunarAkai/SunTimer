import requests
import json


with open("config.json") as configFile:
    jsonObject = json.load(configFile)
    configFile.close()

    apiKey = jsonObject['keys']['api_key']


def requestAPIResp(_url):
    resp = requests.get(_url)
    return resp


def saveToJSON(_apiResponse):
    global fileName
    if isCityAPI:
        fileName = "currentcity.json"
    if not isCityAPI:
        fileName = "suntimerfile.json"

    file = open(fileName, "w")
    json.dump(res.json(), file, indent=6)
    file.close()


#####################################################


limit = 1

cityName = input("Please enter the city name: ")
countryCode = input("Please enter the country code: ")

urlCity = f"http://api.openweathermap.org/geo/1.0/direct?q={cityName},{countryCode}&limit={limit}&appid={apiKey}"
isCityAPI = True

res = requestAPIResp(urlCity)

if res.status_code == 200:

    saveToJSON(res)
    isCityAPI = False

    with open("currentcity.json", "r") as jsonCityFile:
        obj = json.load(jsonCityFile)
        jsonCityFile.close()

        lat = obj[0]['lat']
        lng = obj[0]['lon']

    urlSun = f"https://api.sunrise-sunset.org/json?lat=,{lat},&lng=,{lng},&date=today"  # https://sunrise-sunset.org/api
    print(urlSun)
    res = requestAPIResp(urlSun)
    print(res.status_code)

    if res.status_code == 200:
        saveToJSON(res)

        with open("suntimerfile.json") as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()

            sunrise = jsonObject['results']['sunrise']
            sunset = jsonObject['results']['sunset']
            solarNoon = jsonObject['results']['solar_noon']
            dayLength = jsonObject['results']['day_length']

            print("Sunrise: " + sunrise, "Sunset: " + sunset, "Solar Noon: " + solarNoon, "Day Length: " + dayLength,
                  sep=" , ")
            print("Times are in UTC")
    else:
        print("No valid Sun Response")

else:
    print("No valid City response")
