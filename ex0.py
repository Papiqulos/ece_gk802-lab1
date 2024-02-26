import requests  # εισαγωγή της βιβλιοθήκης


def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break
    


if __name__ == '__main__':

    # url = input('Enter URL: ')
    url = 'http://google.com/'

    with requests.get(url) as response:  # το αντικείμενο response
        html = response.text
        # more(html)
        # print(response.headers)
        server = response.headers['Server']
    
        print(f"Web Server: {server}")
        
        try:
            biscuits = response.headers["Set-Cookie"]
            print(f"Cookies: {biscuits.split(';')[0]}")
            print(f"Expires: {biscuits.split(';')[1]}")
        except KeyError:
            print("Cookie header not found")
