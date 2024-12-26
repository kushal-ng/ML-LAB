# import csv

# with open("C:/Users/admin/Downloads/CSE 5/Visual Studio Code/python files/ML LAB/Trainingdata1.csv") as f:
#     data = csv.reader(f)
#     data = list(data)
#     #print(data)

# h = [0 for i in range(len(data[0])-1)]
# for i in data:
#     if i[-1] == 'Yes':
#         for j in range(len(h)):
#             if h[j] == 0:
#                 h[j] = i[j]
#             elif h[j] != i[j]:
#                 h[j] = "?"
# print("Specific hypothesis is :",h)

import pandas as pd
import numpy as np