with open('input.txt') as input:
  depths = input.readlines()
  print(sum(int(l) > int(i) for i, l in zip(depths, depths[1:])))