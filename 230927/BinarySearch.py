def binary_search(array, target, low=None, high=None):
    # 초기값 설정
    if low is None:
        low = 0
    if high is None:
        high = len(array) - 1

    # 기저 조건: 검색 범위가 역전된 경우
    if high < low:
        return False
    
    # 중간 지점 계산
    mid = (low + high) // 2
    print(array[mid], end=' ')

    # 찾고자 하는 값과 중간 값 비교
    if target == array[mid]:
        return True
    elif target < array[mid]:
        # 중간 값보다 작으면 왼쪽 반쪽에서 재귀 탐색
        return binary_search(array, target, low, mid - 1)
    else:
        # 중간 값보다 크면 오른쪽 반쪽에서 재귀 탐색
        return binary_search(array, target, mid + 1, high)

# 테스트 케이스
lst = [1, 3, 4, 9, 10, 13, 17, 24, 28, 30]
print(binary_search(lst, 4))  # True
print(binary_search(lst, 30))  # True
print(binary_search(lst, 38))  # False
