
import requests
import os
import time
import io

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://www.bilibili.com',
    'Connection': 'keep-alive'
}

# 时间戳转时间
def timestampToTime(timestamp):
    timeArray = time.localtime(timestamp)
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return timeStr

# 获取数据
def get_data(bvid):
    resp = requests.get(f'https://api.bilibili.com/x/web-interface/view?bvid={bvid}', headers=headers).json()
    # print(resp['data']['stat'])
    return resp['data']
# 读取文件，导入所有bvids
def read_file():
    with open(r'bilibili_all.txt', 'r') as f:
        content = f.read()

    bvids = content.split(',')
    print(bvids)
    data = []
    for bvid in bvids:
        data.append(get_data(bvid))
        time.sleep(1)

    return data


# 将当前时间点的播放量写入到文件
def writelog(data, filename):
    try:

        with open(filename, 'a', encoding='utf-8') as file:
            print("开始写入数据")
            print(f"{timestampToTime(int(time.time()))}\n")
            file.write(f"{timestampToTime(int(time.time()))}\n")
            file.write("bvid\ttitle\tview\n")
            for vdata in data:
                file.write(f"{vdata['bvid']}\t{vdata['title']}\t{vdata['stat']['view']}\n")

            print("数据写入结束")

    except Exception as e:
        print(f"Error writing log file: {e}")


    












