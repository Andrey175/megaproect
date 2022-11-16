##new_list = num_list.sort()  # 1 вариант сортировка через медод sort

def bubble_sorting(a): # 2 вариант сортировка пузырьком
    b = len(a) -1
    for z in range(0, b):
        for x in range(0, b -z):
            if a[x] > a[x + 1]:
                a[x], a[x +1] = a[x +1], a[x]
    return a


def binary_search(array, element, start, stop):
    if start > stop:
        return False       
    else:
        mid = (start + stop)//2
        if element == array[mid]:
            return mid
        elif element < new_list[mid]:
            return binary_search(array, element, start, mid-1)
        else:
            return binary_search(array, element, mid+1, stop)
        
def result(x):
    if x == False:
        for i in new_list:
            if element < i:
                j = binary_search(new_list, i, 0, len(new_list)) 
                print("Число", element, "отсутствует в массиве списка, \nменьшее число -", new_list[j-1], "под индексом -", j-1,"\nбольшее число -",new_list[j],"под индексом -",j )
                break 
    else:
        print("Число", element, "находиться под индексом", index)

num_list = list(map(int, input("Введите список чисел, разделенных пробелом: ").split()))
print("Список чисел: ", num_list)
        
new_list = bubble_sorting(num_list).copy()
print("Сортировка списка по возрастанию: ", new_list)

element = int(input("Введите любое число: "))
if element > new_list[-1] or element < new_list[0]:
    print("Введеное число не входит в диапазон представленных в массиве списка ")
elif element == new_list[0]:
    w = binary_search(new_list, element, 0, len(new_list))
    print("Число", element, "находиться под индексом",w)
else:
    index =  binary_search(new_list, element, 0, len(new_list))
    result(index)

