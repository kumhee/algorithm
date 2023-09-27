def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        # 현재 원소 이전의 정렬된 부분과 비교하여 위치 찾기
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key # 찾은 위치에 원소 삽입

    return arr

lst = [11, 3, 24, 9, 40, 33, 7, 2, 8, 30]
print(insertion_sort(lst))
