with open("input.txt") as input:
  instructions = input.readlines()
  horizontal = 0
  depth = 0

  for i in instructions:
    instruction, distance = i.split(" ")
    if(instruction == "forward"):
      horizontal += int(distance)
    if(instruction == "backward"):
      horizontal -= int(distance)
    if(instruction == "up"):
      depth -= int(distance)
    if(instruction == "down"):
      depth += int(distance)
  
  print(horizontal * depth)