from utils import query
import json
import pandas as pd
import numpy as np

_cached_data = None

_cached_data1 = None


# 缓存全量数据，避免多次查询
def getAllData():
    global _cached_data
    if _cached_data is None:
        _cached_data = query.querys('select * from movies', [], 'select')

        def map_fn(item):
            item = list(item)
            item[1] = item[1].split(',') if item[1] else ['无']
            item[4] = item[4].split(',') if item[4] else ['无']
            item[7] = item[7].split(',')  # 默认是一个字符串列表
            item[8] = item[8].split(',') if item[8] else ['中国大陆']
            item[9] = item[9].split(',') if item[9] else ['汉语普通话']
            item[13] = item[13].split(',')
            item[16] = item[16].split(',')
            item[15] = json.loads(item[15])
            return item

        _cached_data = list(map(map_fn, _cached_data))

    return _cached_data
# 缓存全量数据，避免多次查询
def getAllData1():
    global _cached_data1
    if _cached_data1 is None:
        _cached_data1 = query.querys('select * from movies', [], 'select')

        def map_fn(item):
            item = list(item)
            item[1] = item[1] if item[1] else ['无']
            item[4] = item[4] if item[4] else ['无']
            item[7] = item[7]  # 默认是一个字符串列表
            item[8] = item[8] if item[8] else ['中国大陆']
            item[9] = item[9] if item[9] else ['汉语普通话']
            item[13] = item[13].split(',')
            item[16] = item[16].split(',')
            item[15] = json.loads(item[15])
            return item

        _cached_data1 = list(map(map_fn, _cached_data1))

    return _cached_data1

def getDataFrame():
    all_data = getAllData()
    return pd.DataFrame(all_data, columns=[
        'id', 'directors', 'rate', 'title', 'casts', 'cover', 'year', 'types',
        'country', 'lang', 'time', 'movieTime', 'comment_len', 'starts',
        'summary', 'comments', 'imgList', 'movieUrl', 'detailLink'
    ])


# 获取最大评分
def getMaxRate():
    df = getDataFrame()
    return df['rate'].astype(float).max()


# 获取最大出演次数的演员
def getMaxCast():
    casts = {}
    for i in getAllData():
        for j in i[4]:
            casts[j] = casts.get(j, 0) + 1
    maxName = max(casts, key=casts.get)
    return maxName


# 获取出现频率最高的语言
def getMaxLang():
    langs = {}
    for i in getAllData():
        for j in i[9]:
            langs[j] = langs.get(j, 0) + 1
    maxLang = max(langs, key=langs.get)
    return maxLang


# 获取所有类型的统计
def getTypesAll():
    types = {}
    for i in getAllData():
        for j in i[7]:
            types[j] = types.get(j, 0) + 1
    return types.keys()


# 获取类型及其统计数据
def getType_t():
    types = {}
    for i in getAllData():
        for j in i[7]:
            types[j] = types.get(j, 0) + 1
    return [{'name': k, 'value': v} for k, v in types.items()]


# 获取评分统计
def getRate_t():
    rates = {}
    for i in getAllData():
        rates[i[2]] = rates.get(i[2], 0) + 1
    return list(rates.keys()), list(rates.values())


# 获取表格数据（已经处理过的数据）
def getTableList():
    def map_fn(item):
        # item[1] = '/'.join(item[1])
        # item[4] = '/'.join(item[4])
        # item[7] = '/'.join(item[7])
        # item[8] = '/'.join(item[8])
        # item[9] = '/'.join(item[9])
        return item

    allData = list(getAllData())
    return list(map(map_fn, allData))

def getTableList1():
    def map_fn(item):
        # item[1] = '/'.join(item[1])
        # item[4] = '/'.join(item[4])
        # item[7] = '/'.join(item[7])
        # item[8] = '/'.join(item[8])
        # item[9] = '/'.join(item[9])
        return item

    allData1 = list(getAllData1())
    return list(map(map_fn, allData1))
