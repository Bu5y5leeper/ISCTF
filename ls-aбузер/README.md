### ls-aбузер
---
Для запуска задания прописать:
```bash 
docker compose up -d
```
Задание поднимется по адресу http://127.0.0.1:5000/
---
1. Открываем главную страницу с формой, которая принимает путь в файловой системе
  ![изображение](https://github.com/user-attachments/assets/ed573a07-1a2a-46c0-b935-8cb16a6a8478)
2. Вывод крайне похож на вывод команды ls
  ![изображение](https://github.com/user-attachments/assets/37fccc17-5a13-4a7e-891c-25b2dcc3b1b5)
3. После некотторого поиска осознаем, что имеем дело с command injection. 
4. Проверим гипотезу с помощью ввода "; whoami"
  ![изображение](https://github.com/user-attachments/assets/79fa90a0-5732-44af-bda1-d213da0d75d1)
7. Действительно, все что мы вводим выполняется в оболочке линукса
8. Попробуем посмотреть скрытые файлы с помощью ";ls -a"
  ![изображение](https://github.com/user-attachments/assets/e700277c-8c01-42d2-a0e5-aef22195007f)
10. Победа - нашли файл с флагом. Смотрим его с помощью "; cat ./.flag.txt"
  ![изображение](https://github.com/user-attachments/assets/0a1eabcf-9956-4e84-b355-78d3e44e4107)

Flag: FLAG{CAT_ILI_NE_CAT_VOT_V_CHEM_VOPROS}
