# from random import randint

# def get_temperature(sensor):
#     return randint(-20,0) if sensor else randint(0, 20)

# def get_pressure(sensor):
#     if sensor:
#         return randint(720, 750)
#     else:
#         return randint(750, 770)    
    
# def get_wind_speed(sensor):
#     if sensor == 1:
#         return randint(0, 30)
#     else:
#         return randint(30, 50) 

# def data_collection(sensor = 1):
#     return (get_temperature(sensor), get_pressure(sensor), get_wind_speed(sensor))

def get_name(sensor):
    return sensor

def get_num(sensor):
    return sensor
     
def get_text(sensor):
    return sensor
    
def data_collection(sensor = 1):
    return (get_name(sensor), get_num(sensor), get_text(sensor))

  