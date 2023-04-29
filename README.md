# Задание 18
Решили делать бота в Telegram. Для модерации и создания мероприятий будет написан frontend и backend

## Подробнее:

4 статуса пользователя (о каждом сейчас расскажу):

### Статус user: 

- Делает базовые вещи по типу поиска мероприятий

### Статус creator:

- Может создать свое мероприятие. Для этого он вводит соответствующую команду, бот отправляет ему кнопку с веб-аппом, в котором креатор регистрируется или входит в свою учетку. может видеть свои мероприятия и создать новое

### Статус moderator:

- Может отклонять и принимать мероприятия. Все в веб админке

### Статус admin:

- Может делать тоже самое, что и модер, но еще удалять модераторов

## Стэк:

- Python
- Aiogram
- Flask
- SQLAlchemy
- PostgreSQL
- HTML
- CSS
- AnimateCSS

