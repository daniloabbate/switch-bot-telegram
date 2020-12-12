# Dependencies installation

```bash
sudo apt-get --assume-yes install python3-pip
sudo pip3 install pybluez
sudo apt-get --assume-yes install libboost-python-dev
sudo apt-get --assume-yes install libboost-thread-dev
sudo apt-get --assume-yes install libbluetooth-dev
sudo apt-get --assume-yes install libglib2.0
sudo pip3 install gattlib
git clone https://github.com/RoButton/switchbotpy.git
cd switchbotpy/
sudo python3 setup.py build
sudo python3 setup.py install
sudo pip3 install python-telegram-bot --upgrade
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

```bash
sudo cp switch-bot.service /etc/systemd/system/
sudo systemctl start switch-bot.service
sudo systemctl enable switch-bot.service
``` 

If you should happen to change the switch-bot.service file, you would then need to have it reloaded by systemctl as follows:
```bash
sudo systemctl daemon-reload
``` 

# Tested on

This code has lastly been tested on 12-Dec-2020 on a RaspberryPI 3 mod B v2 with Raspbian GNU/Linux 10 (buster)
