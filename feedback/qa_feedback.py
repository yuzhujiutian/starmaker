#encoding=utf-8
import os
import json
import requests
import base64
from urllib import urlencode

dry_run = False

# 需要qa_bot的api_token
api_token = None

# 需要关联的主task
feedback_root_task_phid = 'PHID-TASK-jzktotfibtw56bdlzc7k'

# 用户反馈需要关联的两个tag
tags_online_bug_phid = 'PHID-PROJ-v4yiztpzvrknygwii352'
tags_qa_bot_feedback_phid = 'PHID-PROJ-45x3od66biwokyyiz7ez'

# QA所有相关成员的tag
qa_group_phid = 'PHID-PROJ-5u34yvaklxeofcddj5j7'

# 执行phabricator命令
def exec_pha_post(api, params):
    if dry_run:
        return {}

    url = 'https://phabricator.ushow.media/api/%s'%api

    params["api.token"] = api_token
    datas = urlencode(params)

    res = None
    try:
        response = requests.post(url, data = datas)
        res = json.loads(response.text)
        print json.dumps(res, sort_keys=True, indent=4, separators=(',', ': '))
    except Exception as e:
        pass

    return res

def create_task(title, description):
    if title == None or len(title) == 0:
        print "create_task: param title type(%s) is error..."%type(title)
        return

    # TODO: 校验title格式，必须是【用户反馈】_{问题分类}_{问题名称}
    # 如果标题格式不对，返回相应错误信息，不创建task

    params = {}

    # 设置task标题
    params["transactions[0][type]"] = "title"
    params["transactions[0][value]"] = title

    # 设置task内容
    params["transactions[1][type]"] = "description"
    params["transactions[1][value]"] = description

    print "\n---start create task---\n"
    print "  title:", title
    print "  description:", description

    # 设置task的父task
    params["transactions[2][type]"] = "parents.set"
    params["transactions[2][value][0]"] = feedback_root_task_phid

    # 设置task的tag, online和qa_bot_feedback
    params["transactions[3][type]"] = "projects.set"
    params["transactions[3][value][0]"] = tags_online_bug_phid
    params["transactions[3][value][1]"] = tags_qa_bot_feedback_phid

    # 设置subscribers
    # params["transactions[4][type]"] = "subscribers.add"
    # params["transactions[4][value][0]"] = qa_group_phid

    # TODO: assign给对应的QA同学

    res = exec_pha_post('maniphest.edit', params)
    if not (type(res) == type({})):
        # 执行命令出错
        print "create_task: failed,", str(res)
    else:
        error_code = res.get('error_code', None)
        error_info = res.get('error_info', None)

        if not (error_code == None):
            # create_task失败
            print "  create_task: failed,", str(error_info)
            return

        # 创建成功
        task_id = None
        try:
            task_id = res['result']['object']['id']
        except Exception as e:
            pass

        if not (task_id == None):
            print "  create_task: succ, task url is https://phabricator.ushow.media/T%s"%task_id
        else:
            print "  create_task: failed, the format of the response is invalid.. please check it..."

        return task_id

# 评论某个task
def comment_task(task_id, comment):
    params = {}

    params["objectIdentifier"] = task_id

    # 设置task标题
    params["transactions[0][type]"] = "comment"
    params["transactions[0][value]"] = comment

    print "\n---start comment task(T%s)---\n"%task_id
    print "comment:"
    print comment

    res = exec_pha_post('maniphest.edit', params)
    if not (type(res) == type({})):
        # 执行命令出错
        print "comment_task: failed,", str(res)
    else:
        error_code = res.get('error_code', None)
        error_info = res.get('error_info', None)

        if not (error_code == None):
            # create_task失败
            print "  comment_task: failed,", str(error_info)
            return

        # 创建成功
        task_id = None
        try:
            task_id = res['result']['object']['id']
        except Exception as e:
            pass

        if not (task_id == None):
            print "  comment_task: succ, task url is https://phabricator.ushow.media/T%s"%task_id
        else:
            print "  comment_task: failed, the format of the response is invalid.. please check it..."

        return task_id

# 输入一系列title, 根据title搜索是否存在对应的task是否已经创建
def search_feedback_task(titles):
    params = {}

    # 设置task标题
    params["queryKey"] = "e3A4QhTyPOOA"

    res = exec_pha_post('maniphest.search', params)

    """
    The limit and order fields are describing the effective limit and order the query was executed with, and are usually not of much interest. The after and before fields give you cursors which you can pass when making another API call in order to get the next (or previous) page of results.
    To get the next page of results, repeat your API call with all the same parameters as the original call, but pass the after cursor you received from the first call in the after parameter when making the second call.
    """
    result = {}
    try:
        datas = res['result']['data']
        for d in datas:
            title = d['fields']['name']
            phid = d['id']

            if title in titles:
                result[title] = phid

    except Exception as e:
        pass

    return result

def upload_file(file_path, file_name):
    print '\n--- upload_file start ---\n'
    if not os.path.isfile(file_path):
        print 'file %s is not exsit...'%file_path
        return

    if file_name == None:
        file_name = os.path.basename(file_path)

    params = {}

    params['data_base64'] = base64.b64encode(open(file_path).read())
    params['name'] = file_name

    res = exec_pha_post('file.upload', params)

    file_phid = None
    if not (type(res) == type({})):
        # 执行命令出错
        print "upload_file: failed,", str(res)
    else:
        error_code = res.get('error_code', None)
        error_info = res.get('error_info', None)

        if not (error_code == None):
            # create_task失败
            print "  upload_file: failed,", str(error_info)
            return

        # 创建成功
        file_phid = res.get('result', None)

        if file_phid == None:
            print "  upload_file: failed..."

    if not (file_phid == None):
        params = {}
        params['phid'] = file_phid

        res = exec_pha_post('file.info', params)

        try:
            file_phid = res.get('result', {}).get('objectName', None)
        except Exception as e:
            print '  get upload file info error:', str(res)
        
    print 'upload_file: succ, file id is %s'%file_phid
    return file_phid



# upload_file('./unittest/3.csv', 'test.3.csv')


# create_task("test title", "test desc\ndfasdfasdf\n")
# search_feedback_task(['test title 1'])
# description = "| index | 问题描述 | UID | 版本 | 系统 | 日期 | 图片链接1 | 图片链接2 | 图片链接3 |\n\
# | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n\
# | 1 | Sir plzzzzz My song ranking | 5.34802E+15 | 7.3.2 | Android 8.1.0 | 3月29日 | https://improxy.starmakerstudios.com/tools/im/0/production/promotion/other/5182ae1c5c6ce63ca06ec1a13ae38682.jpg |  |  |"
# comment_task('40744', description)

# get_task_info("12061")
