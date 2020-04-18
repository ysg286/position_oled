#!/usr/bin/env python
#
# BakeBit example for the basic functions of BakeBit 128x32 OLED
#
# The BakeBit connects the NanoPi NEO (NEO2) and BakeBit sensors.
# You can learn more about BakeBit here:  http://wiki.friendlyarm.com/BakeBit
#
# Have a question about this example?  Ask on the forums here:  http://www.friendlyarm.com/Forum/
#

import threading
import bakebit_128_64_oled as oled
import LZ_NET_inter
from addict import Dict
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

oled.init()  # initialze SEEED OLED display
oled.clearDisplay()  # clear the screen and set start position to top left corner
oled.setNormalDisplay()  # Set display to normal mode (i.e non-inverse mode)
oled.setHorizontalMode()

# 按键状态初始化未按下
key_state = {'return': True, 'landing': True, 'search': True, 'direction': True}
# 远程4G
remote_state = False
# LZ探测板状态
LZ_survey_state = {'login': False, 'GPS': ['longitude', 'latitude'], 'drone_num': 0}
# 无人机列表
drone_list = []


class Drone:

    def __init__(self, buzzer_level=0, id='60601f141701', name='DJI Mavic', freq_khz='2450500', signal_dbm='-69'):
        self.buzzer_level = buzzer_level
        self.id = id
        self.name = name
        self.freq_khz = freq_khz
        self.signal_dbm = signal_dbm


# 定义OLED屏显示刷新方法
# def oled_action():
while True:

    # image = Image.open('./logo/friendllyelec.png').convert('1')
    # oled.drawImage(image)
    # time.sleep(3)
    width = 128
    height = 64
    logo_x = 21
    logo_y = 21
    logo_disment = 1
    # 画布
    image_background = Image.new('1', (width, height))
    # Get drawing object to draw on image.
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(image_background)
    # Load default font.


    # Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
    # Some other nice fonts to try: http://www.dafont.com/bitmap.php
    # font = ImageFont.truetype('Minecraftia.ttf', 8)

    # 图标分割线
    draw.line((0, logo_y + 1, width, logo_y + 1), fill=128)
    oled.drawImage(image_background)
    time.sleep(10)
    #
    # # 2.4G&5.8G 1.5G 探测/寻向 无人机 远程 定位
    # #    1      2      3  4    5    6    7
    # image_return = Image.open('./logo/return.jpg').convert('1').resize((logo_x, logo_y))
    # image_gps = Image.open('./logo/gps.jpg').convert('1').resize((logo_x, logo_y))
    # image_search = Image.open('./logo/search.jpg').convert('1').resize((logo_x, logo_y))
    # image_position = Image.open('./logo/position.jpg').convert('1').resize((logo_x, logo_y))
    # image_uav = Image.open('./logo/UAV.jpg').convert('1').resize((logo_x, logo_y))
    # image_remote = Image.open('./logo/remote.jpg').convert('1').resize((logo_x, logo_y))
    # image_location = Image.open('./logo/location.jpg').convert('1').resize((logo_x, logo_y))
    # # 图标横幅
    # logo_image = [image_return, image_gps, image_search, image_position, image_uav, image_remote, image_location]
    #


    # while True:
    #     # 前4个图标
    #     key_values = list(key_state.values())
    #     for i in range(len(key_values)):  # 0123
    #         if key_values[i]:
    #             image_background.paste(logo_image[i], (i * (logo_x + logo_disment), i * (logo_y + logo_disment)))
    #         else:
    #             # Draw a black filled box to clear the image.
    #             draw.rectangle(
    #                 (i * (logo_x + logo_disment), i * (logo_y + logo_disment), (i + 1) * logo_x, (i + 1) * logo_y),
    #                 outline='white', fill='white')
    #
    #     # 后两个图标和探测板通信
    #     if not LZ_survey_state['login']:
    #         draw.text((2, logo_y + logo_disment), 'Detector Starting...', font=font, fill=255)
    #     else:  # 通信正常后显示探测板数据
    #         draw.rectangle((2, logo_y + logo_disment, 128, logo_y + logo_disment), fill='white')
    #         # 临时列表组合配合图标横幅4，5
    #         logo_values4 = list(LZ_survey_state['drone_num'], remote_state)
    #         for i in range(4, 5):
    #             if logo_values4[i - 4] > 0:
    #                 image_background.paste(logo_image[i], (i * (logo_x + logo_disment), i * (logo_y + logo_disment)))
    #             else:
    #                 # Draw a black filled box to clear the image.
    #                 draw.rectangle(
    #                     (i * (logo_x + logo_disment), i * (logo_y + logo_disment), (i + 1) * logo_x, (i + 1) * logo_y),
    #                     outline='white', fill='white')
    #
    #     # 探测到无人机信息显示******暂时只显示一个
    #     if LZ_survey_state['drone_num'] > 0 and key_state['search']:
    #         draw.text((2, logo_y + logo_disment), drone_list[0].name, font=font, fill=255)
    #         draw.text((2, logo_y + logo_disment + 20), drone_list[0].freq_khz, font=font, fill=255)
    #         if key_state['position']:
    #             draw.rectangle((0, 0, 128, 64), fill='white')
    #             while key_state['position']:
    #                 # 寻向开启显示方位图
    #                 draw.ellipse((32, 0, 96, 128), outline=255, fill=0)
    #                 draw.line((64, 0, 64, 64), fill=255)
    #                 draw.line((32, 0, 64, 96), fill=255)
    #                 oled.drawImage(image_background)
    #                 time.sleep(0.1)
    #         else:  # 寻向关闭清除圆圈
    #             draw.rectangle((0, 0, 128, 64), fill='white')
    #
    #     else:  # 清除
    #         draw.rectangle((2, logo_y + logo_disment, 128, 64), fill='white')
    # oled.drawImage(image_background)
    # time.sleep(0.5)  # 刷屏间隔

#
# # 定义LZ探测板数据读取方法
# def LZ_data_obtain():
#     # 先登陆
#     while not LZ_survey_state['login']:
#         token = LZ_NET_inter.login()
#         if token == '':
#             LZ_survey_state['login'] = False
#         else:
#             LZ_survey_state['login'] = True
#         time.sleep(1)  # 间隔1s
#     while True:
#         achieve = Dict(LZ_NET_inter.detection_drone(token))
#         LZ_survey_state['drone_num'] = len(achieve.data.drone)  # 数量
#         for i in range(LZ_survey_state['drone_num']):
#             drone = Drone()  # 实例化1
#             drone.buzzer_level = achieve.data.drone[i].buzzer_level
#             drone.id = achieve.data.drone[i].buzzer_level
#             drone.name = str(achieve.data.drone[i].name)
#             drone.freq_khz = str(achieve.data.drone[i].seen_sensor[0].detected_freq_khz)
#             drone.signal_dbm = str(achieve.data.drone[i].seen_sensor[1].signal_dbm)
#             drone_list.append(drone)
#
#         time.sleep(0.5)  # 读取间隔

# # 定义地磁数据读取方法
# def magnet_obtain():
#     pass
#
#
# # 定义远程和数据上传方法
# def remote_control():
#     pass
# display_run = threading.Thread(target=oled_action)
# display_run.start()
# LZ_data = threading.Thread(target=LZ_data_obtain)
# LZ_data.start()
