#m3gon
#import lib
#try
import time
try:
    from colorama import Fore
    import colorama
    colorama.init(autoreset=colorama)
except:
    print(Fore.LIGHTRED_EX+f'[-] {Fore.RESET}pip install colorama')
    exit(0)
try:
    import requests
except:
    print(Fore.LIGHTRED_EX+f'[-] {Fore.RESET}pip install requests')
    exit(0)
def banner():
    Bb = Fore.LIGHTYELLOW_EX
    print(Bb + """
        __  __ ____   _____  ____  _   _ 
        |  \/  |___ \ / ____|/ __ \| \ | |
        | \  / | __) | |  __| |  | |  \| |
        | |\/| ||__ <| | |_ | |  | | . ` |
        | |  | |___) | |__| | |__| | |\  |
        |_|  |_|____/ \_____|\____/|_| \_|
    """, Fore.LIGHTGREEN_EX + "\n                  ( @_m3gon )",
          Fore.LIGHTBLUE_EX + "\n   (This tool is programmed by the programmer : @_m3gon)              \n",
          Fore.LIGHTYELLOW_EX + "          ( Check Emails Instagram )\n\n" + Fore.RESET)
banner()
def open_file_emails():
    try:
        name_file = input('[?] Enter the name of the email file : ')
        open_file = open(name_file).read().splitlines()
        for file_emails in open_file:
            def check_email_instagram():
                url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'no-cache',
                    'content-length': '65',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_did=E1069C00-B44A-4C3C-AEC6-2EDFF828476E; mid=YFNJ-gALAAFOnl3VaylOWdyOj2VX; ig_nrcb=1; shbid=19035; shbts=1618983571.4369197; rur=FRC; csrftoken=75w240jkIcjHprthgBk5cRirROsosVzI',
                    'origin': 'https://www.instagram.com',
                    'pragma': 'no-cache',
                    'referer': 'https://www.instagram.com/accounts/emailsignup/',
                    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
                    'x-csrftoken': '75w240jkIcjHprthgBk5cRirROsosVzI',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': 'hmac.AR1YTbiNiOj-oFmz6or5-aLaGeSG8E7Lsos9CcSReFXVmszR',
                    'x-instagram-ajax': 'e7396eb67b88',
                    'x-requested-with': 'XMLHttpRequest'
                }
                data =  {
                    'email': file_emails,
                    'username': '',
                    'first_name': '',
                    'opt_into_one_tap': 'false'
                }
                response = requests.post(url, data=data, headers=headers).text
                if '"code": "email_is_taken"' in response:
                    print(Fore.LIGHTRED_EX+f'[-] {Fore.RESET}Email Taken : {file_emails}')
                else:
                    print(Fore.LIGHTGREEN_EX+f'[+] {Fore.RESET}Email Available : {file_emails}')
                    with open('Email_Available.txt', 'a') as email:
                        email.write(f'[+] Email Available : {file_emails}' + '\n')
            check_email_instagram()
    except:
        print(f'[-] Not Found File {name_file}')
        exit(0)
open_file_emails(jdndjjdjd@gmail.com jdjfbf@gmail.com)
