# Dependencies installation

```bash command-line
pi@raspberry:~ $ sudo apt-get --assume-yes install python3-pip
pi@raspberry:~ $ sudo pip3 install pybluez
pi@raspberry:~ $ sudo apt-get --assume-yes install libboost-python-dev
pi@raspberry:~ $ sudo apt-get --assume-yes install libboost-thread-dev
pi@raspberry:~ $ sudo apt-get --assume-yes install libbluetooth-dev
pi@raspberry:~ $ sudo apt-get --assume-yes install libglib2.0
pi@raspberry:~ $ sudo pip3 install gattlib
pi@raspberry:~ $ git clone https://github.com/RoButton/switchbotpy.git
pi@raspberry:~ $ cd switchbotpy/
pi@raspberry:~/switchbotpy/ $ sudo python3 setup.py build
pi@raspberry:~/switchbotpy/ $ sudo python3 setup.py install
pi@raspberry:~/switchbotpy/ $ sudo pip3 install python-telegram-bot --upgrade
``` 

# How to run manually

```bash
sudo nohup python3 apri-portone.py --mac <SWITCHBOT::BLUETOOTH::MAC::ADDRESS> --password "<switchbot-password>" --token <telegram-token> > nohup.log &
```

Make sure that:

1. SwitchBot MAC address is all UPPERCASE
1. SwitchBot password is enclosed in double quotes

# How to run at system startup

We can use systemctl to configure switchbot (aka apri-portone.py) to be started up at system boot. Modify the switch-bot.service file from this repo to 
to use your switchbot MAC Address, password and Telegram BOT API Token. *Heads-up* systemctl service file will not need double quotes around Switchbot password!

```bash command-line
pi@raspberry:~/switch-bot-telegram $ sudo cp switch-bot.service /etc/systemd/system/
pi@raspberry:~/switch-bot-telegram $ sudo systemctl start switch-bot.service
pi@raspberry:~/switch-bot-telegram $ sudo systemctl enable switch-bot.service
``` 

## Updating systemctl service file

If you should happen to change the switch-bot.service file, you would then need to have it reloaded by systemctl as follows:
```bash
sudo systemctl daemon-reload
``` 

## Reading log messages
You can see switch-bot.service related logs via `journalctl`. As a sample, following command follows logs for switch-bot.service, starting from the current system boot:
```bash command-line
pi@raspberry:~ $ journalctl -u switch-bot.service -b -f
-- Logs begin at Thu 2019-02-14 10:11:59 GMT. --
Dec 13 08:49:54 tre14 systemd[1]: Stopping switchbot...
Dec 13 08:49:56 tre14 systemd[1]: switch-bot.service: Succeeded.
Dec 13 08:49:56 tre14 systemd[1]: Stopped switchbot.
Dec 13 08:49:56 tre14 systemd[1]: Started switchbot.
Dec 13 08:50:59 tre14 sudo[1289]:     root : TTY=unknown ; PWD=/home/pi/git/switch-bot ; USER=root ; COMMAND=/usr/bin/systemctl restart bluetooth
Dec 13 08:50:59 tre14 sudo[1289]: pam_unix(sudo:session): session opened for user root by (uid=0)
Dec 13 08:50:59 tre14 sudo[1289]: pam_unix(sudo:session): session closed for user root
Dec 13 08:50:59 tre14 sudo[1292]:     root : TTY=unknown ; PWD=/home/pi/git/switch-bot ; USER=root ; COMMAND=/usr/bin/hciconfig hci0 reset
Dec 13 08:50:59 tre14 sudo[1292]: pam_unix(sudo:session): session opened for user root by (uid=0)
Dec 13 08:50:59 tre14 sudo[1292]: pam_unix(sudo:session): session closed for user root
```

# Tested on

This code has lastly been tested on 12-Dec-2020 on a RaspberryPI 3 mod B v2 with Raspbian GNU/Linux 10 (buster)
