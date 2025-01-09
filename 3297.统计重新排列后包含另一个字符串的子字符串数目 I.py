class Solution:
    # 打表 + 双指针法   t1 >= t2 后面不用比较，直接累加
    def validSubstringCount(self, word1: str, word2: str) -> int:
        # t1 >= t2  python原生 m = [2,0,2] >= t = [1,1,1],需要自己写一个函数
        def compare(t1, t2):
            n = len(t1)
            for i in range(n):
                if t1[i] < t2[i]:
                    return False
            return True

        t1 = [0 for i in range(26)]
        t2 = [0 for i in range(26)]
        for ch in word2:
            index = ord(ch) - ord('a')
            t2[index] += 1
        
        n = len(word1)
        left = 0
        right = 0
        res = 0
        while(right <= n):
            if compare(t1, t2):
                res += (n - right + 1)
                t1[ord(word1[left]) - ord('a')] -= 1
                left += 1
            elif right < n:
                index = ord(word1[right]) - ord('a')
                t1[index] += 1
                right += 1
            # 最后right==n, 且t1 < t2 直接退出
            else:
                break
            
        return res
            
            
                
            
        