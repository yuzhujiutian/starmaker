#encoding=utf-8

import os
import sys
import datetime
import hashlib
import ConfigParser

import qa_feedback as qf
import qa_feedback_utils as qfu

# 获取当前脚本目录，作为工作目录
root_dir = os.path.realpath(os.path.realpath(__file__)+"/..")
os.chdir(root_dir)

dry_run = False

# 重定向日志，将print日志输出到控制台和日志文件里面
class logger:

    def __init__(self):
        self.__console__ = sys.stdout
        
        log_dir = os.path.join(root_dir, '.logs')
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)

        self.file_logger = open(os.path.join(log_dir, "./qa-bot-feedback-logs-%s"%datetime.datetime.now().strftime('%Y%m%d%H%M%S')), 'w')

        sys.stdout = self

    def write(self, output_stream):
        self.__console__.write(output_stream)
        self.file_logger.write(output_stream)

    def reset(self):
        sys.stdout = self.__console__

# 获得文件的md5值
def md5(file_path):
    md5file=open(file_path, 'rb')
    value=hashlib.md5(md5file.read()).hexdigest()
    md5file.close()
    
    return value

def check_ini():
    # 检查配置文件是否存在，不存在，写入配置文件，并提示用户
    ini_config_file = os.path.join(root_dir, 'main.ini')
    ini_template_config_file = os.path.join(root_dir, 'template.ini')

    if not os.path.isfile(ini_config_file):
        # os.popen('cp %s %s'%(ini_template_config_file, ini_config_file))
        qfu.copy_file(ini_template_config_file, ini_config_file)

    conf = ConfigParser.ConfigParser()
 
    # 读ini文件
    conf.read(os.path.join(root_dir, ini_config_file))

    error_info = ""
    while 1:
        try:
            api_token = conf.get('qa_bot', 'api.token')
        except Exception as e:
            error_info =  "not found api.token setting in qa_bot section, please check main.ini file..."
            break

        if not api_token.startswith('api-') or (len(api_token) != 32):
            error_info = "please set the right api.token in qa_bot section..."
            break

        qf.api_token = api_token

        break

    if len(error_info) > 0:
        print "error:", error_info
        return False
    else:
        print "check ini succ..."
        return True

# 解析反馈日志
def parse_daily_feedback(csv_file='', force=False):
    print '\n--------- parse_daily_feedback start ---------'
    # 默认从csv目录下面读取当天的csv文件，文件名格式为 【用户反馈日报】-20190402.csv
    # 如果有设置csv文件，将csv文件复制到对应的目录，并重命名
    csv_dir = os.path.join(root_dir, 'csv')
    if not os.path.isdir(csv_dir):
        os.makedirs(csv_dir)

    daily_csv_file_path = os.path.join(csv_dir, "feedback-daily-%s.csv"%(datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y%m%d'))

    if os.path.isfile(csv_file):
        daily_csv_file_path = os.path.join(csv_dir, os.path.basename(csv_file))
        qfu.copy_file(csv_file, daily_csv_file_path)

    print 'process', daily_csv_file_path

    error_info = ''
    while 1:
        if not os.path.isfile(daily_csv_file_path):
            error_info = "not found feedback daily report csv file(%s)"%daily_csv_file_path
            break

        # 检查是否已经处理过
        if (not force) and _check_file_is_already_process(daily_csv_file_path):
            error_info = "daily report file(%s) already been processed..."%daily_csv_file_path
            break

        # 开始处理
        qfu.parse_feedback_csv(daily_csv_file_path)
        break

    # todo: 检查csv文件格式是否正确
    if len(error_info) > 0:
        print "error:", error_info
        return False
    else:

        # 标记文件已经处理
        _mark_csv_file_is_already_process(daily_csv_file_path)
        return True

def _check_file_is_already_process(csv_file):
    if dry_run:
        return

    cmds  = []
    cmds.append('git checkout master')
    cmds.append('git reset --hard')
    cmds.append('git pull')
    for cmd in cmds:
        os.popen(cmd)

    csv_file_md5_file = os.path.join(root_dir, '.csv_file_md5')
    all_csv_file_md5 = []
    if os.path.isfile(csv_file_md5_file):
        all_csv_file_md5 = open(csv_file_md5_file).readline().split()

    daily_csv_file_md5 = md5(csv_file)
    if daily_csv_file_md5 in all_csv_file_md5:
        return True
    else:
        return False

def _mark_csv_file_is_already_process(csv_file):
    if dry_run:
        return

    csv_file_md5_file = open(os.path.join(root_dir, '.csv_file_md5'), 'a')
    daily_csv_file_md5 = md5(csv_file)
    csv_file_md5_file.write(daily_csv_file_md5+"\n")
    csv_file_md5_file.close()

    _update_git(csv_file)

def _update_git(csv_file):
    # 更新git记录
    cmd = []
    cmd.append('git add .csv_file_md5')
    cmd.append('git add "%s"'%csv_file)
    cmd.append('git commit -m "qa_bot process daily feedback: %s"'%os.path.basename(csv_file))
    cmd.append('git push')

    for c in cmd:
        r = os.popen(c)
        print 'exec:', c
        print '  ', r.read()

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')

    r_logger = logger()

    dry_run = not ("--apply" in sys.argv)
    qf.dry_run = dry_run

    csv_file = ""
    for arg in sys.argv:
        if arg.startswith('--file='):
            csv_file = arg.split('=')[1]

    print "process csv file:", csv_file, os.path.isfile(csv_file)

    check_ini()

    parse_daily_feedback(csv_file=csv_file)

    r_logger.reset()
    




