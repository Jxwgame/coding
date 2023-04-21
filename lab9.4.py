def card(card):
    set01 = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "10":9, "J":10, "Q":11, "K":12, "A":13}
    set02 = {"♣":0, "♦":1, "♥":2, "♠":3}
    return(set01[card[:-1]], set02[card[-1]])
def insertionSort(list, last):
    comparisons = 0
    for i in range(1, last+1):
        key = list[i]
        j = i-1
        while j >= 0 and card(key) < card(list[j]):
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
            if card(list[min_index]) > card(list[j]):
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
            if card(list[walker]) < card(list[walker - 1]):
                sorted = False
                list[walker], list[walker - 1] = list[walker - 1], list[walker]
            walker -= 1
            c += 1
        current += 1
        print(list)
    print("Comparisons times: %s" %c)

def main():
    insertionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
    selectionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
    bubbleSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
main()