# 1456.定长子串元音最大数目
class Solution:
    # 定长滑动窗口模板套路
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)

        res = 0
        temp = 0
        
        for i, ch in enumerate(s):
            # insert
            if ch in 'aeiou':
                temp += 1
            if i < k - 1:
                continue

            # update
            res = max(res, temp)

            # delete
            if s[i-k+1] in 'aeiou':
                temp -= 1
        
        return res
            

# 1343.平均值大于等于阈值的子数组数目  mid
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        nums = arr
        
        n = len(nums)
        res = 0
        temp = 0
        
        for i, num in enumerate(nums):
            # insert
            temp += num
            if i < k - 1:
                continue

            # update
            if temp/k >= threshold:
                res += 1
            
            # delete
            temp -= nums[i-k+1]
        
        return res


# 2090.半径为k的子数组平均值  mid
class Solution:
    # 变形题：相当于定长为2 * k + 1的窗口
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        res = [-1 for i in range(n)]
        temp = 0
        k = 2 * k + 1

        for i, num in enumerate(nums):
            temp += num
            if i < k - 1:
                continue
            
            # k可能为0
            res[i - int(k / 2)] = temp // k
            
            temp -= nums[i-k+1]
        
        return res


