# NumPy লাইব্রেরি ইমপোর্ট
import numpy as np

# এক-ডাইমেনশনাল (1D) অ্যারে তৈরি
a = np.array([1, 2, 3])  
print("1D Array:", a)  # ১ডি অ্যারে প্রিন্ট
print("Type:", type(a))  # টাইপ দেখায়
print("Dimensions:", a.ndim)  # ডাইমেনশন দেখায়

# দুই-ডাইমেনশনাল (2D) অ্যারে তৈরি
b = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", b)  # ২ডি অ্যারে প্রিন্ট
print("Shape:", b.shape)  # আকৃতি (rows, columns) দেখায়
print("Size:", b.size)  # মোট এলিমেন্ট সংখ্যা

# শূন্য দিয়ে পূর্ণ ৩x৩ ম্যাট্রিক্স তৈরি
zeros_matrix = np.zeros((3, 3))  
print("\nZeros Matrix:\n", zeros_matrix)

# এক (1) দিয়ে পূর্ণ ২x৪ ম্যাট্রিক্স তৈরি
ones_matrix = np.ones((2, 4))  
print("\nOnes Matrix:\n", ones_matrix)

# এলোমেলো সংখ্যা দিয়ে পূর্ণ ২x৩ ম্যাট্রিক্স তৈরি
random_matrix = np.random.rand(2, 3)  
print("\nRandom Matrix:\n", random_matrix)

# একটি নির্দিষ্ট সংখ্যা দ্বারা পূর্ণ ম্যাট্রিক্স
filled_matrix = np.full((3, 3), 7)  # ৭ দ্বারা পূর্ণ
print("\nFilled Matrix:\n", filled_matrix)

# একটি ক্রম তৈরি (start=0, stop=10, step=2)
sequence = np.arange(0, 10, 2)  
print("\nSequence:", sequence)

# ৫ সংখ্যার মধ্যে সমান দূরত্বে বিভক্ত সংখ্যা তৈরি
linspace_array = np.linspace(0, 1, 5)  
print("\nLinspace Array:", linspace_array)

# ম্যাট্রিক্স যোগ-বিয়োগ
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
sum_matrix = matrix1 + matrix2  # ম্যাট্রিক্স যোগ
diff_matrix = matrix1 - matrix2  # ম্যাট্রিক্স বিয়োগ
print("\nMatrix Addition:\n", sum_matrix)
print("Matrix Subtraction:\n", diff_matrix)

# ম্যাট্রিক্স গুন এবং ডট প্রডাক্ট
product_matrix = matrix1 * matrix2  # এলিমেন্ট অনুযায়ী গুন
dot_product = np.dot(matrix1, matrix2)  # ডট প্রডাক্ট
print("\nMatrix Element-wise Multiplication:\n", product_matrix)
print("Matrix Dot Product:\n", dot_product)

# ট্রান্সপোজ (transpose) ম্যাট্রিক্স
transpose_matrix = matrix1.T  
print("\nTransposed Matrix:\n", transpose_matrix)

# এলিমেন্টের গড়, সর্বোচ্চ এবং সর্বনিম্ন মান
print("\nMean of Matrix1:", np.mean(matrix1))  # গড়
print("Max of Matrix1:", np.max(matrix1))  # সর্বোচ্চ মান
print("Min of Matrix1:", np.min(matrix1))  # সর্বনিম্ন মান
