class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        m -= 1
        n -= 1

        while m >= 0 and n >= 0:
            num1 = nums1[m]
            num2 = nums2[n]

            if (num1 >= num2):
                nums1[last] = num1
                m -= 1
            else:
                nums1[last] = num2
                n -= 1
            last -= 1
            
        while n >= 0:
            nums1[last] = nums2[n]
            n -= 1
            last -= 1
        