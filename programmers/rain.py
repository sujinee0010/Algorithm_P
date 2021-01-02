
buildings =[3,1,2,3,4,1,1,2]

def rain (buildings):
    """
    i 기준으로 왼 , 오 의 max 값을 구한다
    둘중에 작은 거 에서 i 높이를 빼면 됨

    """
    sum = 0
    for i in range(len(buildings)):
        left = max(buildings[:i+1])
        right = max(buildings[i:])

        low = min(left,right)
        sum += low - buildings[i]
    return sum


if __name__ == '__main__':
    H, W = map(int, input().split())  # 세로 가로
    buildings = list(map(int, input().split()))
    answer = rain(buildings)
    print(answer)

