import requests
import json

# Erfurt, GER, https://www.latlong.net/place/erfurt-thuringia-germany-29863.html
lat = 50.983334
lng = 11.033333

url = f"https://api.sunrise-sunset.org/json?lat=,{lat},&lng=,{lng},&date=today"  # https://sunrise-sunset.org/api


def requestAPIResp(_url):
    resp = requests.get(_url)
    return resp


def saveToJSON(_apiResponse):
    file = open("suntimerfile.json", "w")
    json.dump(res.json(), file, indent=6)
    file.close()


#####################################################


res = requestAPIResp(url)

if res.status_code == 200:
    saveToJSON(res)

    with open("suntimerfile.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

        sunrise = jsonObject['results']['sunrise']
        sunset = jsonObject['results']['sunset']
        solar_noon = jsonObject['results']['solar_noon']
        day_length = jsonObject['results']['day_length']

        print("Sunrise: " + sunrise, "Sunset: " + sunset, "Solar Noon:" + solar_noon, "Day Length: " + day_length,
              sep=" , ")
        print("Times are in UTC")

else:
    print("No valid response")
