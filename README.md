# instagram_bot
An instagram bot to automate the boring stuff for you.


## Setup

1. Clone the repo if you haven't already.
```
$ git clone https://github.com/iBvishal/instagram_bot.git
```

2. Install dependencies.
```
$ cd instagram_bot
$ pip install -r requirements.txt
```

3. Install Geckodriver.
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.23.0-linux64.tar.gz -O > /usr/bin/geckodriver'
sudo chmod +x /usr/bin/geckodriver
rm geckodriver-v0.23.0-linux64.tar.gz
```

4. Replace your login credentials in bot.py and run bot.py.
```
$ python bot.py
```

### Show some :heart: and do star the repo