import math
from functools import reduce

points = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
distance = list(map(lambda x: (x[0] ** 2 + x[1] ** 2 + x[2] ** 2) ** 0.5, points))
print(distance)

#  FILTER  #
NaN = float('nan')
scores = [[NaN, 12, 0.5, 78, math.pi],
          [2, 13, 0.5, 0.7, math.pi / 2],
          [2, NaN, 0.5, 78, math.pi],
          [2, 14, 0.5, 39, 1 - math.pi]
          ]

print(list(filter(lambda x: NaN not in x, scores)))

# REDUCE #
list1 = [1, 2, 3, 4, 6, 7, 8, 5, 9]
print(reduce(lambda x, y: x + y, list1)/len(list1))