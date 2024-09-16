def check_flag(in_str):
    alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_string = ''
    for i in in_str:
        if i in alph:
            new_index = (alph.find(i) - 41) % len(alph)
            new_string += alph[new_index]
        else:
            new_string += i
    if new_string == 'AG5B{VBV_OW_7COV_MYQYMNYM?}':
        return True
    return False

def main():
    input_value = input("Введите флаг: ")
    if check_flag(input_value):
        print("OK!")
    else:
        print("Nope(")

main()
