import numpy as np

def analyzeOneDimArray(oneDimArray: np.ndarray):
    print(f"1D Array: {oneDimArray}")
    print(f"Min: {oneDimArray.min()}, Max: {oneDimArray.max()}, Mean: {oneDimArray.mean()}")
    print(f"Sum: {oneDimArray.sum()}, Standard Deviation: {oneDimArray.std()}\n")

def analyzeTwoDimArray(twoDimArray: np.ndarray):
    print(f"2D Array:\n{twoDimArray}")
    print(f"Row-wise Min: {twoDimArray.min(axis=1)}")
    print(f"Column-wise Max: {twoDimArray.max(axis=0)}")
    print(f"Overall Mean: {twoDimArray.mean()}")
    print(f"Sum of all elements: {twoDimArray.sum()}\n")

def analyzeBooleanArray(boolArray: np.ndarray):
    """Performs operations on a Boolean NumPy array."""
    print(f"Boolean Array:\n{boolArray}")
    print(f"Count of True values: {np.count_nonzero(boolArray)}")
    print(f"Any True? {boolArray.any()}, All True? {boolArray.all()}")
    print(f"Inverted Boolean Array:\n{~boolArray}\n")

oneDimArray = np.array([3, 7, 1, 9, 12])
twoDimArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
boolArray = np.array([[True, False, True], [False, False, True]])

print("===== 1D Array =====")
print(oneDimArray)
print("===== 1D Array Stats =====")
analyzeOneDimArray(oneDimArray)

print("===== 2D Array =====")
print(twoDimArray)
print("===== 2D Array Stats =====")
analyzeTwoDimArray(twoDimArray)

print("===== Boolean Array =====")
print(boolArray)
print("===== Boolean Array Stats =====")
analyzeBooleanArray(boolArray)

