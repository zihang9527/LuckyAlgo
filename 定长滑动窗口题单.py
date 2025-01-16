from typing import List
'''
总结
1、模板题单指针写法和双指针写法 
    单指针 lc1456
    双指针 1652
2、针对滑动窗口内满足某个的条件的res值
    2.1 窗口求平均满足某个条件  lc1343
    2.2 窗口内不重复元素条件  lc1297 lc2461 lc2814
    2.3 窗口内第x小数  lc2653
3、问题转变为滑动窗口题
    lc1423  k = n - k
    lc2090 半径为k的子数组平均值 k = 2*k+1
    lc2134 最小交换次数把所有1放一起  k = sum(nums)
4、k属于区间[minSize, maxSize]，遍历k的范围，然后计算res
    lc1297
'''

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

# 1052.爱生气的书店老板 mid
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
    
# 2461.长度为 K 子数组中的最大和  mid
class Solution:
    # 常规变形：定长滑动+子数组特定条件
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
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

            if len(dic) == k:
                res = max(res, temp)

            leftNum = nums[i-k+1]
            temp -= leftNum
            if dic[leftNum] == 1:
                del dic[leftNum]
            else:
                dic[leftNum] -= 1
            
        return res
            
# 1423.一行卡牌可获得的最大点数  mid
class Solution:
    # 转换为滑动窗口n-k的最小和
    # 注意：1、k==n的情况，此时窗口等于0
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        s = sum(cardPoints)

        if k == n:
            return s
        new_k = n - k
        
        temp = 0
        res = float('-inf')
        for i, num in enumerate(cardPoints):
            temp +=  num
            if i < new_k - 1:
                continue
            
            res = max(res, s - temp)
            
            # print(i)
            temp -= cardPoints[i - new_k + 1]
        
        return res

# 1652.拆炸弹
class Solution:
    # 学习：1、循环数组采用 code += code拼接。 2、学习使用滑动窗口的双指针写法。之前属于单指针写法[i-k+1, i]表示窗口区间
    # 题解：拼接后滑动窗口  
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        code += code
        res = []
        
        if k > 0:
            l = 1
            r = k
        else:
            r = n - 1
            # k < 0 
            l = n + k
        
        # for i in range()
        s = sum(code[l:r+1])
        for i in range(n):
            res.append(s)
            s -= code[l]
            s += code[r + 1]
            
            l += 1
            r += 1
        
        return res

# 1297.子串的最大出现次数  mid
class Solution:
    # 简单变形题：k范围[minSize, maxSize],区间内不同字符<=maxLetters
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        
        res = 0
        for k in range(minSize, maxSize+1):
            dic = {}
            ch_dic = {}
        
            for i, ch in enumerate(s):
                # temp += ch
                if ch not in ch_dic:
                    ch_dic[ch] = 1
                else:
                    ch_dic[ch] += 1

                if i < k - 1:
                    continue
                
                temp = s[i-k+1:i+1]
                if len(ch_dic) <= maxLetters:
                    if temp not in dic:
                        dic[temp] = 1
                    else:
                        dic[temp] += 1
                
                    res = max(res, dic[temp])

                l_ch = s[i-k+1]
                if ch_dic[l_ch] == 1:
                    del ch_dic[l_ch]
                else:
                    ch_dic[l_ch] -= 1
                
        return res

# 2134.最小交换次数把所有1放一起  mid
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = sum(nums)
        nums += nums

        if k == 0:
            return 0
        
        temp = 0
        res = float('inf')
        for i, num in enumerate(nums[:n+k-1]):
            temp += num
            if i < k - 1:
                continue
            
            res = min(res, k - temp)
            
            temp -= nums[i-k+1]
        
        return res

# 2653.滑动子数组内的第x小数  
class Solution:
    # 如何求窗口内第x小数：由于值域很小，采取计数排序的方法。累计计数，第一个大于x的数就是第x小数。
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        
        res = []
        window = [0] * 101
        for i, num in enumerate(nums):
            window[num+50] += 1
            if i < k - 1:
                continue
            
            count = 0
            # print(window)
            for j in range(len(window)):
                count += window[j]
                if count >= x:
                    if j - 50 < 0:
                        res.append(j - 50)
                    else:
                        res.append(0)

                    break
            
            window[nums[i-k+1]+50] -= 1
        
        return res
                    
                
            