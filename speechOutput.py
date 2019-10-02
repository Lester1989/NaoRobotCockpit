# -*- coding: utf-8 -*-

import sys
from naoqi import ALProxy


_ip = "127.0.0.1"
_port = 9559

_speed = -1
_pitch = -1

_what_object = ""
_what_bin = ""
_confirm = ""
_repeat = ""
_proband_repeat = ""
_reset_object = ""
_goodbye = ""
_thanks = ""

_eyecolor = [-1,-1,-1]
_ledProxy = 123
_ttsProxy = 123

_picked_object = " Ding"
_bin = ""

_ttAsProxy = None

_state_counter = 0

def set_params(condition, nao_ip, nao_port):
    """
    Sets the parameters for the speech output to create the desired attitude.

    Possible parameters are:
    "friendly"
    "neutral"
    "submissive"
    """

    global _ip
    _ip = nao_ip

    global _port
    _port = nao_port

    global _eyecolor
    global _what_object
    global _what_bin
    global _confirm
    global _repeat
    global _proband_repeat
    global _reset_object
    global _goodbye
    global _thanks
    global _initial_state

    global _pitch
    global _speed

    global _state_counter
    _state_counter = 0

    # set parameters depending on condition
    if(condition == "friendly"):

        _eyecolor = [0,227,94]

        _what_object = "Welches Objekt soll ich weg räumen?"
        _what_bin = "Alles klar, in welchen Mülleimer gehört {0}?"
        _confirm = "Super, dann räume ich {0} in den {1}"
        _repeat = "Toll, wir haben die Aufgabe erledigt! Möchtest du sie noch mal mit mir durchführen?"
        _goodbye = "Alles klar, dann danke und bis zum nächsten Mal!"
        _thanks = "Super, danke dir"

        _proband_repeat = "Oh, das hab ich nicht verstanden. Was hast du gesagt?"
        _reset_object = "Uups. Kannst du mir {0} wieder auf den Tisch stellen?"
        _initial_state = "O käi gut, dann brauche ich deine Hilfe. Räume die Gegenstände bitte wieder so auf den Tisch, so dass ich sie erreichen kann."
        
        
        _pitch = 120
        _speed = 110

    elif(condition == "neutral"):

        _eyecolor = [255,255,255]

        _what_object = "Welches Objekt soll ich nehmen?"
        _what_bin = "In welchen Mülleimer gehört {0}?"
        _confirm = "O käi, ich räume {0} in den  {1}"
        _repeat = "Die Aufgabe ist abgeschlossen. Möchtest du sie wiederholen?"
        _goodbye = "O käi, vielen Dank und auf wiedersehen."
        _thanks = "danke"

        _proband_repeat = "Das habe ich nicht verstanden. Kannst du das wiederholen?"
        _reset_object = "Oh. Bitte stell {0} wieder auf den Tisch."
        _initial_state = "Damit das Szenario neu gestartet werden kann, müssen die Gegenstände auf dem Tisch stehen."
        
        _pitch = 100
        _speed = 100

    elif(condition == "submissive"):

        _eyecolor = [255,0,127]

        _what_object = "Welches der Objekte vor mir darf ich nehmen?"
        _what_bin = "Und in welchen der beiden Mülleimer soll ich {0} werfen?"
        _confirm = "Verstanden, dann räume ich {0} in den {1}"
        _repeat = "Sieht so aus als wäre die Aufgabe erledigt, oder? Möchtest du sie noch mal durchführen?"
        _goodbye = "Alles klar. Wenn du noch mal Lust hast, dann kann ich hier auf dich warten. Bis dann!"
        _thanks = "Vielen Dank, tut mir leid"

        _proband_repeat = "Entschuldigung, das habe ich nicht verstanden. Würdest du das noch ein mal wiederholen?"
        _reset_object = "Entschuldigung. Könntest du mir {0} bitte wieder auf den Tisch stellen?"
        _initial_state = "Danke sehr, aber ich benötige deine Hilfe. Kannst du bitte die Gegenstände wieder auf den Tisch stellen?"
        
        _pitch = 95
        _speed = 95

    else:
        print("invalid condition")

    _ledProxy = ALProxy("ALLeds", _ip, _port)
    _ledProxy.fadeRGB("FaceLeds", 256*256*_eyecolor[0] + 256*_eyecolor[1] + _eyecolor[2], 0.1)

    global _ttsProxy
    _ttsProxy = ALProxy("ALTextToSpeech", _ip, _port)
    _ttsProxy.setLanguage("German")
    
    global _ttAsProxy
    _ttAsProxy = ALProxy("ALAnimatedSpeech", _ip, _port)

    print("parameters where set for specified attitude")



def welcome():
    """
    Let Nao say the introduction text for the study with non-edited voice.
    """

    configuration = {"bodyLanguageMode":"contextual"}
    _ttAsProxy.say("\RSPD="+ str(_speed) + "\ \VCT="+ str(_pitch) + "\  Hallo. Schön, dass du da bist. Ich möchte gerne dabei helfen, die Welt aufzuräumen. Dafür lerne ich grade die Mülltrennung und" +
    " versuche  mit deiner Hilfe   die vor mir liegenden Objekte in den richtigen Mülleimer links und rechts hinter mir sortieren. Dazu frage ich dich zuerst nach dem Objekt, welches ich nehmen soll. Danach frage ich dich nach dem Mülleimer, in welchen das Objekt gehört. Du kannst mir die Antwort einfach sagen. "+
    "Den richtigen Mülleimer für jedes Objekt erkennst du an der Markierung an dem Behälter. "+
    "Wenn alle Objekte sortiert sind, haben wir die Aufgabe erledigt. Danach können wir das ganze wiederholen, damit ich das noch mal üben kann. Hast du noch Fragen? \RST\ ",configuration)


def ask_what_object():
    """
    Ask for the object to pick next.
    """

    sentence = "\RSPD="+ str(_speed) + "\ "
    sentence += "\VCT="+ str(_pitch) + "\ "
    sentence += str(_what_object)
    sentence +=  "\RST\ "
    _ttsProxy.say(sentence)


def ask_what_bin(picked_object = 'Ding'):
    """
    Ask for the bin the previously picked object should be put in.

    parameters:
    picked_object: the previously picked object. 
        valid parameters are "ball", "flasche", "vitalis", "somat"
    """

    global _picked_object

    if(picked_object == "Kuscheltier"):
        article = "das "
        _picked_object = "Kuscheltier "
    elif(picked_object == "flasche"):
        article = "die "
        _picked_object = "Flasche "
    elif(picked_object == "vitalis"):
        article = "das "
        _picked_object = "Müsli "
    elif(picked_object == "somat"):
        article = "das "
        _picked_object = "Spülmittel "
    else:
        article = "das "
        _picked_object = "Ding "

    concatinatedText = _what_bin.format(article + _picked_object)

    sentence = "\RSPD="+ str(_speed) + "\ "
    sentence += "\VCT="+ str(_pitch) + "\ "
    sentence += str(concatinatedText)
    sentence +=  "\RST\ "
    _ttsProxy.say(sentence)


def confirm(picked_bin ='Müll'):
    """
    Confirm the users choice of the object and the bin to put it in.

    parameters:
    picked_bin: the previously picked bin.
        valid parameters are "wertstoff", "altpapier"
    """

    global _bin

    if(picked_bin == "wertstoff"):
        _bin = " Wertstoff Behälter."
    elif(picked_bin == "altpapier"):
        _bin = " Altpapier Behälter."
    else:
        _bin = 'Müll.'


    if(_picked_object == "Kuscheltier "):
        article = "das "
    elif(_picked_object == "Flasche "):
        article = "die "
    elif(_picked_object == "Müsli "):
        article = "das "
    elif(_picked_object == "Spülmittel "):
        article = "das "
    else:
        article = 'das'

    concatinatedText = _confirm.format("" + article + _picked_object, _bin)

    sentence = "\RSPD="+ str(_speed) + "\ "
    sentence += "\VCT="+ str(_pitch) + "\ "
    sentence += str(concatinatedText)
    sentence +=  "\RST\ "
    _ttsProxy.say(sentence)


def repeat():
    """ 
    Ask if the user wants to repeat the task.
    """

    sentence = "\RSPD="+ str(_speed) + "\ "
    sentence += "\VCT="+ str(_pitch) + "\ "
    sentence += str(_repeat)
    sentence +=  "\RST\ "
    _ttsProxy.say(sentence)


def ask_for_help():
    """
    Ask if the user would put the object back on the desk.
    """
    
    if(_picked_object == "Ball "):
        article = "den "
    elif(_picked_object == "Flasche "):
        article = "die "
    elif(_picked_object == "Müsli "):
        article = "das "
    elif(_picked_object == "Spülmittel "):
        article = "das "
    else:
        article = 'das '

    concatinatedText = _reset_object.format(article + _picked_object)

    sentence = "\RSPD="+ str(_speed) + "\ "
    sentence += "\VCT="+ str(_pitch) + "\ "
    sentence += str(concatinatedText)
    sentence +=  "\RST\ "
    _ttsProxy.say(sentence)
    
def thank_you():
    """
    
    """
    
    sentence = "\RSPD="+ str(_speed) + "\ "
    sentence += "\VCT="+ str(_pitch) + "\ "
    sentence += str(_thanks)
    sentence +=  "\RST\ "
    _ttsProxy.say(sentence)



def proband_repeat():
    sentence = "\RSPD="+ str(_speed) + "\ "
    sentence += "\VCT="+ str(_pitch) + "\ "
    sentence += str(_proband_repeat)
    sentence +=  "\RST\ "
    _ttsProxy.say(sentence)

def initial_state():
    sentence = "\RSPD="+ str(_speed) + "\ "
    sentence += "\VCT="+ str(_pitch) + "\ "
    sentence += str(_initial_state)
    sentence +=  "\RST\ "
    _ttsProxy.say(sentence)
    
def ask_bin():
    sentence = "\RSPD="+ str(_speed) + "\ "
    sentence += "\VCT="+ str(_pitch) + "\ "
    sentence += str(_ask_bin)
    sentence +=  "\RST\ "
    _ttsProxy.say(sentence)


def goodbye():
    sentence = "\RSPD="+ str(_speed) + "\ "
    sentence += "\VCT="+ str(_pitch) + "\ "
    sentence += str(_goodbye)
    sentence +=  "\RST\ "
    _ttsProxy.say(sentence) 
    
def free_speech(text):
    sentence = "\RSPD="+ str(_speed) + "\ "
    sentence += "\VCT="+ str(_pitch) + "\ "
    sentence += str(text.toUtf8())
    sentence +=  "\RST\ "
    _ttsProxy.say(sentence) 
