import numpy as np  # NumPy লাইব্রেরি ইমপোর্ট

# 1D অ্যারে তৈরি
a = np.array([1, 2, 3])  # একটি ১-ডাইমেনশনাল অ্যারে
print("1D Array:", a)    # ১-ডাইমেনশনাল অ্যারে প্রিন্ট
print("Type:", type(a))  # টাইপ চেক (numpy.ndarray)
print("Dimension:", a.ndim)  # অ্যারের ডাইমেনশন চেক (১)

# 2D অ্যারে তৈরি
b = np.array([[1, 2, 3], [4, 5, 6]])  # একটি ২-ডাইমেনশনাল অ্যারে
print("\n2D Array:\n", b)  # ২-ডাইমেনশনাল অ্যারে প্রিন্ট
print("Shape:", b.shape)   # অ্যারের আকার চেক (২ রো এবং ৩ কলাম)
print("Dimension:", b.ndim)  # ডাইমেনশন চেক (২)

# 3D অ্যারে তৈরি
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # একটি ৩-ডাইমেনশনাল অ্যারে
print("\n3D Array:\n", c)  # ৩-ডাইমেনশনাল অ্যারে প্রিন্ট
print("Shape:", c.shape)   # ৩D অ্যারের আকার চেক (২x২x২)
print("Dimension:", c.ndim)  # ডাইমেনশন চেক (৩)

# জিরো এবং ওয়ান দিয়ে অ্যারে তৈরি
zeros_array = np.zeros((3, 3))  # ৩x৩ এর একটি জিরো-ম্যাট্রিক্স
print("\nZeros Array:\n", zeros_array)  # জিরো-ম্যাট্রিক্স প্রিন্ট

ones_array = np.ones((2, 4))  # ২x৪ এর একটি ওয়ান-ম্যাট্রিক্স
print("\nOnes Array:\n", ones_array)  # ওয়ান-ম্যাট্রিক্স প্রিন্ট

# র‍্যান্ডম সংখ্যা দিয়ে অ্যারে তৈরি
random_array = np.random.random((3, 2))  # ৩x২ এর একটি র‍্যান্ডম অ্যারে
print("\nRandom Array:\n", random_array)  # র‍্যান্ডম অ্যারে প্রিন্ট

# অ্যারে গণিত
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])
print("\nAddition:", arr1 + arr2)  # অ্যারের যোগফল
print("Multiplication:", arr1 * arr2)  # অ্যারের গুণফল
print("Mean:", np.mean(arr1))  # গড় মান
print("Sum:", np.sum(arr1))    # মোট যোগফল

# ইনডেক্সিং এবং স্লাইসিং
print("\nIndexing:", arr1[1])  # দ্বিতীয় উপাদান প্রিন্ট
print("Slicing:", arr1[1:3])  # স্লাইস করা (১ থেকে ২ নম্বর পর্যন্ত)

# রি-শেপিং অ্যারে
reshaped_array = np.reshape(arr1, (3, 1))  # ১D অ্যারে থেকে ২D অ্যারে
print("\nReshaped Array:\n", reshaped_array)  # রিশেপ করা অ্যারে প্রিন্ট
