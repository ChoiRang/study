from itertools import combinations_with_replacement


# n : 화살 갯수, info : 어피치가 쏜 과녁 정보
def solution(n, info):
    answer = [0 for _ in range(11)]
    win = False
    max_num = 0  # 라이언이 이길 때 가장 큰 점수 차이
    # 중복 조합을 사용하여 라이언의 모든 가능한 점수 만들기
    for res in list(combinations_with_replacement(range(11), n)):
        now = [0 for _ in range(11)]
        for r in res:
            now[10-r] += 1

        lion, peach = 0, 0

        # 2. 라이언, 어피치 점수 비교
        for i, (l, p) in enumerate(zip(now, info)):
            if l == p == 0:
                continue
            if p >= l:
                peach += (10-i)
            elif l > p:
                lion += (10-i)
        # 3. 최종점수 계산, 라이언이 큰 경우 -> 결과 없데이트
        if lion > peach:
            win = True
            if (lion - peach) > max_num:
                max_num = lion = peach
                answer = now
    if not win:
        return [-1]

    return answer


from copy import deepcopy

max_num, max_board = 0, []


def solution2(n, info):
    def dfs(ascore, lscore, cnt, idx, board):
        global max_num, max_board
        if cnt > n:
            return

        if idx > 10:
            diff = lscore - ascore
            if diff > max_num:
                board[10] = n - cnt     # 남은 화살을 모두 0점에 쏴라
                max_board = board
                max_num = diff
            return

        # 어피치 보다 1발더 쏠때
        if cnt > n:
            cboard = deepcopy(board)
            cboard[10-idx] = info[10-idx] + 1
            dfs(ascore, lscore+idx, cnt+info[10-idx], idx+1, cboard)

        # 해당과녁 정보다 0 또는 0이 아님
        ccboard = deepcopy(board)
        if info[10-idx] > 0:
            dfs(ascore+idx, lscore, cnt, idx+1, ccboard)
        else:
            dfs(ascore, lscore, cnt, idx+1, ccboard)    # 둘다 0점

    dfs(0, 0, 0, 0, [0]*11)

    if max_board:
        return max_board
    else:
        return [-1]
