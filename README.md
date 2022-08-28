### Небольшой парсер канала.

Проверяет изменение аватарки и названия канала раз в 30секунд

Настройка:
1. Зарегаться и получить `API_ID` и `API_HASH` по ссылке:  https://core.telegram.org/
1. Создать файл `dot.env` в котором прописать переменные:

```bash

TELEGRAM_API_ID=00000000
TELEGRAM_API_HASH=00000000
TELEGRAM_SESSION_NAME=my_session
SEND_TO_CHANNEL=me
CHANNEL_URL=@example_channel

```

`SEND_TO_CHANNEL` - можно указать номер телефона, указать `me` или указать канал
`TELEGRAM_SESSION_NAME` - произвольное название для сессии