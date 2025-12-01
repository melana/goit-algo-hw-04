import timeit
import random

def insertion_sort(lst): # сортування вставками
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


def merge_sort(arr): # сортування злиттям
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def main():
    
    arr_100 = [random.randint(1, 100) for _ in range(100)]
    arr_1000 = [random.randint(1, 1000) for _ in range(1000)]
    arr_10000 = [random.randint(1, 10000) for _ in range(10000)]


    print("Виконаємо тестування для сортування масиву зі 100 елементів різними способами:")

    t100_is = timeit.timeit(lambda: insertion_sort(arr_100.copy()), number=1)
    print (t100_is) # 0.00011504699978104327

    t100_ms = timeit.timeit(lambda: merge_sort(arr_100.copy()), number=1)
    print (t100_ms) # 8.784800047578756e-05

    t100_ts = timeit.timeit(lambda: arr_100.copy().sort(), number=1)
    print (t100_ts) # 6.994001523707993e-06

    """ Висновок: для сортування масиву розміром 100 елементів 
    найшвидше працює вбудований алгоритм Timsort, найповільніше - сортування вставками """


    print("Виконаємо тестування для сортування масиву з 1000 елементів різними способами:")
    
    t1000_is = timeit.timeit(lambda: insertion_sort(arr_1000.copy()), number=1)
    print (t1000_is) # 0.009542056999634951

    t1000_ms = timeit.timeit(lambda: merge_sort(arr_1000.copy()), number=1)
    print (t1000_ms) # 0.0010530239997024182

    t1000_ts = timeit.timeit(lambda: arr_1000.copy().sort(), number=1)
    print (t1000_ts) # 7.488200026273262e-05

    """ Висновок: для сортування масиву розміром 1000 елементів 
    найшвидше працює вбудований алгоритм Timsort, найповільніше - сортування вставками """


    print("Виконаємо тестування для сортування масиву з 10000 елементів різними способами:")
    
    t10000_is = timeit.timeit(lambda: insertion_sort(arr_10000.copy()), number=1)
    print (t10000_is) # 0.996904605999589

    t10000_ms = timeit.timeit(lambda: merge_sort(arr_10000.copy()), number=1)
    print (t10000_ms) # 0.012617067999599385

    t10000_ts = timeit.timeit(lambda: arr_10000.copy().sort(), number=1)
    print (t10000_ts) # 0.000987411000096472
    
    """ Висновок: для сортування масиву розміром 10000 елементів 
    найшвидше працює вбудований алгоритм Timsort, найповільніше - сортування вставками """

    """ Загальні висновки: вбудований алгоритм Timsort працює найшвидше, 
    це видно при тестувані як з невеликими, так і з порівняно великими даними"""

if __name__ == "__main__":
    main()