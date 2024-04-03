# 세 수의 합
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
from typing import List

# nums = [-1, 0, 1, 2, -1, -4]
nums = [0, 0, 0]
expected = [[-1, -1, 2], [-1, 0, 1]]

def threeSum(self, nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()
    # 1.브루트 포스 n^3 반복
    # for i in range(len(nums) - 2):
    #     # 중복된 값 건너뛰기
    #     if i > 0 and nums[i] == nums[i - 1]:
    #         continue
    #     for j in range(i + 1, len(nums) - 1):
    #         if (j > i + 1 and nums[j] == nums[j - 1]) or j <= i:
    #             continue
    #         for k in range(i + 2, len(nums)):
    #             if (k > j + 1 and nums[k] == nums[k - 1]) or k <= j:
    #                 continue
    #             if nums[i] + nums[j] + nums[k] == 0:
    #                 results.append([nums[i], nums[j], nums[k]])
    # return results

    # 2.투 포인터로 합 계산
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 간격을 좁혀가며 합 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0인 경우이므로 정답 및 중복 스킵처리
                results.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return results

output = threeSum(nums, nums)
print(output == expected, output)