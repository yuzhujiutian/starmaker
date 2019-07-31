#### 环境准备
1.  安装git环境，保证自己的账号有qa repo的权限，repo地址`ssh://git@phabricator.ushow.media/source/starmaker-qa.git`. 保证自己的账号的pull和push的权限，并且配置正确
2.  安装python 2.7版本，如果是python 3.0版本以上环境，脚本需要修改
3.  拉取最新代码，程序执行入口在`feedback/main.py`


#### 执行命令
0.  第一次执行会在目录下生成一个`main.ini`文件，将里面的`api.token`设置为有效的值
1.  将昨天的反馈文件放入到csv目录下，如果当天是20190403, 则反馈日报文件的命名为 **feedback-daily-20190402.csv**
2.  执行 `python main.py`, 会假装执行一次，可以先看看执行完成的日志，确认无误后，执行 `python main.py --apply`, 此次会真正执行
3.  执行完成会在`.logs`下面生成此次执行的详细日志
4.  可以指定解析某个文件, `python main.py --file={file_path} --apply`, 如果没有 `--apply`参数，则是假装执行一次，可以预览此次执行的结果

#### 目前可能得问题
1.  python安装的版本错误，会导致脚本无法运行
2.  没有安装git, 可能会导致重复提交相同的csv文件时，无法去重
3.  csv文件的格式错误，可能会导致脚本崩溃
4.  csv文件的中文可能对于脚本有影响

