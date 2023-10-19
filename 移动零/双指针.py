from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


# 时间复杂度：O(n)，其中 n 为序列长度。每个位置至多被遍历两次。

if __name__ == '__main__':
    lst1 = [0, 1, 0, 3, 12]
    Solution().moveZeroes(lst1)
    print(lst1)

    lst2 = [0]
    Solution().moveZeroes(lst2)
    print(lst2)
