from geopy.geocoders import Nominatim

# generates lat and long using an address input
print("GEOLOCATING")
geolocator = Nominatim(user_agent="Vade_test_question")
location = geolocator.geocode("1128 Berwyn Way NC")
print(location.address)
print((location.latitude, location.longitude))

# reverse generates an adddress using lat and long input
print("REVERSE GEOLOCATING")
geolocator = Nominatim(user_agent="Vade_test_question")
location = geolocator.reverse("35.91847454422203, -78.67605333997926")
print(location.address)