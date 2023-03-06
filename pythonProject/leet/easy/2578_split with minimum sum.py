class Solution:
    def splitNum(self, num: int) -> int:
        num_list = [int(i) for i in str(num)]
        num_list.sort()
        left, right = 0, 0
        N = len(num_list)
        for i in range(N):
            if i % 2 == 0:
                left *= 10
                left += num_list[i]
            else:
                right *= 10
                right += num_list[i]

        return left+right
