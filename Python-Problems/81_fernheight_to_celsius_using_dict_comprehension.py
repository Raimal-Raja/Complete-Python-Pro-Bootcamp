weather = {"mondy":37,
           'tuesday':14,
           "wednesday":15,
           "thursday":14,
           "friday":21,
           "saturday":22,
           "sunday":24
           }

new_list = {days:(tem *9/5 +32) for (days, tem) in weather.items()}
print(new_list)