# RCON Discord Bot

Данный бот создан для удалённого выполнения команд от имени администратора на игровых серверах в Warnament. Реализовать это позволяет протокол RCON который есть в ядре TCORE.

## Установка
#### Linux
```
sudo apt install python3.9
sudo apt install python3-pip
git clone https://github.com/Explorer-art/RCON-Discord-Bot.git
cd RCON-Discord-Bot
pip install -r requirements.txt
chmod +x start.sh
./start.sh
```

#### Windows
```
git clone https://github.com/Explorer-art/RCON-Discord-Bot.git
cd RCON-Discord-Bot
pip install -r requirements.txt
start.bat
```

## Настройка
Откройте файл config.py
Измените токен бота, список разрешённых ID пользователей, айпи и порт сервера и RCON пароль (порт веб-сервера 9001)
 
## Использование
Введите в чат команду /rcon [команда] (команды писать без /).
