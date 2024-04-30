from pyowm import OWM

owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
mgr = owm.weather_manager()

city = input("Введите название города на английском языке: ")

observation = mgr.weather_at_place(city)

if observation is not None:
    from pprint import pprint
    print(dir(observation))
    d = observation.to_dict()
    pprint(d)
else:
    print(f"Город {city} не найден.")

