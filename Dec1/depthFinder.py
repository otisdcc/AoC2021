with open('input.txt') as input:
  depthReadings = input.readlines()
  print (len(depthReadings))
  depthIncreaseCounter = 0
  i = 1

  while i < len(depthReadings):

    if(int(depthReadings[i]) > int(depthReadings[i-1])):
      depthIncreaseCounter += 1
    i += 1

  print(depthIncreaseCounter)