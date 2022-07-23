import requests
from twocaptcha import TwoCaptcha


def login(twocaptcha_api_key, mail_address, password, proxies=None):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    if proxies is None:
        response = requests.get('https://gametrade.jp/signin', headers=headers)

    else:
        response = requests.get('https://gametrade.jp/signin', headers=headers, proxies=proxies)

    session_id = response.cookies.get_dict()["_session_id"]
    authenticity_token = response.text.split('"csrf-token" content="')[1].split('"')[0]

    solver = TwoCaptcha(twocaptcha_api_key)
    result = solver.recaptcha(url='https://gametrade.jp', sitekey="6Lckg8cZAAAAAB59DnqTKd5I21URI80QT5HuI5zx")
    recaptcha_response = result["code"]

    cookies = {
        '_session_id': session_id,
    }

    data = {
        'utf8': '✓',
        'authenticity_token': authenticity_token,
        'session[email]': mail_address,
        'session[password]': password,
        'g-recaptcha-response': recaptcha_response,
    }

    if proxies is None:
        response = requests.post('https://gametrade.jp/signin', cookies=cookies, headers=headers, data=data, allow_redirects=False)
    else:
        response = requests.post('https://gametrade.jp/signin', cookies=cookies, headers=headers, data=data, allow_redirects=False, proxies=proxies)

    if "remember_token" in str(response.cookies):
        remember_token = response.cookies.get_dict()["remember_token"]
        return remember_token
    else:
        return "Failed"


def favorite(remember_token, URL, proxies=None):

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    if proxies is None:
        response = requests.get(URL, headers=headers)

    else:
        response = requests.get(URL, headers=headers, proxies=proxies)

    session_id = response.cookies.get_dict()["_session_id"]
    authenticity_token = response.text.split('"csrf-token" content="')[1].split('"')[0]

    cookies = {
        '_session_id': session_id,
        'remember_token': remember_token,
    }

    headers = {
        'accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-csrf-token': authenticity_token,
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'utf8': '✓',
        'button': '',
    }

    ID = str(URL).split("/")[5]

    if proxies is None:
        response = requests.post('https://gametrade.jp/exhibits/' + ID + '/thinkings', cookies=cookies, headers=headers,
                                data=data, allow_redirects=False)
    else:
        response = requests.post('https://gametrade.jp/exhibits/' + ID + '/thinkings', cookies=cookies, headers=headers,
                                data=data, proxies=proxies, allow_redirects=False)

    if response.status_code == 200:
        return "Success"
    else:
        return "Failed"


def unfavorite(remember_token, URL, proxies=None):

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    if proxies is None:
        response = requests.get(URL, headers=headers)

    else:
        response = requests.get(URL, headers=headers, proxies=proxies)

    session_id = response.cookies.get_dict()["_session_id"]
    authenticity_token = response.text.split('"csrf-token" content="')[1].split('"')[0]

    cookies = {
        '_session_id': session_id,
        'remember_token': remember_token,
    }

    headers = {
        'accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-csrf-token': authenticity_token,
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'utf8': '✓',
        '_method': 'delete',
        'button': '',
    }

    ID = str(URL).split("/")[5]

    if proxies is None:
        response = requests.post('https://gametrade.jp/exhibits/' + ID + '/thinkings', cookies=cookies, headers=headers,
                                data=data, allow_redirects=False)
    else:
        response = requests.post('https://gametrade.jp/exhibits/' + ID + '/thinkings', cookies=cookies, headers=headers,
                                data=data, proxies=proxies, allow_redirects=False)

    if response.status_code == 200:
        return "Success"
    else:
        return "Failed"


def update(remember_token, URL, proxies=None):
    print("欲しい人10万円で売るよ！" + remember_token + URL + proxies)

