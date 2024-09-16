## WriteUP
- Заходим на сайт и видим set cookie, и это сильный намек! Запускаем burpsuite и смотрим что нам приходит.
  <img width="1165" alt="Снимок экрана 2024-09-16 в 15 10 55" src="https://github.com/user-attachments/assets/c0830e5a-a6a5-4e7c-a97c-aea546881baf">

- Опа! Видим в куках значение admin = false, кидаем запрос в репитер и меняем false на тру и отправляем новый запрос
<img width="1511" alt="Снимок экрана 2024-09-16 в 15 11 49" src="https://github.com/user-attachments/assets/7f9f493f-5eeb-4386-9c96-adddcb0a36db">
<img width="586" alt="Снимок экрана 2024-09-16 в 15 12 07" src="https://github.com/user-attachments/assets/c7dbe38c-0844-4a30-b209-bdfc370e92ae">
