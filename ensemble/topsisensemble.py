pred_scores = []
from numpy import *
import numpy as np
for i in range(len(test3)):
  confidence1 = test3[i]
  confidence2 = test4[i]
  confidence3 = test5[i]

  
  c1 = np.array(confidence1)
  c2 = np.array(confidence2)
  c3 = np.array(confidence3)


  x = np.vstack((c1,c2,c3))
  n = 3#(classifier)
  m = 3#(classes)

  w=[0.1, 0.3, 0.4]
  weights = np.array(w)
  av=[w[i]*(a1[i]+a2[i]+a3[i]) for i in range(3)]
  print("Weighted Average:", av)

  #classifiers
  col_sums = array(cumsum(x**2,0))
  
  a=col_sums[x.shape[0]- 1, 0]+col_sums[x.shape[0]- 1, 1]+col_sums[x.shape[0]- 1, 2]
  norm_x = np.array([[round(x[i, j] / sqrt(col_sums[x.shape[0]- 1, j]),5) for j in range(n)] for i in range(m)])
  print(norm_x)
  wnx = np.array([[round(weights[i] * norm_x[j, i], 3) for i in range(n)] for j in range(m)])
  print(wnx)
  pis = np.array([amax(wnx[:, :1]), amax(wnx[:, 1:2]), amax(wnx[:, 2:3])])
  print(pis)
  nis = np.array([amin(wnx[:, :1]), amin(wnx[:, 1:2]), amin(wnx[:, 2:3])])
  print(nis)
  b1 = np.array([[(wnx[j, i] - pis[i])**2 for i in range(n)] for j in range(m)])
  dpis = sqrt(sum(b1, 1))
  print(dpis)
  b2 = array([[(wnx[j, i] - nis[i])**2 for i in range(n)] for j in range(m)])
  dnis = sqrt(sum(b2, 1))
  print(dnis)
  final_solution = array([round(dnis[i] / (dpis[i] + dnis[i]), 5) for i in range(m)])
  print("Grand Final: ",final_solution)
  pred = np.argmax(final_solution)
  z = np.array([0,0,0])
  z[pred] = 1
  pred_scores.append(z)
pred_list = np.array(pred_scores)
