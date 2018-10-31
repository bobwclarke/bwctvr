"""
Logic between the Raspberry Pi and the LED light. Changes maintained through
the Light object and the pigpio daemon connection.
"""
"""
import time
import logging

import pigpio

from light_values import RGB, CANDLE

# Respective Gpio ports
R_PIN = 4
G_PIN = 17
B_PIN = 22

# Gpio ports representation in RGB tuple
PINS = RGB(r=R_PIN, g=G_PIN, b=B_PIN)

# OFF color setting to turn lights off
OFF = RGB(r=0, g=0, b=0)
"""
import os

import time
import logging
import tvr_helper
import json
from pprint import pprint

lirc_file_conf = 'TVremote'
power_button_command = 'KEY_POWER'
mute_button_command = 'KEY_MUTE'
zero_button_command = 'KEY_0'
one_button_command = 'KEY_1'
two_button_command = 'KEY_2'
three_button_command = 'KEY_3'
four_button_command = 'KEY_4'
five_button_command = 'KEY_5'
six_button_command = 'KEY_6'
seven_button_command = 'KEY_7'
eight_button_command = 'KEY_8'
nine_button_command = 'KEY_9'
source_button_command = 'KEY_MODE'
up_button_command = 'KEY_UP'
down_button_command = 'KEY_DOWN'
left_button_command = 'KEY_LEFT'
right_button_command = 'KEY_RIGHT'
volume_up_button_command = 'KEY_VOLUMEUP'
volume_down_button_command = 'KEY_VOLUMEDOWN'
menu_button_command = 'KEY_MENU'
exit_button_command = 'KEY_EXIT'
channel_up_button_command = 'KEY_CHANNELUP'
channel_down_button_command = 'KEY_CHANNELDOWN'
ok_button_command = 'KEY_OK'
info_button_command = 'KEY_INFO'
picture_mode_button_command = 'KEY_VIDEO'
audio_mode_command = 'KEY_AUDIO'
epg_button_command = 'KEY_EPG'

commands = {
    'power': 'KEY_POWER',
    'mute': 'KEY_MUTE',
    'zero': 'KEY_0',
    'oh': 'KEY_0',
    'one': 'KEY_1',
    'two': 'KEY_2',
    'three': 'KEY_3',
    'four': 'KEY_4',
    'five': 'KEY_5',
    'six': 'KEY_6',
    'seven': 'KEY_7',
    'eight': 'KEY_8',
    'nine': 'KEY_9',
    '0': 'KEY_0',
    '1': 'KEY_1',
    '2': 'KEY_2',
    '3': 'KEY_3',
    '4': 'KEY_4',
    '5': 'KEY_5',
    '6': 'KEY_6',
    '7': 'KEY_7',
    '8': 'KEY_8',
    '9': 'KEY_9',
    0: 'KEY_0',
    1: 'KEY_1',
    2: 'KEY_2',
    3: 'KEY_3',
    4: 'KEY_4',
    5: 'KEY_5',
    6: 'KEY_6',
    7: 'KEY_7',
    8: 'KEY_8',
    9: 'KEY_9',
    'source': 'KEY_MODE',
    'up': 'KEY_UP',
    'down': 'KEY_DOWN',
    'left': 'KEY_LEFT',
    'right': 'KEY_RIGHT',
    'menu': 'KEY_MENU',
    'exit': 'KEY_EXIT',
    'back': 'KEY_EXIT',
    'channel up': 'KEY_CHANNELUP',
    'channel down': 'KEY_CHANNELDOWN',
    'OK': 'KEY_OK',
    'ok': 'KEY_OK',
    'select': 'KEY_OK',
    'info': 'KEY_INFO',
    'information': 'KEY_INFO',
    'picture mode': 'KEY_VIDEO',
    'video mode': 'KEY_VIDEO',
    'image mode': 'KEY_VIDEO',
    'picture': 'KEY_VIDEO',
    'audio': 'KEY_AUDIO',
    'audio mode': 'KEY_AUDIO',
    'sound mode': 'KEY_AUDIO',
    'EPG': 'KEY_EPG',
    'guide': 'KEY_EPG',
    'tv guide': 'KEY_EPG'
    }

sound_commands ={
    'power': 'KEY_POWER',
    'eq': 'KEY_AUDIO',
    'mute': 'KEY_MUTE',
    'bluetooth': 'KEY_BLUE',
    'aux': 'KEY_AUX',
    'opt': 'KEY_OPTION',
    'volup': 'KEY_VOLUMEUP',
    'voldown': 'KEY_VOLUMEDOWN',
    'playpause': 'KEY_PLAY',
    'rewind': 'KEY_REWIND',
    'forward': 'KEY_FASTFORWARD'
    }

tv_sources = {
    'freeviewtv': 0,
    'freeview': 0,
    'normaltv' : 0,
    'livetv': 0,
    'preview': 0,
    'previewtv': 0,
    'analoguetv': 1,
    'analogue':1,
    'analogtv':1,
    'analog':1,
    'compositeav': 2,
    'composite': 2,
    'av':2,
    'componentypbpr': 3,
    'component': 3,
    'hdmi1': 4,
    'hdmione': 4,
    'chromecast': 4,
    'netflix': 4,
    'hdmi2': 5,
    'hdmitwo': 5,
    'xbox': 5,
    'hdmi3': 6,
    'hdmithree': 6
    }

channels = {
    'bbc': '101',
    'bbchd': '101',
    'bbc1hd': '101',
    'bbconehd': '101',
    'onehd': '101',
    '1hd': '101',
    'bbc1': '001',
    'bbcone': '001',
    'bbc2hd': '102',
    'bbctwohd': '102',
    'twohd': '102',
    '2hd': '102',
    'bbc2': '002',
    'bbctwo': '002',
    'bbc4': '009',
    'bbcfour': '009',
    'itv': '103',
    'itvhd': '103',
    'itv1hd': '103',
    'itvonehd': '103',
    'itv1': '003',
    'itvone': '003',
    'itv2': '006',
    'itvtwo': '006',
    'itv1plus1': '033',
    'itvoneplusone': '033',
    'itv2plus1': '027',
    'itvtwoplusone': '027',
    'itv3': '010',
    'itvthree': '010',
    'itv4': '024',
    'itvfour': '024',
    'channel4': '004',
    'channelfour': '004',
    'channel4hd': '104',
    'channelfourhd': '104',
    '4hd': '104',
    'fourhd': '104',
    'channel5': '005',
    'channel5hd': '005',
    'channelfive': '005',
    'channel5hd': '105',
    'channelfivehd': '105',
    'fivehd': '105',
    '5hd': '105',
    'channel4plus1': '013',
    'channelfourplusone': '013',
    'dave': '012',
    'e4': '028',
    'efour': '028',
    'e4plus1': '029',
    'efourplusone': '029',
    'film4': '015',
    'filmfour': '015',
    'more4': '014',
    'morefour': '014'
    }

# Logger information
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

class Remote(object):
    """
    Light object to maintian logic of the state of the lights and
    Gpio ports
    """
    def __init__(self):
        super(Remote, self).__init__()
        ## Default start up settings
        self.last_timestamp = 0
        self.power_value = 'off'
        self.mute_value = 'unmute'
        self.volume_value = '0'
        self.source_value = 'unknown'
        self.channel_value = 'unknown'
        self.button_value = 'none'

    def current_settings(self):
        """
        Gives current settings of Remote object.

        Returns:
            Python dict of Temote object power state and brightness
        """
        return {
                   'I_dont_want_to': 'respond_anything'
               }

    def needs_updating(self, remote_data_timestamp):
        
            
        if remote_data_timestamp != self.last_timestamp:
            self.last_timestamp = remote_data_timestamp
            return True
        return False

    def update_remote(self, remote_data):
        
        if remote_data.get('ChangePowerIntent') is not None:
            intent_data = remote_data.get('ChangePowerIntent')
            self._update_power(intent_data)
        if remote_data.get('ChangeMuteIntent') is not None:
            intent_data = remote_data.get('ChangeMuteIntent')
            self._update_mute(intent_data)
        if remote_data.get('ChangeVolumeIntent') is not None:
            intent_data = remote_data.get('ChangeVolumeIntent')
            self._update_volume(intent_data)
        if remote_data.get('ChangeSourceIntent') is not None:
            intent_data = remote_data.get('ChangeSourceIntent')
            self._update_source(intent_data)
        if remote_data.get('ChangeChannelIntent') is not None:
            intent_data = remote_data.get('ChangeChannelIntent')
            self._update_channel(intent_data)
        if remote_data.get('PressButtonIntent') is not None:
            intent_data = remote_data.get('PressButtonIntent')
            self._update_buttons(intent_data)

    def _update_power(self, intent_data):
        self.power_value = intent_data.get('power_value')
        os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, power_button_command))
        logger.info(self.power_value)
        
    def _update_mute(self, intent_data):
        self.mute_value = intent_data.get('mute_value')
        os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, mute_button_command))
        logger.info(self.mute_value)
    
    def _update_volume(self, intent_data):
        
        up_down_value = intent_data.get('up_down_value').lower()
        num_value = intent_data.get('num_of_presses')
        
        if up_down_value == 'increasing volume':
            volume_direction = volume_up_button_command
        else:
            volume_direction = volume_down_button_command
    
        if num_value == 0 or num_value is None:
            number_of_presses = 10
        else:
            number_of_presses = int(num_value)
    
        for x in range (0, number_of_presses ):
            os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, volume_direction))
            time.sleep(0.2)
        
        self.volume_value = up_down_value + ' ' + num_value
        logger.info(self.volume_value)
    
    def _update_source(self, intent_data):
        next_source = intent_data.get('set_source')

        if intent_data.get('last_source') is None:
            self.source_value = next_source
            return
        else:
            last_source = intent_data.get('last_source')

        lastsource = last_source.replace(" ", "")
        nextsource = next_source.replace(" ", "")
        last_source_pos = tv_sources[lastsource.lower()]
        next_source_pos = tv_sources[nextsource.lower()]
        
        diff = last_source_pos - next_source_pos
        if diff + 7 > 10:
            number_of_presses = 7 - diff
        
            tvr_helper.swap_source(self, number_of_presses, down_button_command)
    
        elif diff + 7 > 7:
            number_of_presses = diff
        
            tvr_helper.swap_source(self, number_of_presses, up_button_command)
    
        elif diff + 7 > 3:
            number_of_presses = diff * (-1)
        
            tvr_helper.swap_source(self, number_of_presses, down_button_command)
    
        else:
            number_of_presses = diff + 7
        
            tvr_helper.swap_source(self, number_of_presses, up_button_command)
        
        self.source_value = next_source
        logger.info(self.source_value)
    
    def _update_channel(self, intent_data):
        
        self.channel_value = intent_data.get('channel_value')
        
        buttons = [int(n) for n in str(self.channel_value)]
    
        i = 0
        while i < len(buttons):
            this_button = buttons[i]
            button_command = commands[this_button]
            os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, button_command))
            time.sleep(0.2)
            i += 1
        
        logger.info(self.channel_value)
        
    def _update_buttons(self, intent_data):
        
        self.button_value = intent_data.get('buttons_pressed')
        button_one_value = self.button_value[0]
        button_two_value = self.button_value[1]
        button_three_value = self.button_value[2]
        
        button_command = commands[button_one_value]
        os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, button_command))
    
        if button_two_value is not None:
            time.sleep(0.2)
            button_command = commands[button_two_value]
            os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, button_command))
        
        if button_three_value is not None:
            time.sleep(0.2)
            button_command = commands[button_three_value]
            os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, button_command))
        
        logger.info(self.button_value)
    