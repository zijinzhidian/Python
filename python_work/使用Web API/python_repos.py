import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

#发送请求并获取请求结果
r = requests.get(url)

#状态码
print("Status code:",r.status_code)

#json数据--->字典
response_dict = r.json()

print(response_dict.keys())

#Python仓库总数
print("Total repositories:", response_dict['total_count'])

#探索有关仓库信息items
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

#获取仓库的名字和星数
names ,stars = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

#样式
my_style = LS('#333366', base_style=LCS)

#参数设置
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend=False    #隐藏图例


#直方图
chart = pygal.Bar(my_config ,style=my_style)

chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')
