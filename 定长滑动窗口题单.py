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

# 1052.爱生气的书店老板  mid
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # 滑动窗口求得minutes内的最大收益, 让最多的人满意
        # pos表示当前最大收益窗口的右边界
        temp = 0
        res = float('-inf')
        pos = 0
        for i, num in enumerate(customers):
            if grumpy[i] == 1:
                temp += num
            
            if i < minutes - 1:
                continue
            
            if temp > res:
                res = temp
                pos = i
                
            # res = max(temp, res)

            if grumpy[i - minutes + 1] == 1:
                temp -= customers[i - minutes + 1]
        
        # 求出最后的结果。[pos-minutes+1, pos]区间内的都算满意。
        res = 0
        for i in range(n):
            if grumpy[i] == 0:
                res += customers[i]
            elif i >= pos - minutes + 1 and i <= pos:
                res += customers[i]

        return res

# 1461.检查一个字符串是否包含所有长度为 K 的二进制子串
class Solution:
    # 滑动串口+哈希记录所有的子串  最后判断是否有2^k个
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        # 长度不够直接退出
        if n < 2 ** k  + k - 1:
            return False
        
        dic = {}
        # i = 0
        j = k - 1
        while(j < n):
            temp = s[j-k+1: j+1] 
            if temp not in dic:
                dic[temp] = 1
            
            j += 1
        
        if len(dic) == 2 ** k:
            return True
        
        return False
    
# 2814.几乎唯一子数组最大和
class Solution:
    # 滑动窗口变形。普通的定长滑动窗口加上一个条件判断，然后计算res
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)

        res = 0
        temp = 0
        dic = {}
        for i, num in enumerate(nums):
            temp += num
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
                
            if i < k - 1:
                continue
            
            # s = set(nums[i-k+1: i+1])
            if len(dic) >= m:
                res = max(res, temp)
            
            temp -= nums[i-k+1]
            if dic[nums[i-k+1]] == 1:
                del dic[nums[i-k+1]]
            else:
                dic[nums[i-k+1]] -= 1
        
        return res

