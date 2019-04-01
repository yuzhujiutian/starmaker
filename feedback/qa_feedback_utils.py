#encoding=utf-8
import qa_feedback as qf

import os
import csv
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

def parse_feedback_csv(csv_file_path):
    f = open(csv_file_path, 'rb')
    feedbacks = csv.DictReader(f)

    feedback_category = None
    feedback_name = None
    feedback_desc = None

    feedbacks_info = {}

    for feedback in feedbacks:
        # python对于中文的支持问题，暂时这么处理
        for key in feedback.keys():
            ukey = unicode(key, 'utf-8')
            value = unicode(feedback[key], 'utf-8')
            if ukey == "问题分类":
                feedback_category = value
            elif ukey == "问题名称":
                feedback_name = value

        title = '【用户反馈】_%s_%s'%(feedback_category, feedback_name)
        fs = feedbacks_info.get(title, [])
        fs.append(feedback)
        feedbacks_info[title] = fs

    titles = feedbacks_info.keys()

    # 查询反馈是否已经被处理了
    feedbacks_status = qf.search_feedback_task(titles)
    print feedbacks_status

    for title in titles:
        task_id = feedbacks_status.get(title, None)

        description = generate_description(feedbacks_info.get(title))

        if task_id == None:
            # 创建新task
            # print 'create task', title
            # print 'description:\n', description
            qf.create_task(title, description)
        else:
            # 更新task
            qf.comment_task(task_id, description)

    # 更新主task

def generate_description(feedbacks):
    index = 1

    result = ""

    if feedbacks == None or len(feedbacks) == 0:
        return result

    # 添加总共统计
    result += "%s\n"%time.ctime()
    result += "当天共计反馈%d次\n\n"%len(feedbacks)

    columns = ["index", "问题描述", "UID", "版本", "系统", "日期", "图片链接1", "图片链接2", "图片链接3"]

    result += "| " + " | ".join(columns) + " |\n"
    result += "| --- " * len(columns) + "|\n"

    line_format = ""
    for feedback in feedbacks:
        feedback_desc = ''
        feedback_uid = ''
        feedback_version = ''
        feedback_platform = ''
        feedback_date = ''
        feedback_pic1 = ''
        feedback_pic2 = ''
        feedback_pic3 = ''

        for key in feedback.keys():
            ukey = str(unicode(key, 'utf-8'))
            value = str(unicode(feedback[key], 'utf-8'))

            if ukey == "问题描述":
                feedback_desc = value
            elif ukey == "UID":
                feedback_uid = value
            elif ukey == "版本":
                feedback_version = value
            elif ukey == "系统":
                feedback_platform = value
            elif ukey == "日期":
                feedback_date = value
            elif ukey == "图片链接1":
                feedback_pic1 = value
            elif ukey == "图片链接2":
                feedback_pic2 = value
            elif ukey == "图片链接3":
                feedback_pic3 = value

        result += "| %s | %s | %s | %s | %s | %s | %s | %s | %s |\n"%(index, feedback_desc, feedback_uid, feedback_version, feedback_platform, feedback_date, feedback_pic1, feedback_pic2, feedback_pic3)

    return result


# parse_feedback_csv("./3.csv")







