def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    html = requests.get(url, headers=headers) # 发送请求
    if html.status_code == 200: # 判断请求是否成功
        # print(html)
        return html.content # 返回网页内容
    else:
        return None

if __name__ == "__main__":
    get_data("https://api.github.com/repos/ippanpeople/Nginx_Configration/commits")