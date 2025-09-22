n = int(input())
arr = list(map(int, input().split()))

def heapify(arr, n, i):
    largest = i        # 루트 노드 인덱스
    left = 2 * i + 1   # 왼쪽 자식
    right = 2 * i + 2  # 오른쪽 자식

    # 왼쪽 자식이 루트보다 크면 largest 업데이트
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 largest보다 크면 업데이트
    if right < n and arr[right] > arr[largest]:
        largest = right

    # largest가 루트가 아니면 swap하고 재귀 호출
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # 1️⃣ 배열을 최대 힙으로 만들기
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2️⃣ 힙에서 하나씩 요소 꺼내서 끝에 정렬
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 가장 큰 값(루트)과 마지막 값 교환
        heapify(arr, i, 0)  # 남은 힙을 다시 정렬

heap_sort(arr)
print(*arr)