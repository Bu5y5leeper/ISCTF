## WriteUP
- Смотрим на название и понимаем, что надо посмотреть директории. Будем использовать dirb(или dirsearch).
```
$ dirb http://194.87.101.168:8081/
или
# dirsearch -u http://194.87.101.168:8081/
```
- Запускаем скан и ждем.
  <img width="493" alt="Снимок экрана 2024-09-16 в 14 51 19" src="https://github.com/user-attachments/assets/1eb94690-ce99-4b4c-ac81-ca91cc7865fd">
- Переходим по admindb и видим флаг!
  <img width="1432" alt="Снимок экрана 2024-09-16 в 14 55 29" src="https://github.com/user-attachments/assets/e31e4d81-17b6-4470-9f70-2cdff22d9589">
