### Питхон

---
Выдать участникам файл main.py
---
1. Содержимое главной функции:
```python
def main():
    input_value = input("Введите флаг: ")
    if check_flag(input_value):
        print("OK!")
    else:
        print("Nope(")

```
- Видим, что программа получает на вход флаг и проверяет его в функции check_flag()
2. Смотрим функцию  check_flag()
```python
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
```
- Видим, что функция берет введенные данные и выполняет циклический сдвиг по алфавиту на 41 влево(омагад, это что, шифр Цезаря??????)
3. Обратим алгоритм, скрипт для решения выглядит слеудющим образом (сдвинем конечную строку обратно на 41 вправо)
```python
encr = 'AG5B{VBV_OW_7COV_MYQYMNYM?}'
alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
flag = ''
for i in encr:
    if i in alph:
        new_index = (alph.find(i) + 41) % len(alph)
        flag += alph[new_index]
    else:
        flag += i
print(flag)
```

Flag: FLAG{0G0_T1_CHT0_R3V3RS3R?}