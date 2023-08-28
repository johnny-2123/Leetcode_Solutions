class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seenNums = set()

        for n in nums:
            if n in seenNums:
                return True
            seenNums.add(n)

        return False
