import numpy as np

#English lower caps
entropy_a = -10*(1/26) * np.log2(1/26)
print(entropy_a)

#English lower caps and upper caps
entropy_b = -10*(1/52) * np.log2(1/52)
print(entropy_b)

#Alphanumeric including *"-+=
entropy_c = -10*(1/67) * np.log2(1/67)
print(entropy_c)
