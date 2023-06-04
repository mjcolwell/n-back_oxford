#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on May 18, 2023, at 12:47
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'N-Back (Version 4 - 2023) Behavioural Version'  # from the Builder filename that created this script
expInfo = {
    'participant': 'P0',
    'Task Version (1 or 2)': '1',
    'Pre or post': 'NA',
    'Practice (mainonly, prctonly, and both)': 'mainonly',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\PERL Admin\\Desktop\\PEACE Battery\\Behavioural Tasks\\0 nBack (practice only)\\N-Back_Behavioural_2023_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Start_Code" ---
# Run 'Begin Experiment' code from VersionCode
TaskVersion = expInfo['Task Version (1 or 2)'] 

TaskVersion = TaskVersion.replace(' ', '')

if TaskVersion == '1':
        VersionSelection = 'Conditions/NbackMaster_v1.xlsx'
        PracticeSelection = 'Conditions/NbackMasterPract_v1.xlsx'
        
if TaskVersion == '2':
        VersionSelection = 'Conditions/NbackMaster_v2.xlsx'
        PracticeSelection = 'Conditions/NbackMasterPract_v2.xlsx'
        
PracticeState = expInfo['Practice (mainonly, prctonly, and both)']

# Run 'Begin Experiment' code from MouseSet
win.setMouseVisible(False)
# Run 'Begin Experiment' code from SetBlock
BlockNo = 1
PractNo = 1

# --- Initialize components for Routine "LeftKeyCheck" ---
key_resp_8 = keyboard.Keyboard()
KeyChecker1 = visual.TextStim(win=win, name='KeyChecker1',
    text="Please press the 'left' key.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "RightKeyCheck" ---
key_resp_9 = keyboard.Keyboard()
KeyChecker2 = visual.TextStim(win=win, name='KeyChecker2',
    text="Please press the 'right' key.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "StartExpInst" ---
TaskVersionText = visual.TextStim(win=win, name='TaskVersionText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
InstrKey1 = keyboard.Keyboard()
PressToContinueText = visual.TextStim(win=win, name='PressToContinueText',
    text="Press 'left' or 'right' to continue.",
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "MainInstru1" ---
InstructionsText1 = visual.TextStim(win=win, name='InstructionsText1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "MainInstru2" ---
TextInstructions = visual.TextStim(win=win, name='TextInstructions',
    text="Press the 'right' key based on the rule (e.g letters appearing twice in a row). \n\nFor other letters, press the 'left' key.\n\nPress 'left' or 'right' to continue.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ContinueKey = keyboard.Keyboard()

# --- Initialize components for Routine "Maininstru3" ---
InstructionsText2 = visual.TextStim(win=win, name='InstructionsText2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "MainInstru4_2" ---
InstructionsText3 = visual.TextStim(win=win, name='InstructionsText3',
    text="Letters are uppercase (A,B,C) and lowercase (a,b,c).\n\nTreat uppercase and lowercase as the same (e.g., A = a).\n\nPress 'left' or 'right' to continue.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# --- Initialize components for Routine "MainInstru5" ---
InstructionsText4 = visual.TextStim(win=win, name='InstructionsText4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "InstructionsPractice" ---
PractIn1 = visual.TextStim(win=win, name='PractIn1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
PractIn2 = visual.TextStim(win=win, name='PractIn2',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
PractInstructionPass = keyboard.Keyboard()
PractBlock1 = visual.TextStim(win=win, name='PractBlock1',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
LeftText2 = visual.TextStim(win=win, name='LeftText2',
    text="Press 'left' when you see any other letter.",
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "Brief_ISI" ---
Brief_ISI_P = visual.TextStim(win=win, name='Brief_ISI_P',
    text='·',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.7255, 0.7255, 0.7255], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "trial_practice_3" ---
N_backP_2 = visual.TextStim(win=win, name='N_backP_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KeyPractice = keyboard.Keyboard()
ISI = visual.TextStim(win=win, name='ISI',
    text='·',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.7255, 0.7255, 0.7255], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "PracticeFeedbackRoutine" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "PractAdder" ---

# --- Initialize components for Routine "Transition" ---
TransitionText = visual.TextStim(win=win, name='TransitionText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_6 = keyboard.Keyboard()

# --- Initialize components for Routine "Transition2" ---
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "InstructionsTrial" ---
MainInt1 = visual.TextStim(win=win, name='MainInt1',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
MainInt2 = visual.TextStim(win=win, name='MainInt2',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
InstructionPass = keyboard.Keyboard()
Blocks1 = visual.TextStim(win=win, name='Blocks1',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
LeftText = visual.TextStim(win=win, name='LeftText',
    text="Press 'left' when you see any other letter.",
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "Brief_ISI" ---
Brief_ISI_P = visual.TextStim(win=win, name='Brief_ISI_P',
    text='·',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.7255, 0.7255, 0.7255], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "trial_proper" ---
N_backD = visual.TextStim(win=win, name='N_backD',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='·',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.7255, 0.7255, 0.7255], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Adder" ---

# --- Initialize components for Routine "EndOfExperiment" ---
EndOfExperimentText = visual.TextStim(win=win, name='EndOfExperimentText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Start_Code" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Start_CodeComponents = []
for thisComponent in Start_CodeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Start_Code" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_CodeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Start_Code" ---
for thisComponent in Start_CodeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Start_Code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "LeftKeyCheck" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
LeftKeyCheckComponents = [key_resp_8, KeyChecker1]
for thisComponent in LeftKeyCheckComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "LeftKeyCheck" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['left'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *KeyChecker1* updates
    if KeyChecker1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyChecker1.frameNStart = frameN  # exact frame index
        KeyChecker1.tStart = t  # local t and not account for scr refresh
        KeyChecker1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyChecker1, 'tStartRefresh')  # time at next scr refresh
        KeyChecker1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LeftKeyCheckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "LeftKeyCheck" ---
for thisComponent in LeftKeyCheckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "LeftKeyCheck" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "RightKeyCheck" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
RightKeyCheckComponents = [key_resp_9, KeyChecker2]
for thisComponent in RightKeyCheckComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "RightKeyCheck" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *KeyChecker2* updates
    if KeyChecker2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyChecker2.frameNStart = frameN  # exact frame index
        KeyChecker2.tStart = t  # local t and not account for scr refresh
        KeyChecker2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyChecker2, 'tStartRefresh')  # time at next scr refresh
        KeyChecker2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RightKeyCheckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "RightKeyCheck" ---
for thisComponent in RightKeyCheckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()
# the Routine "RightKeyCheck" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "StartExpInst" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from TaskNoPrint
VersionT = ('This is the n-back task version '+ TaskVersion)
TaskVersionText.setText(VersionT)
InstrKey1.keys = []
InstrKey1.rt = []
_InstrKey1_allKeys = []
# keep track of which components have finished
StartExpInstComponents = [TaskVersionText, InstrKey1, PressToContinueText]
for thisComponent in StartExpInstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "StartExpInst" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TaskVersionText* updates
    if TaskVersionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TaskVersionText.frameNStart = frameN  # exact frame index
        TaskVersionText.tStart = t  # local t and not account for scr refresh
        TaskVersionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TaskVersionText, 'tStartRefresh')  # time at next scr refresh
        TaskVersionText.setAutoDraw(True)
    
    # *InstrKey1* updates
    waitOnFlip = False
    if InstrKey1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        InstrKey1.frameNStart = frameN  # exact frame index
        InstrKey1.tStart = t  # local t and not account for scr refresh
        InstrKey1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstrKey1, 'tStartRefresh')  # time at next scr refresh
        InstrKey1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(InstrKey1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(InstrKey1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if InstrKey1.status == STARTED and not waitOnFlip:
        theseKeys = InstrKey1.getKeys(keyList=['right','left'], waitRelease=False)
        _InstrKey1_allKeys.extend(theseKeys)
        if len(_InstrKey1_allKeys):
            InstrKey1.keys = _InstrKey1_allKeys[-1].name  # just the last key pressed
            InstrKey1.rt = _InstrKey1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *PressToContinueText* updates
    if PressToContinueText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PressToContinueText.frameNStart = frameN  # exact frame index
        PressToContinueText.tStart = t  # local t and not account for scr refresh
        PressToContinueText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PressToContinueText, 'tStartRefresh')  # time at next scr refresh
        PressToContinueText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartExpInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "StartExpInst" ---
for thisComponent in StartExpInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if InstrKey1.keys in ['', [], None]:  # No response was made
    InstrKey1.keys = None
thisExp.addData('InstrKey1.keys',InstrKey1.keys)
if InstrKey1.keys != None:  # we had a response
    thisExp.addData('InstrKey1.rt', InstrKey1.rt)
thisExp.nextEntry()
# the Routine "StartExpInst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MainInstru1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
InstructionsText1.setText("In this task, you will see a series of letters appear on the screen. Only one letter will appear at a time. \n\nYou need to press the 'right' or 'left' key based on rules which change over time.\n\nPress 'left' or 'right' to continue.")
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
MainInstru1Components = [InstructionsText1, key_resp_4]
for thisComponent in MainInstru1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MainInstru1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionsText1* updates
    if InstructionsText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsText1.frameNStart = frameN  # exact frame index
        InstructionsText1.tStart = t  # local t and not account for scr refresh
        InstructionsText1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsText1, 'tStartRefresh')  # time at next scr refresh
        InstructionsText1.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['right','left'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MainInstru1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MainInstru1" ---
for thisComponent in MainInstru1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "MainInstru1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MainInstru2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ContinueKey.keys = []
ContinueKey.rt = []
_ContinueKey_allKeys = []
# keep track of which components have finished
MainInstru2Components = [TextInstructions, ContinueKey]
for thisComponent in MainInstru2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MainInstru2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextInstructions* updates
    if TextInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TextInstructions.frameNStart = frameN  # exact frame index
        TextInstructions.tStart = t  # local t and not account for scr refresh
        TextInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TextInstructions, 'tStartRefresh')  # time at next scr refresh
        TextInstructions.setAutoDraw(True)
    
    # *ContinueKey* updates
    waitOnFlip = False
    if ContinueKey.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        ContinueKey.frameNStart = frameN  # exact frame index
        ContinueKey.tStart = t  # local t and not account for scr refresh
        ContinueKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueKey, 'tStartRefresh')  # time at next scr refresh
        ContinueKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ContinueKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ContinueKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ContinueKey.status == STARTED and not waitOnFlip:
        theseKeys = ContinueKey.getKeys(keyList=['left','right'], waitRelease=False)
        _ContinueKey_allKeys.extend(theseKeys)
        if len(_ContinueKey_allKeys):
            ContinueKey.keys = _ContinueKey_allKeys[-1].name  # just the last key pressed
            ContinueKey.rt = _ContinueKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MainInstru2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MainInstru2" ---
for thisComponent in MainInstru2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ContinueKey.keys in ['', [], None]:  # No response was made
    ContinueKey.keys = None
thisExp.addData('ContinueKey.keys',ContinueKey.keys)
if ContinueKey.keys != None:  # we had a response
    thisExp.addData('ContinueKey.rt', ContinueKey.rt)
thisExp.nextEntry()
# the Routine "MainInstru2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Maininstru3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
InstructionsText2.setText("You have 2s to press a key from when a letter appears. \n\nYou must press the key before the next letter appears. Only the first press will be counted.\n\nPress 'left' or 'right' to continue.")
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Maininstru3Components = [InstructionsText2, key_resp_3]
for thisComponent in Maininstru3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Maininstru3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionsText2* updates
    if InstructionsText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsText2.frameNStart = frameN  # exact frame index
        InstructionsText2.tStart = t  # local t and not account for scr refresh
        InstructionsText2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsText2, 'tStartRefresh')  # time at next scr refresh
        InstructionsText2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['right','left'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Maininstru3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Maininstru3" ---
for thisComponent in Maininstru3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Maininstru3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MainInstru4_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
MainInstru4_2Components = [InstructionsText3, key_resp_7]
for thisComponent in MainInstru4_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MainInstru4_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionsText3* updates
    if InstructionsText3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsText3.frameNStart = frameN  # exact frame index
        InstructionsText3.tStart = t  # local t and not account for scr refresh
        InstructionsText3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsText3, 'tStartRefresh')  # time at next scr refresh
        InstructionsText3.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['left','right'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MainInstru4_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MainInstru4_2" ---
for thisComponent in MainInstru4_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "MainInstru4_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MainInstru5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
InstructionsText4.setText("Before you begin the main task, you will complete practice. This will provide feedback on how accurate you are.\n\nPlease press 'left' or 'right' to begin practice.")
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# Run 'Begin Routine' code from SkipChecker
if PracticeState == 'mainonly': 
    continueRoutine = False #end the routine 
# keep track of which components have finished
MainInstru5Components = [InstructionsText4, key_resp_2]
for thisComponent in MainInstru5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MainInstru5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionsText4* updates
    if InstructionsText4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsText4.frameNStart = frameN  # exact frame index
        InstructionsText4.tStart = t  # local t and not account for scr refresh
        InstructionsText4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsText4, 'tStartRefresh')  # time at next scr refresh
        InstructionsText4.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['right','left'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MainInstru5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MainInstru5" ---
for thisComponent in MainInstru5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "MainInstru5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practicetrials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(PracticeSelection),
    seed=None, name='practicetrials')
thisExp.addLoop(practicetrials)  # add the loop to the experiment
thisPracticetrial = practicetrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticetrial.rgb)
if thisPracticetrial != None:
    for paramName in thisPracticetrial:
        exec('{} = thisPracticetrial[paramName]'.format(paramName))

for thisPracticetrial in practicetrials:
    currentLoop = practicetrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticetrial.rgb)
    if thisPracticetrial != None:
        for paramName in thisPracticetrial:
            exec('{} = thisPracticetrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "InstructionsPractice" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from skip_practice
    if PracticeState == 'mainonly': 
        continueRoutine = False #end the routine 
        practicetrials.finished = True #break the loop
    PractIn1.setColor('white', colorSpace='rgb')
    PractIn1.setText(InstructionsP)
    PractIn1.setHeight(0.05)
    PractIn2.setColor('white', colorSpace='rgb')
    PractIn2.setPos((0, -0.35))
    PractIn2.setText("Please press 'left' or 'right' to begin.")
    PractIn2.setHeight(0.05)
    PractInstructionPass.keys = []
    PractInstructionPass.rt = []
    _PractInstructionPass_allKeys = []
    # Run 'Begin Routine' code from code_4
    PractIns = ("Practice Block: " + str(PractNo) + " of 4")
    PractBlock1.setColor('green', colorSpace='rgb')
    PractBlock1.setPos((0.00, 0.30))
    PractBlock1.setText(PractIns)
    PractBlock1.setHeight(0.05)
    # keep track of which components have finished
    InstructionsPracticeComponents = [PractIn1, PractIn2, PractInstructionPass, PractBlock1, LeftText2]
    for thisComponent in InstructionsPracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "InstructionsPractice" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PractIn1* updates
        if PractIn1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PractIn1.frameNStart = frameN  # exact frame index
            PractIn1.tStart = t  # local t and not account for scr refresh
            PractIn1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PractIn1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PractIn1.started')
            PractIn1.setAutoDraw(True)
        
        # *PractIn2* updates
        if PractIn2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            PractIn2.frameNStart = frameN  # exact frame index
            PractIn2.tStart = t  # local t and not account for scr refresh
            PractIn2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PractIn2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PractIn2.started')
            PractIn2.setAutoDraw(True)
        
        # *PractInstructionPass* updates
        waitOnFlip = False
        if PractInstructionPass.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            PractInstructionPass.frameNStart = frameN  # exact frame index
            PractInstructionPass.tStart = t  # local t and not account for scr refresh
            PractInstructionPass.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PractInstructionPass, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PractInstructionPass.started')
            PractInstructionPass.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(PractInstructionPass.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(PractInstructionPass.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if PractInstructionPass.status == STARTED and not waitOnFlip:
            theseKeys = PractInstructionPass.getKeys(keyList=['right','left'], waitRelease=False)
            _PractInstructionPass_allKeys.extend(theseKeys)
            if len(_PractInstructionPass_allKeys):
                PractInstructionPass.keys = _PractInstructionPass_allKeys[-1].name  # just the last key pressed
                PractInstructionPass.rt = _PractInstructionPass_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *PractBlock1* updates
        if PractBlock1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PractBlock1.frameNStart = frameN  # exact frame index
            PractBlock1.tStart = t  # local t and not account for scr refresh
            PractBlock1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PractBlock1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PractBlock1.started')
            PractBlock1.setAutoDraw(True)
        
        # *LeftText2* updates
        if LeftText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LeftText2.frameNStart = frameN  # exact frame index
            LeftText2.tStart = t  # local t and not account for scr refresh
            LeftText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LeftText2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'LeftText2.started')
            LeftText2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstructionsPractice" ---
    for thisComponent in InstructionsPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if PractInstructionPass.keys in ['', [], None]:  # No response was made
        PractInstructionPass.keys = None
    practicetrials.addData('PractInstructionPass.keys',PractInstructionPass.keys)
    if PractInstructionPass.keys != None:  # we had a response
        practicetrials.addData('PractInstructionPass.rt', PractInstructionPass.rt)
    # the Routine "InstructionsPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Brief_ISI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    Brief_ISIComponents = [Brief_ISI_P]
    for thisComponent in Brief_ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Brief_ISI" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Brief_ISI_P* updates
        if Brief_ISI_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Brief_ISI_P.frameNStart = frameN  # exact frame index
            Brief_ISI_P.tStart = t  # local t and not account for scr refresh
            Brief_ISI_P.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Brief_ISI_P, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Brief_ISI_P.started')
            Brief_ISI_P.setAutoDraw(True)
        if Brief_ISI_P.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Brief_ISI_P.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Brief_ISI_P.tStop = t  # not accounting for scr refresh
                Brief_ISI_P.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Brief_ISI_P.stopped')
                Brief_ISI_P.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Brief_ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Brief_ISI" ---
    for thisComponent in Brief_ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # set up handler to look after randomisation of conditions etc
    InnerLoopPractice = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(CondFileP),
        seed=None, name='InnerLoopPractice')
    thisExp.addLoop(InnerLoopPractice)  # add the loop to the experiment
    thisInnerLoopPractice = InnerLoopPractice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInnerLoopPractice.rgb)
    if thisInnerLoopPractice != None:
        for paramName in thisInnerLoopPractice:
            exec('{} = thisInnerLoopPractice[paramName]'.format(paramName))
    
    for thisInnerLoopPractice in InnerLoopPractice:
        currentLoop = InnerLoopPractice
        # abbreviate parameter names if possible (e.g. rgb = thisInnerLoopPractice.rgb)
        if thisInnerLoopPractice != None:
            for paramName in thisInnerLoopPractice:
                exec('{} = thisInnerLoopPractice[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "trial_practice_3" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        N_backP_2.setText(LettersDisplayedP)
        KeyPractice.keys = []
        KeyPractice.rt = []
        _KeyPractice_allKeys = []
        # Run 'Begin Routine' code from InstrSkipper
        if PracticeState == 'mainonly': 
            continueRoutine = False #end the routine 
            InnerLoopPractice.finished = True #break the loop2
        # keep track of which components have finished
        trial_practice_3Components = [N_backP_2, KeyPractice, ISI]
        for thisComponent in trial_practice_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial_practice_3" ---
        while continueRoutine and routineTimer.getTime() < 2.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *N_backP_2* updates
            if N_backP_2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                N_backP_2.frameNStart = frameN  # exact frame index
                N_backP_2.tStart = t  # local t and not account for scr refresh
                N_backP_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(N_backP_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'N_backP_2.started')
                N_backP_2.setAutoDraw(True)
            if N_backP_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > N_backP_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    N_backP_2.tStop = t  # not accounting for scr refresh
                    N_backP_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'N_backP_2.stopped')
                    N_backP_2.setAutoDraw(False)
            
            # *KeyPractice* updates
            waitOnFlip = False
            if KeyPractice.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                KeyPractice.frameNStart = frameN  # exact frame index
                KeyPractice.tStart = t  # local t and not account for scr refresh
                KeyPractice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KeyPractice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KeyPractice.started')
                KeyPractice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KeyPractice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KeyPractice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KeyPractice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > KeyPractice.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    KeyPractice.tStop = t  # not accounting for scr refresh
                    KeyPractice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'KeyPractice.stopped')
                    KeyPractice.status = FINISHED
            if KeyPractice.status == STARTED and not waitOnFlip:
                theseKeys = KeyPractice.getKeys(keyList=['right','left'], waitRelease=False)
                _KeyPractice_allKeys.extend(theseKeys)
                if len(_KeyPractice_allKeys):
                    KeyPractice.keys = _KeyPractice_allKeys[0].name  # just the first key pressed
                    KeyPractice.rt = _KeyPractice_allKeys[0].rt
                    # was this correct?
                    if (KeyPractice.keys == str(CorrectnessP)) or (KeyPractice.keys == CorrectnessP):
                        KeyPractice.corr = 1
                    else:
                        KeyPractice.corr = 0
            
            # *ISI* updates
            if ISI.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                # keep track of start time/frame for later
                ISI.frameNStart = frameN  # exact frame index
                ISI.tStart = t  # local t and not account for scr refresh
                ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ISI.started')
                ISI.setAutoDraw(True)
            if ISI.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ISI.tStartRefresh + 1.3-frameTolerance:
                    # keep track of stop time/frame for later
                    ISI.tStop = t  # not accounting for scr refresh
                    ISI.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI.stopped')
                    ISI.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_practice_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_practice_3" ---
        for thisComponent in trial_practice_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if KeyPractice.keys in ['', [], None]:  # No response was made
            KeyPractice.keys = None
            # was no response the correct answer?!
            if str(CorrectnessP).lower() == 'none':
               KeyPractice.corr = 1;  # correct non-response
            else:
               KeyPractice.corr = 0;  # failed to respond (incorrectly)
        # store data for InnerLoopPractice (TrialHandler)
        InnerLoopPractice.addData('KeyPractice.keys',KeyPractice.keys)
        InnerLoopPractice.addData('KeyPractice.corr', KeyPractice.corr)
        if KeyPractice.keys != None:  # we had a response
            InnerLoopPractice.addData('KeyPractice.rt', KeyPractice.rt)
        # Run 'End Routine' code from FeedbackRecord
        if KeyPractice.corr==1:
                PracticeFeedback = 'Correct'
                FeedbackColour = 'green'
        
        if KeyPractice.corr==0:
                PracticeFeedback = 'Incorrect'
                FeedbackColour = 'red'
        
        if KeyPractice.corr==0 and KeyPractice.keys== None:
                PracticeFeedback = 'Miss (too slow)'
                FeedbackColour = 'orange'
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.100000)
        
        # --- Prepare to start Routine "PracticeFeedbackRoutine" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        text_4.setColor(FeedbackColour, colorSpace='rgb')
        text_4.setText(PracticeFeedback)
        # Run 'Begin Routine' code from code_7
        if PracticeState == 'mainonly': 
            continueRoutine = False #end the routine 
            InnerLoopPractice.finished = True #break the loop2
        # keep track of which components have finished
        PracticeFeedbackRoutineComponents = [text_4]
        for thisComponent in PracticeFeedbackRoutineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PracticeFeedbackRoutine" ---
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.started')
                text_4.setAutoDraw(True)
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_4.stopped')
                    text_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeFeedbackRoutineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeFeedbackRoutine" ---
        for thisComponent in PracticeFeedbackRoutineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'InnerLoopPractice'
    
    
    # --- Prepare to start Routine "PractAdder" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from PractAddBlock
    PractNo = PractNo + 1
    # keep track of which components have finished
    PractAdderComponents = []
    for thisComponent in PractAdderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "PractAdder" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PractAdderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PractAdder" ---
    for thisComponent in PractAdderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "PractAdder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practicetrials'


# --- Prepare to start Routine "Transition" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_8
if PracticeState == 'mainonly': 
    continueRoutine = False #end the routine
TransitionText.setText("You have now completed the practice runs. Please take a break if required.\n\nKeep in mind you not receive visual feedback (correct/incorrect/miss) in the main task.\n\nPress 'right' or 'left' to continue")
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
TransitionComponents = [TransitionText, key_resp_6]
for thisComponent in TransitionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Transition" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TransitionText* updates
    if TransitionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TransitionText.frameNStart = frameN  # exact frame index
        TransitionText.tStart = t  # local t and not account for scr refresh
        TransitionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TransitionText, 'tStartRefresh')  # time at next scr refresh
        TransitionText.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['right','left'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TransitionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Transition" ---
for thisComponent in TransitionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "Transition" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Transition2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_10
if PracticeState == 'prctonly': 
    core.quit()

text_5.setText("You will begin the main task on the next screen.\n\nPlease press 'right' or 'left' to start the main task.")
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
Transition2Components = [text_5, key_resp_5]
for thisComponent in Transition2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Transition2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['right','left'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Transition2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Transition2" ---
for thisComponent in Transition2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "Transition2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(VersionSelection),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "InstructionsTrial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    MainInt1.setPos((0, 0))
    MainInt1.setText(Instructions)
    MainInt1.setHeight(0.05)
    MainInt2.setPos((0, -0.35))
    MainInt2.setText("Please press 'right' or 'left' to begin.")
    MainInt2.setHeight(0.05)
    InstructionPass.keys = []
    InstructionPass.rt = []
    _InstructionPass_allKeys = []
    # Run 'Begin Routine' code from TaskBlockNoSet
    MainIns = ('Task Block: '+ str(BlockNo) + ' of 16')
    Blocks1.setPos((0.00, 0.20))
    Blocks1.setText(MainIns)
    Blocks1.setHeight(0.05)
    # keep track of which components have finished
    InstructionsTrialComponents = [MainInt1, MainInt2, InstructionPass, Blocks1, LeftText]
    for thisComponent in InstructionsTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "InstructionsTrial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *MainInt1* updates
        if MainInt1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MainInt1.frameNStart = frameN  # exact frame index
            MainInt1.tStart = t  # local t and not account for scr refresh
            MainInt1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MainInt1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'MainInt1.started')
            MainInt1.setAutoDraw(True)
        
        # *MainInt2* updates
        if MainInt2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            MainInt2.frameNStart = frameN  # exact frame index
            MainInt2.tStart = t  # local t and not account for scr refresh
            MainInt2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MainInt2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'MainInt2.started')
            MainInt2.setAutoDraw(True)
        
        # *InstructionPass* updates
        waitOnFlip = False
        if InstructionPass.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionPass.frameNStart = frameN  # exact frame index
            InstructionPass.tStart = t  # local t and not account for scr refresh
            InstructionPass.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionPass, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionPass.started')
            InstructionPass.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(InstructionPass.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(InstructionPass.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if InstructionPass.status == STARTED and not waitOnFlip:
            theseKeys = InstructionPass.getKeys(keyList=['right','left'], waitRelease=False)
            _InstructionPass_allKeys.extend(theseKeys)
            if len(_InstructionPass_allKeys):
                InstructionPass.keys = _InstructionPass_allKeys[-1].name  # just the last key pressed
                InstructionPass.rt = _InstructionPass_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Blocks1* updates
        if Blocks1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blocks1.frameNStart = frameN  # exact frame index
            Blocks1.tStart = t  # local t and not account for scr refresh
            Blocks1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blocks1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Blocks1.started')
            Blocks1.setAutoDraw(True)
        
        # *LeftText* updates
        if LeftText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LeftText.frameNStart = frameN  # exact frame index
            LeftText.tStart = t  # local t and not account for scr refresh
            LeftText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LeftText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'LeftText.started')
            LeftText.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstructionsTrial" ---
    for thisComponent in InstructionsTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if InstructionPass.keys in ['', [], None]:  # No response was made
        InstructionPass.keys = None
    trials.addData('InstructionPass.keys',InstructionPass.keys)
    if InstructionPass.keys != None:  # we had a response
        trials.addData('InstructionPass.rt', InstructionPass.rt)
    # the Routine "InstructionsTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Brief_ISI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    Brief_ISIComponents = [Brief_ISI_P]
    for thisComponent in Brief_ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Brief_ISI" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Brief_ISI_P* updates
        if Brief_ISI_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Brief_ISI_P.frameNStart = frameN  # exact frame index
            Brief_ISI_P.tStart = t  # local t and not account for scr refresh
            Brief_ISI_P.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Brief_ISI_P, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Brief_ISI_P.started')
            Brief_ISI_P.setAutoDraw(True)
        if Brief_ISI_P.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Brief_ISI_P.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Brief_ISI_P.tStop = t  # not accounting for scr refresh
                Brief_ISI_P.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Brief_ISI_P.stopped')
                Brief_ISI_P.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Brief_ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Brief_ISI" ---
    for thisComponent in Brief_ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # set up handler to look after randomisation of conditions etc
    InnerLoop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(CondFile),
        seed=None, name='InnerLoop')
    thisExp.addLoop(InnerLoop)  # add the loop to the experiment
    thisInnerLoop = InnerLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInnerLoop.rgb)
    if thisInnerLoop != None:
        for paramName in thisInnerLoop:
            exec('{} = thisInnerLoop[paramName]'.format(paramName))
    
    for thisInnerLoop in InnerLoop:
        currentLoop = InnerLoop
        # abbreviate parameter names if possible (e.g. rgb = thisInnerLoop.rgb)
        if thisInnerLoop != None:
            for paramName in thisInnerLoop:
                exec('{} = thisInnerLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "trial_proper" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        N_backD.setText(LettersDisplayed)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        trial_properComponents = [N_backD, key_resp, Fixation]
        for thisComponent in trial_properComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial_proper" ---
        while continueRoutine and routineTimer.getTime() < 2.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *N_backD* updates
            if N_backD.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                N_backD.frameNStart = frameN  # exact frame index
                N_backD.tStart = t  # local t and not account for scr refresh
                N_backD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(N_backD, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'N_backD.started')
                N_backD.setAutoDraw(True)
            if N_backD.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > N_backD.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    N_backD.tStop = t  # not accounting for scr refresh
                    N_backD.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'N_backD.stopped')
                    N_backD.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['left','right'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                    key_resp.rt = _key_resp_allKeys[0].rt
                    # was this correct?
                    if (key_resp.keys == str(Correctness)) or (key_resp.keys == Correctness):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
            
            # *Fixation* updates
            if Fixation.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                # keep track of start time/frame for later
                Fixation.frameNStart = frameN  # exact frame index
                Fixation.tStart = t  # local t and not account for scr refresh
                Fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fixation.started')
                Fixation.setAutoDraw(True)
            if Fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation.tStartRefresh + 1.4-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation.tStop = t  # not accounting for scr refresh
                    Fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fixation.stopped')
                    Fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_properComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_proper" ---
        for thisComponent in trial_properComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(Correctness).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for InnerLoop (TrialHandler)
        InnerLoop.addData('key_resp.keys',key_resp.keys)
        InnerLoop.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            InnerLoop.addData('key_resp.rt', key_resp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.100000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'InnerLoop'
    
    
    # --- Prepare to start Routine "Adder" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Add
    BlockNo = BlockNo + 1
    # keep track of which components have finished
    AdderComponents = []
    for thisComponent in AdderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Adder" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AdderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Adder" ---
    for thisComponent in AdderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Adder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "EndOfExperiment" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
EndOfExperimentText.setText("You have now completed the experiment. Thank you.\n\nPlease inform the researcher.\n\nPress 'escape' to close this window.")
# keep track of which components have finished
EndOfExperimentComponents = [EndOfExperimentText]
for thisComponent in EndOfExperimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EndOfExperiment" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndOfExperimentText* updates
    if EndOfExperimentText.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        EndOfExperimentText.frameNStart = frameN  # exact frame index
        EndOfExperimentText.tStart = t  # local t and not account for scr refresh
        EndOfExperimentText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndOfExperimentText, 'tStartRefresh')  # time at next scr refresh
        EndOfExperimentText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndOfExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndOfExperiment" ---
for thisComponent in EndOfExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "EndOfExperiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
