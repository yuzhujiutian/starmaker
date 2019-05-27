# coding=utf-8
import datetime
import gzip
import io
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler

from analysis_dot.analysis_report_dot.check_clear_log import TestLog_Processing

# 获取当前脚本目录，作为工作目录
root_dir = os.path.realpath(os.path.realpath(__file__)+"/..")
os.chdir(root_dir)

_filter_params = {}
# _filter_params['type'] = ['load', 'show', 'visit', 'performance', 'page_open', 'request', 'page_close']
# _filter_params['page'] = ['party_room', 'live_room', 'Popular', 'Following', 'library', 'push', 'splash',
#                           'app_launch', 'main']
# _filter_params['obj'] = ['page_open', 'watch_live', 'enter_live_room', 'activity', 'splash', 'song_show', 'unread',
#                          'banner', 'fragment', 'card']

# _filter_params['output'] = ['enter_mode', 'room_mode', 'socket_connect_cost_time', 'socket_streaminfo_cost_time',
# 'socket_joinroom_cost_time', 'ui_total_cost_time', 'ui_sub_room_cost_time', 'media_play_cost_time']

# 直播打点
# _filter_params['type'] = ['show', 'visit']
# _filter_params['page'] = ['live_room']
# _filter_params['obj'] = ['watch_live', 'enter_live_room']
# _filter_params['output'] = ['room_enter_time','load_library_time','ui_cost_time','delegate_cost_time',
# 'create_viewer_time','all_cost_time','cost_time','stream_type']


# 重定向日志，将print日志输出到控制台和日志文件里面
class logger:
    def __init__(self):
        self.__console__ = sys.stdout

        log_dir = os.path.join(root_dir, '.logs')
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)

        self.file_logger = open(
            os.path.join(log_dir, "./events-logs-%s.log" % datetime.datetime.now().strftime('%Y%m%d')), 'a+')
        self.detail_file_logger = open(
            os.path.join(log_dir, "./events-logs-details-%s.log" % datetime.datetime.now().strftime('%Y%m%d')), 'a+')

        sys.stdout = self

    def write(self, output_stream):
        self.__console__.write(output_stream)
        self.file_logger.write(output_stream)
        self.file_logger.flush()

    def detail(self, output_stream):
        self.detail_file_logger.write(output_stream)
        self.detail_file_logger.flush()

    def reset(self):
        sys.stdout = self.__console__


r_logger = logger()


# 打印事件
def print_e(e):
    print('\n''------------')
    # python2写法
    # keys = e.keys()
    # keys.sort()
    keys = sorted(e)

    _output_params = ['type', 'page', 'obj', 'timestamp']

    for i in _output_params:
        print(('%30s: %s' % (i, e.get(i, ""))))

    for k in keys:
        if k.startswith('t_params_'):
            print(('%30s: %s' % (k[len('t_params_'):], e.get(k, ""))))

    print('------------''\n')


# 过滤是否需要处理打点事件(如需过滤将此处注释打开)
def j_fileter(event):
    # keys = _filter_params.keys()

    result = True
    # for key in keys:
    #     if key == 'output':
    #         continue
    #
    #     _value = event.get(key, '')
    #
    #     if not (_value in _filter_params[key]):
    #         result = False
    #         break

    return result


def android_handle_event(datas, filter=None):
    # Android需要这么处理
    content = datas.decode('utf-8').encode('ISO-8859-1')
    data = gzip.GzipFile('', 'rb', 9, io.BytesIO(content))
    content = json.loads(data.read())
    _events = content['events']

    base_params = {}
    for k in content.keys():
        if k in ['events']:
            continue
        else:
            base_params[k] = content.get(k, "")

    for _e in _events:
        _params = _e.pop('params')
        e_params = {}
        for k in _params.keys():
            e_params['t_params_' + k] = _params.get(k, "")
        # 最终的event
        # python2的写法
        # e = dict{_e.items() + base_params.items() + e_params.items()
        e = {}
        e.update(_e.items())
        e.update(base_params.items())
        e.update(e_params.items())
        if filter is None:
            print_e(e)
        else:
            if filter(e):
                print_e(e)
        r_logger.detail(json.dumps(e, indent=2))


def ios_handle_event(datas, filter=None):
    # IOS需要这么处理
    buff = io.BytesIO(datas)
    data = gzip.GzipFile(fileobj=buff)
    aa = data.read().decode('utf-8').encode()
    content = json.loads(aa)
    _events = content['events']

    base_params = {}
    for k in content.keys():
        if k in ['events']:
            continue
        else:
            base_params[k] = content.get(k, "")

    for _e in _events:
        _params = _e.pop('params')
        e_params = {}
        for k in _params.keys():
            e_params['t_params_' + k] = _params.get(k, "")
        # 最终的event
        # e = dict(_e.items() + base_params.items() + e_params.items())
        e = {}
        e.update(_e.items())
        e.update(base_params.items())
        e.update(e_params.items())
        if filter is None:
            print_e(e)
        else:
            if filter(e):
                print_e(e)
        r_logger.detail(json.dumps(e, indent=2))


class PostHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # path = self.path
        # print 'path:', path
        # if len(path) > 1:
        query = urllib.parse.splitquery(self.path)
        # print 'query:', query
        action = query[0][1:]
        # print 'action:', action

        if action == 'config':
            # 接收get参数
            print(query[1])
            if query[1] is not None:
                for qp in query[1].split('&'):
                    kv = qp.split('=')
                    _filter_params[kv[0]] = urllib.parse.unquote(kv[1]).decode("utf-8", 'ignore').split(',')

        self.send_response(200)
        self.end_headers()

        self.wfile.write(json.dumps(_filter_params, indent=4))
        return

    def do_POST(self):
        # path = self.path
        # 获取post提交的数据
        # print self.headers
        str_headers = self.headers.__str__()
        user_agent = re.findall("User-Agent: " + "(.*)", str_headers)[0]
        platform1 = re.findall("Android", user_agent)
        platform2 = re.findall("iOS", user_agent)
        datas = self.rfile.read(int(self.headers['content-length']))
        if platform1:
            try:
                android_handle_event(datas, j_fileter)
            except Exception as e:
                print(e)
        elif platform2:
            try:
                ios_handle_event(datas, j_fileter)
            except Exception as e:
                print(e)
        else:
            self.send_response(404)
            self.end_headers()

        self.send_response(201)
        self.end_headers()


def StartServer():
    # 开始前清理log日志
    try:
        TestLog_Processing()
    except:
        pass
    from http.server import HTTPServer
    sever = HTTPServer(("", 8982), PostHandler)
    # import ssl
    # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    # context.load_cert_chain(certfile="./cert.pem", keyfile="./key.pem")
    # sever.socket = context.wrap_socket (sever.socket, server_side=True)
    sever.serve_forever()


if __name__ == '__main__':
    StartServer()
