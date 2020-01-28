import requests
import geocoder

api_base_url = "https://api.darksky.net/forecast/ac0eca6a9b53e0ace708e0eb9a9e60b1/"

destinations = ["Space Needle", "Crater Lake", "Golden Gate Bridge", "Yosemite National Park", "Las Vegas, Nevada", "Grand Canyon National Park", "Aspen, Colorado", "Mount Rushmore", "Yellowstone National Park", "Sandpoint, Idaho", "Banff National Park", "Capilano Suspension Bridge"]
for point in destinations:
    g = geocoder.arcgis(point)
    full_api_url = api_base_url + str(g.latlng[0]) + "," + str(g.latlng[1])
    result = requests.request('GET', full_api_url).json()
    print(point, " ", "is located at", " ", "(","{0:.4f}".format(g.latlng[0]), ",", "{0:.4f}".format(g.latlng[1]), ")" , "\n", "At ", point, " right now, it's", " ", result["currently"]["summary"], " ", "with a temperature of ", result["currently"]["temperature"], u'\u00B0', " ", "F", sep='')     