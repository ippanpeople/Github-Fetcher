import requests

def get_data(url):
    headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
              }
    html = requests.get(url, headers=headers) # 发送请求
    if html.status_code == 200: # 判断请求是否成功
        # print(html)
        return html.content # 返回网页内容
    else:
        return None

def get_all_repo(name): # 某人所有的repo
    url_repos = 'https://api.github.com/users/{name}/repos'.format(name=name)
    html = get_data(url_repos)

    json_data = json.loads(html)
    # json_data里储存的是html下的所有数据
    all_repos = [] # repos's name数据存放数组

    try:
        for item in json_data:
            repo = item['name']
            all_repos.append(repo)
        print(all_repos) # 某用户的所有repo列表
        print( "the %s totally has %d repos" %(name,len(all_repos)) )
        return name,all_repos

    except Exception as e:
            print(e)

if __name__ == "__main__":
    print(get_data("https://api.github.com/repos/ippanpeople/Nginx_Configration/commits"))