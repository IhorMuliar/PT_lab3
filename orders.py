def maxrnge(lst):
    if len(lst) >= 10:
        return False
    else:
        return True

def minrnge(lst):
    if len(lst) <= 0:
        return False
    else:
        return True

def ifexits(lst, a):
    if lst.count(a) < 1:
        return True
    else:
        return False

def show(lst):
    return', '.join(str(value) for value in lst)



if __name__ == '__main__':

    lst = ["106", "107"]
    while True:
        print("\n-------------------------\n")
        print("Tenepiшнiй стан черги: \n", show(lst))
        dia = input("Введіть дію (1 - додати замовлення в кінець черги, 2 - показати замовлення перше, 3 - завершити виконаня: ")
        if dia == "1":
            if maxrnge(lst):
                inf = input("Номер замовлення: ")
                if ifexits(lst, inf):
                    lst.append(inf)
                else:
                    print("\nВже в черзі\n")
            else:
                print("\nЧерга вже повна\n")
        elif dia == "2":
            if minrnge(lst):
                print("\nЗараз: ", lst[0])
            else:
                print("\nЧерга пуста")
        elif dia == "3":
            if minrnge(lst):
                print("Delete: ", lst.pop(0))
            else:
                print("\nQue is empty\n")
