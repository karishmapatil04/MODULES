# Operations in Convolutional Neural Networks
# 1. Convolution
# 2. Max Pooling
# 3. Flattening

import numpy as np

# Input matrix
input_matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Convolution kernel
kernel = np.array([
    [1, 0],
    [0, 1]
])

# ---------------- CONVOLUTION ----------------

rows, cols = input_matrix.shape
k_rows, k_cols = kernel.shape

output_rows = rows - k_rows + 1
output_cols = cols - k_cols + 1

convolution = np.zeros((output_rows, output_cols))

for i in range(output_rows):
    for j in range(output_cols):
        region = input_matrix[i:i+k_rows, j:j+k_cols]
        convolution[i, j] = np.sum(region * kernel)

print("Input Matrix:")
print(input_matrix)

print("\nKernel:")
print(kernel)

print("\nConvolution Result:")
print(convolution)


# ---------------- MAX POOLING ----------------

pool_size = 2
pool_rows = convolution.shape[0] // pool_size
pool_cols = convolution.shape[1] // pool_size

max_pooling = np.zeros((pool_rows, pool_cols))

for i in range(pool_rows):
    for j in range(pool_cols):
        region = convolution[
            i * pool_size:(i + 1) * pool_size,
            j * pool_size:(j + 1) * pool_size
        ]

        max_pooling[i, j] = np.max(region)

print("\nMax Pooling Result:")
print(max_pooling)


# ---------------- FLATTENING ----------------

flattened = max_pooling.flatten()

print("\nFlattened Result:")
print(flattened)