with open("input.txt") as input:
  instructions = input.readlines()
  horizontal = 0
  depth = 0
  aim = 0

  for i in instructions:
    instruction, distance = i.split(" ")
    if(instruction == "forward"):
      depth += (aim*int(distance))
      horizontal += int(distance)
    if(instruction == "backward"):
      horizontal -= int(distance)
    if(instruction == "up"):
      aim -= int(distance)
    if(instruction == "down"):
      aim += int(distance)
  
  print(horizontal * depth)