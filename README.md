#RCON Discord Bot#

Данный бот создан для удалённого выполнения команд от имени администратора на игровых серверах в Warnament. Реализовать это позволяет протокол RCON который есть в ядре TCORE.

##Установка##
#####Linux#####
```
sudo apt install python3.9
sudo apt install python3-pip
git clone https://github.com/Explorer-art/RCON-Discord-Bot.git
cd RCON-Discord-Bot
pip install -r requirements.txt
chmod +x start.sh
./start.sh
```

#####Windows#####
```
git clone https://github.com/Explorer-art/RCON-Discord-Bot.git
cd RCON-Discord-Bot
pip install -r requirements.txt
```
После выполнения этих команд запускаем файл start.bat

##Использование##
Добавьте бота на сервер, измените токен бота и свой ID в bot.py, запустите его и введите команду /rcon [команда] (команды вводить без /)
