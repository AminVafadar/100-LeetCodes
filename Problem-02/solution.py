class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # dictionary to store number -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        # In case no solution is found (though problem guarantees one)
        return []
     
     # ✅ Example Test
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(s.twoSum([3, 2, 4], 6))        # [1, 2]
    print(s.twoSum([3, 3], 6))           # [0, 1]
