with open('input.txt') as input:
  depthReadings = input.readlines()
  depthIncreaseCounter = 0
  i = 1

  while (i + 2) < len(depthReadings):
    currentWindow = int(depthReadings[i]) + int(depthReadings[i+1]) + int(depthReadings[i+2])
    previousWindow = int(depthReadings[i-1]) + int(depthReadings[i]) + int(depthReadings[i+1])

    if(currentWindow > previousWindow):
      depthIncreaseCounter += 1
    i += 1
  
  print(depthIncreaseCounter)