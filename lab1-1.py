import requests  
import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break
    

def get_headers(url):
    with requests.get(url) as response:  
        print("--------------------")
        headers = response.headers
        print("Headers: ")
        for key, value in headers.items():
            print(f"{key:30s}: {value}")


def get_server(url):
    with requests.get(url) as response:  
        server = response.headers['Server']
        print("--------------------")
        print(f"Web Server: {server}")


def get_cookies(url):
    with requests.get(url) as response:
        try:
            cookies = response.cookies
            for cookie in cookies:
                date = datetime.datetime.fromtimestamp(cookie.expires).strftime('%Y-%m-%d %H:%M:%S')
                print(f"Cookie Name: {cookie.name}")
                print(f"Expiration Date: {date}")
                print("--------------------")
        except:
            print("No cookies found")


if __name__ == '__main__':

    # url = input('Enter URL: ')
    url = "https://www.google.com"
    
    get_headers(url)
    
    get_server(url)
    
    get_cookies(url)
