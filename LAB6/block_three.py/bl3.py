
string = input("Введите строку с одной открывающей и одной закрывающей скобкой: ")


open_index = string.find('(')
close_index = string.find(')')


if open_index != -1 and close_index != -1 and open_index < close_index:

    inside = string[open_index + 1:close_index]
    print("Символы внутри скобок:", inside)
else:
    print("Строка некорректна. Убедитесь, что есть одна пара скобок.")