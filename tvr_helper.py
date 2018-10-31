import os
import time
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

def swap_source(self, number_of_presses, direction_command):
    os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, source_button_command))
    time.sleep(1.5)

    for x in range (0, number_of_presses ):
        os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, direction_command))
        time.sleep(0.2)
    
    os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, ok_button_command))
    time.sleep(0.2)
    return True