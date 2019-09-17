initial = [3, 25, 80, 17]
nucleus = int(input("Введите атомный номер элемента: "))
if nucleus == initial[0]:
    print("Li")
elif nucleus == initial[1]:
    print("Mn")
elif nucleus == initial[2]:
    print("Hg")
else:
    print("Cl")
