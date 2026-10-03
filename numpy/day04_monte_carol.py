import numpy as np

n = 1000000000

machines = np.random.choice(
    ['A','B','C'],
    size = n,
    p = [0.5,0.3,0.2]
)

print(machines[:10])

is_defective = np.zeros(n, dtype=bool)

mask_A = machines == 'A'
mask_B = machines == 'B'
mask_C = machines == 'C'

is_defective[mask_A] = np.random.rand(mask_A.sum()) < 0.01
is_defective[mask_B] = np.random.rand(mask_B.sum()) < 0.02
is_defective[mask_C] = np.random.rand(mask_C.sum()) < 0.05

total_defective = is_defective.sum()
c_defective = (mask_C & is_defective).sum()

estimated_probability = c_defective / total_defective

print(estimated_probability)