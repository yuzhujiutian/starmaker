#encoding=utf-8

import phabricator_utils as pu
from bug_report import *

# 计算指定版本bug解决的速度
def bug_report_by_version(platform, version_tag):
    # 获取version phid
    phid = pu.project_search(version_tag)

    if phid == None:
        print 'Not found', version_tag
        return

    if platform == TAG_Android:
        version_tag = version_tag.split()[-1]
    else:
        version_tag = version_tag.split()[-1][1:]

    # 统计每个task的完成情况
    all_open_bugs = bug_report_query([platform, phid], statuses=['open'])
    all_open_bugs_cnt = len(all_open_bugs)

    # any closed status bug
    all_closed_bugs = bug_report_query([platform, phid], statuses=['closed()'])
    all_closed_bugs_cnt = len(all_closed_bugs)

    # 计算closed status bug被修复的时间
    
    phids = []
    for bug in all_closed_bugs:
        phids.append(bug['phid'])

    tasks_detail = collections.OrderedDict()
    start_index = 0
    while start_index + 100 < len(phids[start_index:]):
        tasks_detail.update(pu.task_search_by_phids(phids[start_index:start_index+100]))
        start_index += 100

    tasks_detail.update(pu.task_search_by_phids(phids[start_index:]))

    task_tags = []
    for task_id in tasks_detail.keys():
        tags_phid = tasks_detail[task_id]['projectPHIDs']
        task_tags.extend(tags_phid)

    # 获取所有tag的name
    tags_name = pu.project_search_by_phids(task_tags)

    version_groupby = {}

    for task_id in tasks_detail.keys():
        tags_phid = tasks_detail[task_id]['projectPHIDs']

        start_version = None
        end_version = None
        version_tags = []
        # version的tag, 查找该task的start version和end version
        for tag_phid in tags_phid:
            tag_name = tags_name[tag_phid]
            if '/ The Voice Android' in tag_name and platform == TAG_Android:
                version_tags.append(tag_name.split()[-1])

            if platform == TAG_iOS and ('StarMaker iOS v' in tag_name):
                version_tags.append(tag_name.split()[-1][1:])

            # print task_id, tag_name

        version_tags.sort()

        # print version_tags, task_id

        if len(version_tags) == 1:
            start_version = version_tags[0]
            end_version = version_tags[0]
        elif len(version_tags) == 2:
            start_version = version_tags[0]
            end_version = version_tags[1]
        else:
            start_version = version_tags[0]
            end_version = version_tags[-1]

        # print task_id, start_version, end_version

        if start_version < version_tag:
            # 不是version版本发现的bug, 不统计
            all_closed_bugs_cnt -= 1
            continue

        version_groupby[end_version] = version_groupby.get(end_version, 0) + 1

    print 'version:', version_tag
    print 'all bugs:', (all_open_bugs_cnt + all_closed_bugs_cnt)
    print 'all open bugs', all_open_bugs_cnt
    print 'all close bugs', all_closed_bugs_cnt

    versions = version_groupby.keys()
    versions.sort()
    for version in versions:
        print version, version_groupby[version], '%.2f%%'%(version_groupby[version] * 100. / (all_open_bugs_cnt + all_closed_bugs_cnt))

    print

# for v in ['7.4.3', '7.4.4', '7.4.5', '7.4.6', '7.4.8', '7.4.9', '7.5.0']:
#     bug_report_by_version(TAG_Android, 'StarMaker / The Voice Android %s'%v)


# for v in ['7.5.0', '7.5.1', '7.5.3', '7.5.4', '7.5.5']:
#     bug_report_by_version(TAG_iOS, 'StarMaker iOS v%s'%v)


bug_report_by_version(TAG_iOS, 'StarMaker iOS v7.5.5')










