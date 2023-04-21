def insertionSort(list, last):
    comparisons = 0
    for i in range(1, last+1):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
            comparisons += 1
        list[j+1] = key
        print(list)
    if comparisons == 0:
        comparisons = last
    else:
        comparisons = comparisons + last - 1
    print("Comparison times:", comparisons)

def selectionSort(list, last):
    comparisons = 0
    for i in range(last):
        min_index = i
        for j in range(i+1, last+1):
            if list[min_index] > list[j]:
                min_index = j
            comparisons += 1
        list[i], list[min_index] = list[min_index], list[i]
        print(list)
    print("Comparison times:", comparisons)

def bubbleSort(list, last):
    current = 0
    c = 0
    sorted = False
    while current <= last and sorted == False:
        walker = last
        sorted = True
        while walker > current:
            if list[walker] < list[walker - 1]:
                sorted = False
                list[walker], list[walker - 1] = list[walker - 1], list[walker]
            walker -= 1
            c += 1
        current += 1
        print(list)
    print("Comparisons times: %s" %c)

def main():
    insertionSort([23, 78, 45, 8, 32, 56], 5)
    selectionSort([23, 78, 45, 8, 32, 56], 5)
    bubbleSort([23, 78, 45, 8, 32, 56], 5)

main()  