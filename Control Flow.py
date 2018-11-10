# Control flow
# if, else, elif
# while and for loops

trafficLightState = "yellow"
distanceFromLight = 10

if trafficLightState == "green":
    print("go")
elif trafficLightState == "yellow" and distanceFromLight <= 15:
  print("speed up")
elif trafficLightState == "yellow" and distanceFromLight > 15:
  print("slow down")
elif trafficLightState == "red":
  print("stop")
else:
  print("unknown action")
