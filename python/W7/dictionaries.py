weather_prague = ["Prague", True, 0.77, 13, "Partly cloudy, partly sunny", "Not so nice weather now"]
#0...name of the city
#1... rainy
#2... humidity
#3... celsius
#4... note (not mandatory)
print(type(weather_prague))

dw_prg = {"city":"Prague","rainy":True,"humidity":0.77,"temperature":13, "note":"Partly cloudy, partly sunny","feeling":"Not so nice weather right now"}
print(type(dw_prg))
#we work with pairs (key and value)
print(dw_prg["city"])

dw_kyo = {"city":"Kyoto","rainy":True,"humidity":0.66,"temperature":21}
dw_mar = {"city":"Marrakech","rainy":False,"humidity":0.61,"temperature":21}
dw = {"Prague":dw_prg, "Kyoto":dw_kyo, "Marrakech":dw_mar}
print(dw)
print(type(dw))
print(len(dw))

print(dw["Kyoto"]["city"],dw["Kyoto"]["humidity"])
#Printing keys
print(dw.keys())
print(len(dw))
dw["London"] = {}
print(len(dw))
print(dw.values())
print(dw.keys())
dw["London"]["city"] = "London"
dw["London"]["rainy"] = True
dw["London"]["humidity"] = 0.87
dw["London"]["temperature"] = 12
dw["London"]["note"] = "There is always rain"
print(dw.values())
print(f"---------------------------")
print(dw.keys())
dw.pop("Prague") #remove items
print(dw.keys())

#array [key]
print(dw.items())
print("================")
for key,value in dw.items():
    print(f"Key: {key}, value {value}")
    for subkey,subvalue in value.items():
        print(f"->Subkey: {key}, subvalue: {subvalue}")


print("================-------===============")
Counter = 1
sub_counter = 1
for key,value in dw.items():
    print(f"{Counter}# {key.upper()}")
    Counter +=1
    for subkey,subvalue in value.items():
        print(f"->Subkey #{sub_counter}: {key}, subvalue #{sub_counter}: {subvalue}")
        sub_counter +=1