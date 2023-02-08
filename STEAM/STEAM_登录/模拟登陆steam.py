import time
import execjs
import requests

login_url = 'https://store.steampowered.com/login/dologin/'
get_rsa_key_url = 'https://store.steampowered.com/login/getrsakey/'

headers = {
    'Host': 'store.steampowered.com',
    'Origin': 'https://store.steampowered.com',
    'Referer': 'https://store.steampowered.com/login/?redir=&redir_ssl=1&snr=1_4_4__global-header',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}
session = requests.session()

def get_rsa_key(username):
    data = {
        'donotcache': str(int(time.time() * 1000)),
        'username': username
    }
    response = session.post(url=get_rsa_key_url, data=data, headers=headers).json()
    print(response)
    return response

def get_encrypted_password(password, rsa_key_dict):
    f = open('steam.js', 'r', encoding='utf-8')
    steampowered_js = f.read()
    f.close()
    encrypted_password = execjs.compile(steampowered_js).call('OnAuthCodeResponse', password, rsa_key_dict)
    return encrypted_password

def login(username, encrypted_password, rsa_key_dict):
    data = {
        'donotcache': str(int(time.time() * 1000)),
        'password': encrypted_password,
        'username': username,
        'twofactorcode': '',
        'emailauth': '',
        'loginfriendlyname': '',
        'emailsteamid': '',
        'rsatimestamp': rsa_key_dict['timestamp'],
        'remember_login': False,
        'tokentype': '-1'
    }
    print(data)
    response = session.post(url=login_url, data=data, headers=headers)
    print(response.text)

def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')

    # 获取 RSA 加密所需 key 等信息
    rsa_key_dict = get_rsa_key(username)

    # 获取加密后的密码
    encrypted_password = get_encrypted_password(password, rsa_key_dict)
    # print(encrypted_password)
    # 携带 用户名、加密后的密码、cookies、验证码等登录
    login(username, encrypted_password, rsa_key_dict)

if __name__ == '__main__':
    main()