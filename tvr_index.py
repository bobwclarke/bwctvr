## index.py

import os

import time

import json
from pprint import pprint

from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, '/')

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

@ask.launch
def start_skill():
    welcome_message = 'What should the t.v. do?'
    return question(welcome_message)

@ask.intent('ChangePowerIntent')
def change_power(power_value):
    # Tell LIRC to send IR LED blink pattern to turn TV on/off
    os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, power_button_command))

    text = 'Turning the t.v. {}'.format(power_value)

    print('Received: ChangePowerIntent')
    print('-' + text)
    return statement(text)

@ask.intent('ChangeMuteIntent')
def change_mute(power_value, sound_value):
    print('Received: ChangeMuteIntent')
    os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, mute_button_command))

    sound_on_off_text = 'Turning the t.v.\'s sound {}'.format(power_value)
    mute_text = 'Telling the t.v. to {}'.format(sound_value)
    button_text = 'Pressing mute button on the t.v.'
    
    if power_value is None and sound_value is not None:
	print('-' + mute_text)
        return statement(mute_text)
    elif power_value is not None and sound_value is None:
	print('-' + sound_on_off_text)
        return statement(sound_on_off_text)
    else:
	print('-' + button_text)
        return statement(button_text)


@ask.intent('ChangeVolumeIntent')
def change_volume(up_down_value, num_value):
    print('Received: ChangeVolumeIntent')

    volume_up_text = 'Increasing volume'
    volume_down_text = 'Decreasing volume'
    
    if up_down_value == 'up' or up_down_value == 'increase':
        volume_direction = volume_up_button_command
        direction_text = volume_up_text
    else:
        volume_direction = volume_down_button_command
        direction_text = volume_down_text
    
    if num_value == 0 or num_value is None:
        volume_text = direction_text
        number_of_presses = 10
    else:
        volume_text = direction_text + ' by {}'.format(num_value)
        number_of_presses = int(num_value)
    
    for x in range (0, number_of_presses ):
        os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, volume_direction))
        time.sleep(0.2)   
    
    print('-' + volume_text)
    return statement(volume_text)

def swap_source(number_of_presses, direction_command):
    os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, source_button_command))
    time.sleep(1.5)

    for x in range (0, number_of_presses ):
        os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, direction_command))
        time.sleep(0.2)
    
    os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, ok_button_command))
    time.sleep(0.2)

def write_source_to_file(next_source, file):
    tv_source_file = open(file, "r+")
    last_source = tv_source_file.read()
    tv_source_file.seek(0)
    tv_source_file.truncate()
    tv_source_file.write(next_source)
    tv_source_file.close()
    return last_source
        

@ask.intent('ChangeSourceIntent')
def change_source(source_value):
    print('Received: ChangeSourceIntent')
    next_source = source_value

    last_source = write_source_to_file(next_source, "tv_source.txt")

    lastsource = last_source.replace(" ", "")
    nextsource = next_source.replace(" ", "")
    last_source_pos = tv_sources[lastsource.lower()]
    next_source_pos = tv_sources[nextsource.lower()]
    
    diff = last_source_pos - next_source_pos
    if diff == 0:
        no_change_text = 't.v. is already on ' + next_source
	print('-' + no_change_text)
        return statement(no_change_text)
    
    elif diff + 7 > 10:
        number_of_presses = 7 - diff
        
        swap_source(number_of_presses, down_button_command)
    
    elif diff + 7 > 7:
        number_of_presses = diff
        
        swap_source(number_of_presses, up_button_command)
    
    elif diff + 7 > 3:
        number_of_presses = diff * (-1)
        
        swap_source(number_of_presses, down_button_command)
    
    else:
        number_of_presses = diff + 7
        
        swap_source(number_of_presses, up_button_command)
        

    change_source_text = 'switching t.v. source to ' + next_source

    print('-' + change_source_text)
    return statement(change_source_text)

@ask.intent('SetSourceIntent')
def set_source(source_value, next_source_value):
    print('Received: SetSourceIntent')

    write_source_to_file(source_value, "tv_source.txt")
    
    if next_source_value is None:
        text = 'the t.v. source is set to {}'.format(source_value)
	print('-' + text)
        return statement(text)
    else:
        return change_source(next_source_value)

@ask.intent('PressButtonIntent')
def press_button(button_value, button_two_value, button_three_value):
    print('Received: PressButtonIntent')

    button_command = commands[button_value]
    os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, button_command))
    
    if button_two_value is not None:
        time.sleep(0.2)
        button_command = commands[button_two_value]
        os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, button_command))
        
    if button_three_value is not None:
        time.sleep(0.2)
        button_command = commands[button_three_value]
        os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, button_command))
    print('-OK')
    return statement('OK')

@ask.intent('ChangeChannelIntent')
def change_channel(channel_value, num_value):

    print('Received: ChangeChannelIntent')

    if channel_value is not None:
        text = 'changing channel to ' + channel_value
	chan = channel_value.replace(" ", "")
        channel = channels[chan.lower()]
    else:
        text = 'changing channel to ' + num_value
        channel = str(num_value)
    
    buttons = [int(n) for n in str(channel)]
    
    i = 0
    while i < len(buttons):
        this_button = buttons[i]
        button_command = commands[this_button]
        os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, button_command))
        time.sleep(0.2)
        i += 1

    print('-' + text)
    return statement(text)
    
@ask.intent('GetSourceIntent')
def get_source():
    print('Received: GetSourceIntent')

    source = open("tv_source.txt", "r")
    
    text = 'the t.v. source is set to {}'.format(source.read())
    
    source.close()
    
    print('-' + text)
    return statement(text)


if __name__ == '__main__':
    app.run(debug=True)
