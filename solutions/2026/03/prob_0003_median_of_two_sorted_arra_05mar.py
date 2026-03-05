def medianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    length = len(merged)
    mid = length // 2

    if length % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return merged[mid]

# --- Test Cases ---
if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(medianSortedArrays(nums1, nums2))  # Expected: 2.0

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(medianSortedArrays(nums1, nums2))  # Expected: 2.5

    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [7, 8, 9, 10, 11, 12]
    print(medianSortedArrays(nums1, nums2))  # Expected: 8.5