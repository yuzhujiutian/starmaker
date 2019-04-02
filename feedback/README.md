#### 环境准备
1.  安装git环境，保证自己的账号有qa repo的权限，repo地址`ssh://git@phabricator.ushow.media/source/starmaker-qa.git`
2.  安装python 2.7版本，如果是python 3.0版本以上环境，脚本需要修改
3.  拉取最新代码，程序执行入口在main.py


#### 执行命令
0.  第一次执行会在目录下生成一个`main.ini`文件，将里面的`api.token`设置为有效的值
1.  将当天的反馈文件放入到csv目录下，命名格式为 **【用户反馈日报】-%20190402.csv**
2.  执行 `python main.py`
3.  执行完成会在`.logs`下面生成此次执行的详细日志
