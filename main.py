from geopy.geocoders import Nominatim

# generates lat and long using an address input
print("GEOLOCATING")
geolocator = Nominatim(user_agent="Vade_test_question")
user_input_address = input("Please type address in format of Street Number Street Name. ")
location = geolocator.geocode(user_input_address)
print(location.address)
print((location.latitude, location.longitude))

# reverse generates an adddress using lat and long input
print("")
print("REVERSE GEOLOCATING")
geolocator = Nominatim(user_agent="Vade_test_question")
user_input_coordinates = input("Please enter Latitude, Longitude. ")
location = geolocator.reverse(user_input_coordinates)
print(location.address)