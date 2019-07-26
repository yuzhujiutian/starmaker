#encoding=utf-8
import os
import time
import datetime

import pandas as pd
import warnings
warnings.filterwarnings("ignore")

import phabricator_utils as pu

# 获取当前所有的bug详情
def bug_report_query(tag, statuses=['open'], authors=[], created_before=None, created_after=None, closed_before=None, closed_after=None):
    result_data_len = 100
    cursor_after = ''

    bug_ids = []
    bugs = []

    after = None

    # 防止无限循环
    cnt = 0
    threshold = 300

    tags = []
    if tag is not None:
        tags = [tag]

    while (result_data_len == 100) and (cursor_after is not None):
        result_data, cursor_before, cursor_after, cursor_limit = pu.bug_report_query_request(tags=tags, statuses=statuses, authors=authors, limit=100, after=after, created_before=created_before, created_after=created_after, closed_before=closed_before, closed_after=closed_after)

        # for data in result_data:
        #     bug_id = data['id']
        #     bug_ids.append(bug_id)
        bugs.extend(result_data)

        result_data_len = len(result_data)

        after = cursor_after

        cnt += 1

        if cnt > threshold:
            break

    # print len(bug_ids), len(set(bug_ids)), len(bugs)
    # print bug_ids
    return bugs

TAG_Android = "PHID-PROJ-iuyamxepp7kzthfbfzda"

TAG_iOS = "PHID-PROJ-6uye5ugnkf4dhtgaxnt6"

# 获取截止到end_time时，处于open的bug状态
def bug_report_history(platform, end_time=None):
    timestamp = int(time.time())

    if end_time is not None:
        timestamp = int(time.mktime(time.strptime(end_time,"%Y-%m-%d")))

    # 获取end_time之前创建的bug_report, 此时处于open状态的bug列表
    already_open_bugs = bug_report_query(platform, created_before=timestamp)

    # 获取end_time之前创建的bug, 但是在end_time之后处于非open状态的列表
    already_closed_bugs = bug_report_query(platform, statuses=[], created_before=timestamp, closed_after=timestamp)

    # 截止到end_time时，处于open状态的bug总数
    total_open_bugs = len(already_open_bugs) + len(already_closed_bugs)

    already_open_bugs.extend(already_closed_bugs)

    return already_open_bugs

# start_time到end_time这段时间新创建的bug
def new_bug_report(platform, start_time, end_time):
    new_bugs = bug_report_query(platform, created_after=start_time, created_before=end_time)
    return new_bugs

def android_bug_report_history(end_time=None):
    return bug_report_history(TAG_Android, end_time=end_time)

def ios_bug_report_history(end_time=None):
    return bug_report_history(TAG_iOS, end_time=end_time)

# 在 start_time 到 end_time这段时间新创建的bug
def new_bug_query(platform, start_time, end_time):
    start_time = int(time.mktime(time.strptime(start_time,"%Y-%m-%d")))
    end_time = int(time.mktime(time.strptime(end_time,"%Y-%m-%d")))
    new_bugs = bug_report_query(platform, statuses=[], created_after=start_time, created_before=end_time)

    return new_bugs

def android_new_bug_query(start_time, end_time):
    return new_bug_query(TAG_Android, start_time, end_time)

def ios_new_bug_query(start_time, end_time):
    return new_bug_query(TAG_iOS, start_time, end_time)

# 在 start_time 到 end_time这段时间close的bug
def closed_bug_query(platform, start_time, end_time):
    start_time = int(time.mktime(time.strptime(start_time,"%Y-%m-%d")))
    end_time = int(time.mktime(time.strptime(end_time,"%Y-%m-%d")))
    closed_bugs = bug_report_query(platform, statuses=[], closed_after=start_time, closed_before=end_time)

    return closed_bugs

def android_closed_bug_query(start_time, end_time):
    return closed_bug_query(TAG_Android, start_time, end_time)

def ios_closed_bug_query(start_time, end_time):
    return closed_bug_query(TAG_iOS, start_time, end_time)

# 统计最近weeks周的bug报告
def statistic_bug_report_history(query_method, new_bug_query_method, closed_bug_query_method, data_source, weeks=1):
    days = 0
    fridays = []
    while 1:
        dt = datetime.datetime.fromtimestamp(time.time() - days * 60 * 60 * 24)
        # 周六的00:00:00
        if dt.weekday() == 5:
            fridays.append(dt)
        days += 1

        if len(fridays) >= weeks:
            break

    _pdf = pd.read_csv(data_source)

    for friday in fridays:
        end_time = friday.strftime("%Y-%m-%d")
        start_time = (friday - datetime.timedelta(days=7)).strftime("%Y-%m-%d")

        if len(_pdf[_pdf['start time'] == start_time][_pdf['end time'] == end_time]) > 0:
            # 已经计算过了，不再计算
            continue

        all_open_bugs = query_method(end_time=end_time)

        # all open bug数量
        all_open_bugs_cnt = len(all_open_bugs)

        # 计算open bug category
        all_open_bugs_by_category = {}
        for bug in all_open_bugs:
            priority = bug["fields"]["priority"]["name"].lower()
            v = all_open_bugs_by_category.get(priority, [])
            v.append(bug)
            all_open_bugs_by_category[priority] = v

        # all open high bug数量
        all_open_high_bugs_cnt = len(all_open_bugs_by_category.get('high', []))

        # all open normal bug数量
        all_open_normal_bugs_cnt = len(all_open_bugs_by_category.get('normal', []))

        # all low normal bug数量
        all_open_low_bugs_cnt = len(all_open_bugs_by_category.get('low', []))

        # other bug数量
        all_open_other_bugs_cnt = 0

        for category in all_open_bugs_by_category.keys():
            if category not in ['high', 'normal', 'low']:
                all_open_other_bugs_cnt += len(all_open_bugs_by_category[category])

        # 当周新增bug
        new_bugs = new_bug_query_method(start_time=start_time, end_time=end_time)
        new_bugs_cnt = len(new_bugs)

        # 当周解决bug
        closed_bugs = closed_bug_query_method(start_time=start_time, end_time=end_time)
        closed_bugs_cnt = len(closed_bugs)

        row_value = [start_time, end_time, all_open_bugs_cnt, all_open_high_bugs_cnt, all_open_normal_bugs_cnt, all_open_low_bugs_cnt, all_open_other_bugs_cnt, new_bugs_cnt, closed_bugs_cnt]
        print row_value
        insert_row = pd.DataFrame([row_value], columns = ['start time','end time','all open bug','open high bug','open normal bug','open low bug','the other open bug','new bug','closed bug'])
        _pdf = _pdf.append(insert_row, ignore_index=True)

    # 按升序排列
    _pdf = _pdf.sort_values(by = ["start time"], ascending = [True])
    # 不保留序号
    _pdf.to_csv(data_source, index=0)

# 统计Android 最近20周的bug变化数量
statistic_bug_report_history(android_bug_report_history, android_new_bug_query, android_closed_bug_query, 'bug_report_android.csv', weeks=20)

# 统计iOS 最近20周的bug变化数量
statistic_bug_report_history(ios_bug_report_history, ios_new_bug_query, ios_closed_bug_query, 'bug_report_ios.csv', weeks=20)   


# 统计start_time, end_time时间段，QA创建bug的数量

# qa成员对应的phid
qa_phid_mapping = {
    'PHID-USER-5ucpy3dmgdqwt4mg35rq':'wei.wang',
    'PHID-USER-awnsxd46n3grftcyv6tm':'jin.jiang',
    'PHID-USER-zmc6oer33nkdjowmr4b5':'jie.li',
    'PHID-USER-gmo6hwkrypj36vpjjlpg':'jia.liu',
    'PHID-USER-mq5vhysit57lesbbbghb':'yaoliang.cui',
    'PHID-USER-yqm7glxqn7ms2yw6rnzp':'yangyang.yu',
    'PHID-USER-cuemnzevn2odyp7nxxy7':'zhangdong',
    'PHID-USER-iirsw6b7dhjrcr6zbty5':'liuyue',
}

def bug_report_by_qa_member_query(start_time, end_time):
    start_time = int(time.mktime(time.strptime(start_time,"%Y-%m-%d")))
    end_time = int(time.mktime(time.strptime(end_time,"%Y-%m-%d")))
    bugs = bug_report_query(None, statuses=[], created_after=start_time, created_before=end_time, authors=["members(PHID-PROJ-5u34yvaklxeofcddj5j7)"])

    print 'total bugs:', len(bugs)
    bugs_by_qa_member = {}
    for bug in bugs:
        author_phid = bug['fields']['authorPHID']
        v = bugs_by_qa_member.get(author_phid, [])
        v.append(bug)
        bugs_by_qa_member[author_phid] = v

    for author_phid in bugs_by_qa_member.keys():
        print qa_phid_mapping.get(author_phid, author_phid), len(bugs_by_qa_member[author_phid])

    return bugs_by_qa_member

# 最近六个月，四个月，两个月，一个月和最近一周，每个QA同学发现的bug数量统计
def bug_report_by_qa_member(detail=False):
    end_time = datetime.datetime.fromtimestamp(time.time() - 0 * 60 * 60 * 24).strftime("%Y-%m-%d")
    week_before_time = datetime.datetime.fromtimestamp(time.time() - 7 * 60 * 60 * 24).strftime("%Y-%m-%d")
    month_before_time = datetime.datetime.fromtimestamp(time.time() - 30 * 60 * 60 * 24).strftime("%Y-%m-%d")
    month2_before_time = datetime.datetime.fromtimestamp(time.time() - 60 * 60 * 60 * 24).strftime("%Y-%m-%d")
    month4_before_time = datetime.datetime.fromtimestamp(time.time() - 120 * 60 * 60 * 24).strftime("%Y-%m-%d")
    month6_before_time = datetime.datetime.fromtimestamp(time.time() - 180 * 60 * 60 * 24).strftime("%Y-%m-%d")

    week_report = bug_report_by_qa_member_query(week_before_time, end_time)
    
    month_report = bug_report_by_qa_member_query(month_before_time, end_time)

    month2_report = bug_report_by_qa_member_query(month2_before_time, end_time)

    if detail:
        month4_report = bug_report_by_qa_member_query(month4_before_time, end_time)

        month6_report = bug_report_by_qa_member_query(month6_before_time, end_time)

    result = []

    columns = ['name', 'week', 'month', '2 month']
    if detail:
        columns.extend(['4 month', '6 month'])
    result.append(columns)

    for qa_phid in qa_phid_mapping.keys():
        week_cnt = len(week_report.get(qa_phid, []))
        month_cnt = len(month_report.get(qa_phid, []))
        month2_cnt = len(month2_report.get(qa_phid, []))
        v = [qa_phid_mapping[qa_phid], week_cnt, month_cnt, month2_cnt]

        if detail:
            month4_cnt = len(month4_report.get(qa_phid, []))
            month6_cnt = len(month6_report.get(qa_phid, []))
            v.extend([month4_cnt, month6_cnt])

        result.append(map(str, v))

    f = open('bug_report_by_qa.csv', 'w')
    for r in result:
        f.write(','.join(r)+'\n')
    f.close()


bug_report_by_qa_member(detail=True)

def user_search(user_id):
    params = {}
    params['constraints[nameLike]'] = user_id


    # params = 'params[queryKey]=&params[constraints]={"nameLike":"lin.jiang"}&params[attachments]=&params[order]=&params[before]=&params[after]=&params[limit]=&output=human'

    # print urlencode(params)
    # exit()

    res = pu.exec_pha_post('user.search', params)
    phid = ''
    try:
        phid = res['result']['data'][0]['phid']
    except Exception as e:
        pass

    return phid


def qa_teams_phid():
    qa_teams = ['wei.wang', 'jin.jiang', 'jie.li', 'jia.liu', 'yaoliang.cui', 'yangyang.yu', 'zhangdong', 'liuyue']
    result = []
    for i in qa_teams:
        phid = user_search(i)
        result.append("'%s'='%s',"%(phid, i))

    print '\n'.join(result)

# qa_teams_phid()

