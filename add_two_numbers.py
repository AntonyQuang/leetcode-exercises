def add_two_numbers(l1: list, l2: list) -> list:
    number_1 = ""
    number_2 = ""
    for digit in l1[::-1]:
        number_1 += f"{digit}"
    for digit in l2[::-1]:
        number_2 += f"{digit}"

    total = str(int(number_1) + int(number_2))
    output = [int(digit) for digit in total[::-1]]
    print(output)


add_two_numbers(l1=[2, 4, 3], l2=[5, 6, 4])
add_two_numbers(l1=[0], l2=[0])
add_two_numbers(l1=[9, 9, 9, 9, 9, 9, 9], l2=[9, 9, 9, 9])
