class Solution1:
    def minMaxDifference(self, num: int) -> int:
        result = []
        num = str(num)
        min_val = int(num.replace(num[0], '0'))
        max_val = 0
        for i in range(10):
            for j in range(10):
                val = int(num.replace(str(i), str(j)))
                if val > max_val:
                    max_val = val

        return max_val - min_val


# REF
class Solution2:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        i = 0
        # 앞 자리부터 순차대로 탐색하여 9가 아닐 경우의 값을 i에 저장
        while num[i] == "9" and i < len(num)-1:
            i += 1

        return int(num.replace(num[i], "9")) - int(num.replace(num[0], "0"))
