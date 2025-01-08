class Solution:
    # 排序 + 求前后数最大差值
    # 注意非边界时要减1
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        n = len(special)
        special.sort()
        
        temp = special[0]
        res = special[0] - bottom
        for i in range(1, len(special)):
            res = max(res, special[i] - temp - 1)
            temp = special[i]
        
        return max(res, top - temp)