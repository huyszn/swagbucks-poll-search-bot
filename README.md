# Swagbucks Poll and Search Bot

(Use at your own risk, I'm not responsible if anything happens to your account)

A bot to help you complete your daily Swagbucks poll for 1 SB and your two daily search wins for around 10 SB+ in ~10 minutes. This should earn you 10+ SB every day if you run `sb-poll-search.py` or `sb-poll-search-2.py`. If you want to have more control over the bot, then run `sb-poll-search-2.py`. Note that you will have to manually claim the SB for the two daily search wins by clicking on the 'Claim My SB' button (on the 4th search and final search) and possibly entering a captcha code.


## Setup the bot

### Requirements

```
$ pip install -r requirements.txt
```

### config.py

```
$ touch config.py
```
Copy the contents of `config-example.py` into `config.py`. <br/>

```
EMAIL = 'your email'
PASSWORD = 'your password'
```

Replace the `EMAIL` and `PASSWORD` fields with your account email and password.


## Run the bot

more automated
```
$ python3 sb-poll-search.py
```

or more manual
```
$ python3 sb-poll-search-2.py
```

Click on the 'Claim My SB' button when it pops up on your page

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details