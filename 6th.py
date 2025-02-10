import numpy as np
random_array = np.random.rand(100)
normalized_array = (random_array - np.min(random_array)) / (np.max(random_array) - np.min(random_array))
print("Original Array:\n", random_array)
print("\nNormalized Array:\n", normalized_array)
