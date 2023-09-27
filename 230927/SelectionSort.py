def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        # 현재 인덱스 이후의 부분에서 최솟값을 찾음
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # 최솟값을 현재 인덱스와 교환
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

lst = [11, 3, 24, 9, 40, 33, 7, 2, 8, 30]
print(selection_sort(lst))
