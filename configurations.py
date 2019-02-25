#!/usr/bin/env python
# -*- coding=utf8 -*-
# Created by dengqiangxi at 2018/4/9
'''
可选的配置中，不需要的注释掉就可以了
'''
mail_config = {
    # 服务server,改成自己的
    'smtpserver': 'smtp.hichina.com',
    # 发送邮件端口
    'smtpport': 465,
    # 邮件密码
    'password': '******1111',
    # 发送者
    'sender': 'xxxx@xxxxxxx.com',
    # 接受者  发送者和接受者可以是同一个邮箱
    'receiver': 'xxxx@xxxxxxx.com',
}
config = {
    # 高德地图key可以放入多个，可以从高德开发者平台创建多个key
    'keys': [
        "bb0c3ddf6525d426aba619d8bf79bfaa"
    ],
    # 必选 房源url，可以多个
    'urls': [
        "http://sz.ziroom.com/z/nl/z2-r1111TO1700-s2%E5%8F%B7%E7%BA%BF%28%E8%9B%87%E5%8F%A3%E7%BA%BF%29-t%E9%BB%84%E8%B4%9D%E5%B2%AD.html"
    ],
    # 望京SOHO 经纬度，替换成自己的坐标，坐标可以从 http://www.gpsspg.com/maps.htm 获得，选腾讯高德坐标
    'latlng': '114.0948290000，22.5406410000',
    # 可选 房间朝向
    # 'toward':'南',
    # 可选 过滤掉的房间朝向
    'not_towards': [
        '北'
    ],
    # 必选 最高价格 土豪自己改代码
    "max_price": 1700,
    # 可选 最大步行距离 单位：米
    "max_distance": 500,
    # 可选 最长步行时间 单位：秒
    "max_time": 60 * 20
}
