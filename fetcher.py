import requests
import json

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
        all_commits = 0
        for item in json_data:
            repo = item['name']
            # print(repo)
            repo_commits = len(get_data("https://api.github.com/repos/ippanpeople/%s/commits"%(repo)))
            all_repos.append(repo)
            all_commits += repo_commits
        # print(all_repos) # 某用户的所有repo列表
        # print( "the %s totally has %d repos and %d commits" %(name,len(all_repos), all_commits) )
        return name, all_repos, all_commits

    except Exception as e:
            print(e)

if __name__ == "__main__":
    # date = json.loads(get_data("https://api.github.com/repos/ippanpeople/Github-Fetcher/commits"))
    # print(type(date))
    # print(len(date))
    # print(type(get_all_repo("ippanpeople")))
    github_info = get_all_repo("ippanpeople")
    print("the %s totally has %d repos and %d commits" %(github_info[0],len(github_info[1]), github_info[2]))