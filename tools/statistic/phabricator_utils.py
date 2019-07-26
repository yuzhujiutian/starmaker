#encoding=utf-8
import base64
import json
import collections
from urllib import urlencode

import requests

dry_run = False

# 需要qa_bot的api_token
api_token = 'api-anbgqrl6np4h36au2ppp3jqgewyp'

# 执行phabricator命令
def exec_pha_post(api, params, force=False):
    if dry_run and (not force):
        return {}

    url = 'https://phabricator.ushow.media/api/%s'%api

    params["api.token"] = api_token
    datas = urlencode(params)

    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }

    res = None
    try:
        response = requests.request('POST', url, data = datas, headers=headers)

        res = json.loads(response.text)
        # print json.dumps(res, sort_keys=True, indent=4, separators=(',', ': '))
    except Exception as e:
        print e

    return res

# 查找所有符合条件的bug
# 
def bug_report_query_request(statuses=['open'], after=None, tags=[], limit=100, authors=[], created_before=None, created_after=None, closed_before=None, closed_after=None):
    params = collections.OrderedDict()

    # 查询符合某些状态的bug
    index = 0
    for status in statuses:
        params["constraints[statuses][%d]"%index] = status
        index += 1

    # 设置创建者
    index = 0
    for author in authors:
        params["constraints[authorPHIDs][%d]"%index] = author
        index += 1

    # 包含某些tag的bug
    # Bug Report的project id, PHID-PROJ-4l6jxvbrgltoegpydrzi
    if "PHID-PROJ-4l6jxvbrgltoegpydrzi" not in tags:
        tags.append("PHID-PROJ-4l6jxvbrgltoegpydrzi")

    index = 0
    for tag in tags:
        params["constraints[projects][%d]"%index] = tag
        index += 1

    # 设置bug创建时间，需要是在该时间之前创建
    if created_before is not None:
        params["constraints[createdEnd]"] = created_before

    # 设置bug创建时间，需要是在该时间之后创建
    if created_after is not None:
        params["constraints[createdStart]"] = created_after

    # 设置bug关闭时间，在closed_after时间之后关闭的bug
    if closed_after is not None:
        params["constraints[closedStart]"] = closed_after

    # 设置bug关闭时间，在closed_before时间之前关闭的bug
    if closed_before is not None:
        params["constraints[closedEnd]"] = closed_before

    # 最多一次获取100个
    params["limit"] = limit

    # 按倒序排列
    params["order"] = "newest"

    # cursor
    if after is not None:
        params["after"] = after

    print params

    res = exec_pha_post('maniphest.search', params, force=True)

    error_code = res.get('error_code', '')
    error_info = res.get('error_info', '')

    result = res.get('result', {})
    result_data = []
    if result is not None:
        result_data = result.get('data', [])

    cursor_after = None
    cursor_before = None
    cursor_limit = 100

    if result is not None:
        result_cursor = result.get('cursor', {})
        if result_cursor is not None:
            cursor_before = result_cursor.get('before', None)
            cursor_after = result_cursor.get('after', None)
            cursor_limit = result_cursor.get('limit', None)

    return result_data, cursor_before, cursor_after, cursor_limit


