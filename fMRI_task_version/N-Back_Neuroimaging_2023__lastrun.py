#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on March 03, 2023, at 16:18
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
expName = 'N-Back for Neuroimaging'  # from the Builder filename that created this script
expInfo = {
    'participant': 'P0',
    'Task Version (1 or 2)': '1',
    'Pre or post': 'NA',
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
    originPath='C:\\Users\\PERL Admin\\Desktop\\n_back\\n-back_fMRI_oxford-Psychopy_v1.4\\N-Back_Neuroimaging_2023__lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
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
# Run 'Begin Experiment' code from MouseSet
win.setMouseVisible(False)
# Run 'Begin Experiment' code from SetBlock
BlockNo = 1
PractNo = 1

# --- Initialize components for Routine "StartExpInst" ---
TaskVersionText = visual.TextStim(win=win, name='TaskVersionText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
InstrKey1 = keyboard.Keyboard()

# --- Initialize components for Routine "LeftButtonCheck" ---
CheckText1 = visual.TextStim(win=win, name='CheckText1',
    text="Press the 'left' button",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# --- Initialize components for Routine "RightButtonCheck" ---
CheckText2 = visual.TextStim(win=win, name='CheckText2',
    text="Press the 'right' button",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# --- Initialize components for Routine "LeftButtonCheck" ---
CheckText1 = visual.TextStim(win=win, name='CheckText1',
    text="Press the 'left' button",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# --- Initialize components for Routine "MainInstru1" ---
Instructions1 = visual.TextStim(win=win, name='Instructions1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "Maininstru2" ---
Instructions2 = visual.TextStim(win=win, name='Instructions2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "MainInstru333" ---
TextInstru = visual.TextStim(win=win, name='TextInstru',
    text="You have 2s to press a key, from when the letter appears. \n\nYou must press the key before the next letter appears. Only the first press will be counted.\n\nPress 'left' or 'right' to continue.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ContinueButton = keyboard.Keyboard()

# --- Initialize components for Routine "MainInstru2point5" ---
key_resp_7 = keyboard.Keyboard()
Instructions3 = visual.TextStim(win=win, name='Instructions3',
    text="Letters are uppercase (A,B,C) and lowercase (a,b,c).\n\nTreat uppercase and lowercase as the same (e.g., A = a).\n\nWhen you see a cross (+) it is a rest period.\n\nPress 'left' or 'right' to continue.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Transition2" ---
TransitionText2 = visual.TextStim(win=win, name='TransitionText2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "ScannerPrompt" ---
Scanner_wait_text = visual.TextStim(win=win, name='Scanner_wait_text',
    text='Waiting for the scanner...',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Scanner_control = keyboard.Keyboard()

# --- Initialize components for Routine "Initial_rest" ---
Initial_rest_Fixation = visual.TextStim(win=win, name='Initial_rest_Fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.7255, 0.7255, 0.7255], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PreInstrWarning = visual.TextStim(win=win, name='PreInstrWarning',
    text='!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "InstructionsTrial" ---
MainInt1 = visual.TextStim(win=win, name='MainInt1',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Blocks1 = visual.TextStim(win=win, name='Blocks1',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
LeftText = visual.TextStim(win=win, name='LeftText',
    text="Press 'left' when you see any other letter.",
    font='Open Sans',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "TransitionISI" ---
Transition_Fixation = visual.TextStim(win=win, name='Transition_Fixation',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=1.0, 
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

# --- Initialize components for Routine "TaskBlockEndTimer" ---

# --- Initialize components for Routine "Adder_and_Baseline" ---
FixationPoint = visual.TextStim(win=win, name='FixationPoint',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.7255, 0.7255, 0.7255], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
PreInstrWarning2 = visual.TextStim(win=win, name='PreInstrWarning2',
    text='!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "EndOfExperiment" ---
EndExperimentText = visual.TextStim(win=win, name='EndExperimentText',
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

# --- Prepare to start Routine "StartExpInst" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from TaskNoPrint
VersionT = ('This is the n-back task version '+''+ TaskVersion + ''
+'\n \n \n Please press the left or right key to continue.')
TaskVersionText.setText(VersionT)
InstrKey1.keys = []
InstrKey1.rt = []
_InstrKey1_allKeys = []
# keep track of which components have finished
StartExpInstComponents = [TaskVersionText, InstrKey1]
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
        theseKeys = InstrKey1.getKeys(keyList=['1','2'], waitRelease=False)
        _InstrKey1_allKeys.extend(theseKeys)
        if len(_InstrKey1_allKeys):
            InstrKey1.keys = _InstrKey1_allKeys[-1].name  # just the last key pressed
            InstrKey1.rt = _InstrKey1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # Run 'Each Frame' code from QuitChecker
    keys = event.getKeys()
    if 'q' in keys and 't' in keys:
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

# --- Prepare to start Routine "LeftButtonCheck" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
LeftButtonCheckComponents = [CheckText1, key_resp_8]
for thisComponent in LeftButtonCheckComponents:
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

# --- Run Routine "LeftButtonCheck" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CheckText1* updates
    if CheckText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        CheckText1.frameNStart = frameN  # exact frame index
        CheckText1.tStart = t  # local t and not account for scr refresh
        CheckText1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CheckText1, 'tStartRefresh')  # time at next scr refresh
        CheckText1.setAutoDraw(True)
    
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
        theseKeys = key_resp_8.getKeys(keyList=['1'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LeftButtonCheckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "LeftButtonCheck" ---
for thisComponent in LeftButtonCheckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "LeftButtonCheck" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "RightButtonCheck" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
RightButtonCheckComponents = [CheckText2, key_resp_9]
for thisComponent in RightButtonCheckComponents:
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

# --- Run Routine "RightButtonCheck" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CheckText2* updates
    if CheckText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        CheckText2.frameNStart = frameN  # exact frame index
        CheckText2.tStart = t  # local t and not account for scr refresh
        CheckText2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CheckText2, 'tStartRefresh')  # time at next scr refresh
        CheckText2.setAutoDraw(True)
    
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
        theseKeys = key_resp_9.getKeys(keyList=['2'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RightButtonCheckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "RightButtonCheck" ---
for thisComponent in RightButtonCheckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()
# the Routine "RightButtonCheck" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "LeftButtonCheck" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
LeftButtonCheckComponents = [CheckText1, key_resp_8]
for thisComponent in LeftButtonCheckComponents:
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

# --- Run Routine "LeftButtonCheck" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CheckText1* updates
    if CheckText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        CheckText1.frameNStart = frameN  # exact frame index
        CheckText1.tStart = t  # local t and not account for scr refresh
        CheckText1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CheckText1, 'tStartRefresh')  # time at next scr refresh
        CheckText1.setAutoDraw(True)
    
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
        theseKeys = key_resp_8.getKeys(keyList=['1'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LeftButtonCheckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "LeftButtonCheck" ---
for thisComponent in LeftButtonCheckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "LeftButtonCheck" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MainInstru1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Instructions1.setText("In this task, you will see a series of letters appear on the screen. Only one letter will appear at a time. \n\nYou need to press the 'right' or 'left' key based on rules which change over time.\n\nPress 'left' or 'right' to continue.")
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
MainInstru1Components = [Instructions1, key_resp_4]
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
    
    # *Instructions1* updates
    if Instructions1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions1.frameNStart = frameN  # exact frame index
        Instructions1.tStart = t  # local t and not account for scr refresh
        Instructions1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions1, 'tStartRefresh')  # time at next scr refresh
        Instructions1.setAutoDraw(True)
    
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
        theseKeys = key_resp_4.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # Run 'Each Frame' code from QuitChecker_2
    keys = event.getKeys()
    if 'q' in keys and 't' in keys:
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

# --- Prepare to start Routine "Maininstru2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Instructions2.setText("Press the 'right' key based on the rule (e.g letters appearing twice in a row). \nFor other letters, press the 'left' key.\n\nPress 'left' or 'right' to continue.")
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Maininstru2Components = [Instructions2, key_resp_3]
for thisComponent in Maininstru2Components:
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

# --- Run Routine "Maininstru2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions2* updates
    if Instructions2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions2.frameNStart = frameN  # exact frame index
        Instructions2.tStart = t  # local t and not account for scr refresh
        Instructions2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions2, 'tStartRefresh')  # time at next scr refresh
        Instructions2.setAutoDraw(True)
    
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
        theseKeys = key_resp_3.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Maininstru2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Maininstru2" ---
for thisComponent in Maininstru2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Maininstru2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MainInstru333" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ContinueButton.keys = []
ContinueButton.rt = []
_ContinueButton_allKeys = []
# keep track of which components have finished
MainInstru333Components = [TextInstru, ContinueButton]
for thisComponent in MainInstru333Components:
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

# --- Run Routine "MainInstru333" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextInstru* updates
    if TextInstru.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TextInstru.frameNStart = frameN  # exact frame index
        TextInstru.tStart = t  # local t and not account for scr refresh
        TextInstru.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TextInstru, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TextInstru.started')
        TextInstru.setAutoDraw(True)
    
    # *ContinueButton* updates
    waitOnFlip = False
    if ContinueButton.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        ContinueButton.frameNStart = frameN  # exact frame index
        ContinueButton.tStart = t  # local t and not account for scr refresh
        ContinueButton.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueButton, 'tStartRefresh')  # time at next scr refresh
        ContinueButton.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ContinueButton.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ContinueButton.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ContinueButton.status == STARTED and not waitOnFlip:
        theseKeys = ContinueButton.getKeys(keyList=['left','right'], waitRelease=False)
        _ContinueButton_allKeys.extend(theseKeys)
        if len(_ContinueButton_allKeys):
            ContinueButton.keys = _ContinueButton_allKeys[-1].name  # just the last key pressed
            ContinueButton.rt = _ContinueButton_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MainInstru333Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MainInstru333" ---
for thisComponent in MainInstru333Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ContinueButton.keys in ['', [], None]:  # No response was made
    ContinueButton.keys = None
thisExp.addData('ContinueButton.keys',ContinueButton.keys)
if ContinueButton.keys != None:  # we had a response
    thisExp.addData('ContinueButton.rt', ContinueButton.rt)
thisExp.nextEntry()
# the Routine "MainInstru333" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MainInstru2point5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
MainInstru2point5Components = [key_resp_7, Instructions3]
for thisComponent in MainInstru2point5Components:
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

# --- Run Routine "MainInstru2point5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
        theseKeys = key_resp_7.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Instructions3* updates
    if Instructions3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions3.frameNStart = frameN  # exact frame index
        Instructions3.tStart = t  # local t and not account for scr refresh
        Instructions3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions3, 'tStartRefresh')  # time at next scr refresh
        Instructions3.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MainInstru2point5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MainInstru2point5" ---
for thisComponent in MainInstru2point5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "MainInstru2point5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Transition2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
TransitionText2.setText("You will begin the main task on the next screen.\n\nPress 'right' or 'left' to start the main task.")
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
Transition2Components = [TransitionText2, key_resp_5]
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
    
    # *TransitionText2* updates
    if TransitionText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TransitionText2.frameNStart = frameN  # exact frame index
        TransitionText2.tStart = t  # local t and not account for scr refresh
        TransitionText2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TransitionText2, 'tStartRefresh')  # time at next scr refresh
        TransitionText2.setAutoDraw(True)
    
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
        theseKeys = key_resp_5.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
Prompt_Looper = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Prompt_Looper')
thisExp.addLoop(Prompt_Looper)  # add the loop to the experiment
thisPrompt_Looper = Prompt_Looper.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrompt_Looper.rgb)
if thisPrompt_Looper != None:
    for paramName in thisPrompt_Looper:
        exec('{} = thisPrompt_Looper[paramName]'.format(paramName))

for thisPrompt_Looper in Prompt_Looper:
    currentLoop = Prompt_Looper
    # abbreviate parameter names if possible (e.g. rgb = thisPrompt_Looper.rgb)
    if thisPrompt_Looper != None:
        for paramName in thisPrompt_Looper:
            exec('{} = thisPrompt_Looper[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ScannerPrompt" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Scanner_control.keys = []
    Scanner_control.rt = []
    _Scanner_control_allKeys = []
    # Run 'Begin Routine' code from Scan_Timer_1
    time_ScannerPromptBegin = globalClock.getTime()
    # keep track of which components have finished
    ScannerPromptComponents = [Scanner_wait_text, Scanner_control]
    for thisComponent in ScannerPromptComponents:
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
    
    # --- Run Routine "ScannerPrompt" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Scanner_wait_text* updates
        if Scanner_wait_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Scanner_wait_text.frameNStart = frameN  # exact frame index
            Scanner_wait_text.tStart = t  # local t and not account for scr refresh
            Scanner_wait_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Scanner_wait_text, 'tStartRefresh')  # time at next scr refresh
            Scanner_wait_text.setAutoDraw(True)
        
        # *Scanner_control* updates
        waitOnFlip = False
        if Scanner_control.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Scanner_control.frameNStart = frameN  # exact frame index
            Scanner_control.tStart = t  # local t and not account for scr refresh
            Scanner_control.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Scanner_control, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Scanner_control.started')
            Scanner_control.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Scanner_control.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Scanner_control.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Scanner_control.status == STARTED and not waitOnFlip:
            theseKeys = Scanner_control.getKeys(keyList=['5'], waitRelease=False)
            _Scanner_control_allKeys.extend(theseKeys)
            if len(_Scanner_control_allKeys):
                Scanner_control.keys = _Scanner_control_allKeys[-1].name  # just the last key pressed
                Scanner_control.rt = _Scanner_control_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ScannerPromptComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ScannerPrompt" ---
    for thisComponent in ScannerPromptComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Scanner_control.keys in ['', [], None]:  # No response was made
        Scanner_control.keys = None
    Prompt_Looper.addData('Scanner_control.keys',Scanner_control.keys)
    if Scanner_control.keys != None:  # we had a response
        Prompt_Looper.addData('Scanner_control.rt', Scanner_control.rt)
    # Run 'End Routine' code from Scan_Timer_1
    time_ScannerPromptEnd = globalClock.getTime()
    
    thisExp.addData('time_ScannerPromptBegin', time_ScannerPromptBegin)
    thisExp.addData('time_ScannerPromptEnd', time_ScannerPromptEnd)
    # the Routine "ScannerPrompt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 5.0 repeats of 'Prompt_Looper'


# --- Prepare to start Routine "Initial_rest" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from Initial_rest_timer
time_InitialRestBegin = globalClock.getTime()
# keep track of which components have finished
Initial_restComponents = [Initial_rest_Fixation, PreInstrWarning]
for thisComponent in Initial_restComponents:
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

# --- Run Routine "Initial_rest" ---
while continueRoutine and routineTimer.getTime() < 20.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Initial_rest_Fixation* updates
    if Initial_rest_Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Initial_rest_Fixation.frameNStart = frameN  # exact frame index
        Initial_rest_Fixation.tStart = t  # local t and not account for scr refresh
        Initial_rest_Fixation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Initial_rest_Fixation, 'tStartRefresh')  # time at next scr refresh
        Initial_rest_Fixation.setAutoDraw(True)
    if Initial_rest_Fixation.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Initial_rest_Fixation.tStartRefresh + 19-frameTolerance:
            # keep track of stop time/frame for later
            Initial_rest_Fixation.tStop = t  # not accounting for scr refresh
            Initial_rest_Fixation.frameNStop = frameN  # exact frame index
            Initial_rest_Fixation.setAutoDraw(False)
    
    # *PreInstrWarning* updates
    if PreInstrWarning.status == NOT_STARTED and tThisFlip >= 19-frameTolerance:
        # keep track of start time/frame for later
        PreInstrWarning.frameNStart = frameN  # exact frame index
        PreInstrWarning.tStart = t  # local t and not account for scr refresh
        PreInstrWarning.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PreInstrWarning, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'PreInstrWarning.started')
        PreInstrWarning.setAutoDraw(True)
    if PreInstrWarning.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > PreInstrWarning.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            PreInstrWarning.tStop = t  # not accounting for scr refresh
            PreInstrWarning.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreInstrWarning.stopped')
            PreInstrWarning.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Initial_restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Initial_rest" ---
for thisComponent in Initial_restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from Initial_rest_timer
time_InitialRestEnd = globalClock.getTime()

thisExp.addData('time_InitialRestBegin', time_InitialRestBegin)
thisExp.addData('time_InitialRestEnd', time_InitialRestEnd)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-20.000000)

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
    MainInt1.setPos((0, -0.0))
    MainInt1.setText(Instructions)
    MainInt1.setHeight(0.05)
    # Run 'Begin Routine' code from BlockCounter
    MainIns = ('Block: '+ str(BlockNo) + ' / 16')
    Blocks1.setPos((0.00, 0.20))
    Blocks1.setText(MainIns)
    Blocks1.setHeight(0.05)
    # Run 'Begin Routine' code from Timer_Instructions
    time_InstructionsBegin = globalClock.getTime()
    # keep track of which components have finished
    InstructionsTrialComponents = [MainInt1, Blocks1, LeftText]
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
    while continueRoutine and routineTimer.getTime() < 9.0:
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
            MainInt1.setAutoDraw(True)
        if MainInt1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MainInt1.tStartRefresh + 9.0-frameTolerance:
                # keep track of stop time/frame for later
                MainInt1.tStop = t  # not accounting for scr refresh
                MainInt1.frameNStop = frameN  # exact frame index
                MainInt1.setAutoDraw(False)
        
        # *Blocks1* updates
        if Blocks1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blocks1.frameNStart = frameN  # exact frame index
            Blocks1.tStart = t  # local t and not account for scr refresh
            Blocks1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blocks1, 'tStartRefresh')  # time at next scr refresh
            Blocks1.setAutoDraw(True)
        if Blocks1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blocks1.tStartRefresh + 9.0-frameTolerance:
                # keep track of stop time/frame for later
                Blocks1.tStop = t  # not accounting for scr refresh
                Blocks1.frameNStop = frameN  # exact frame index
                Blocks1.setAutoDraw(False)
        
        # *LeftText* updates
        if LeftText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LeftText.frameNStart = frameN  # exact frame index
            LeftText.tStart = t  # local t and not account for scr refresh
            LeftText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LeftText, 'tStartRefresh')  # time at next scr refresh
            LeftText.setAutoDraw(True)
        if LeftText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > LeftText.tStartRefresh + 9.0-frameTolerance:
                # keep track of stop time/frame for later
                LeftText.tStop = t  # not accounting for scr refresh
                LeftText.frameNStop = frameN  # exact frame index
                LeftText.setAutoDraw(False)
        
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
    # Run 'End Routine' code from Timer_Instructions
    time_InstructionsEnd = globalClock.getTime()
    
    thisExp.addData('time_InstructionsBegin', time_InstructionsBegin)
    thisExp.addData('time_InstructionsEnd', time_InstructionsEnd)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-9.000000)
    
    # --- Prepare to start Routine "TransitionISI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Transition_Fixation.setPos((0, 0))
    Transition_Fixation.setOri(0.0)
    Transition_Fixation.setText('·')
    Transition_Fixation.setFlip('None')
    # Run 'Begin Routine' code from TransitionTimer
    time_TransitionBegin = globalClock.getTime()
    # keep track of which components have finished
    TransitionISIComponents = [Transition_Fixation]
    for thisComponent in TransitionISIComponents:
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
    
    # --- Run Routine "TransitionISI" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Transition_Fixation* updates
        if Transition_Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Transition_Fixation.frameNStart = frameN  # exact frame index
            Transition_Fixation.tStart = t  # local t and not account for scr refresh
            Transition_Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Transition_Fixation, 'tStartRefresh')  # time at next scr refresh
            Transition_Fixation.setAutoDraw(True)
        if Transition_Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Transition_Fixation.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Transition_Fixation.tStop = t  # not accounting for scr refresh
                Transition_Fixation.frameNStop = frameN  # exact frame index
                Transition_Fixation.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TransitionISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TransitionISI" ---
    for thisComponent in TransitionISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from TransitionTimer
    time_TaskStartTimer = globalClock.getTime()
    
    thisExp.addData('time_TransitionBegin', time_TransitionBegin)
    thisExp.addData('time_TaskStartTimer', time_TaskStartTimer)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
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
        # Run 'Begin Routine' code from Trial_Timer
        time_trialBegin = globalClock.getTime()
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
                theseKeys = key_resp.getKeys(keyList=['1','2'], waitRelease=False)
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
        # Run 'End Routine' code from Trial_Timer
        time_trialEnd = globalClock.getTime()
        
        thisExp.addData('time_trialBegin', time_trialBegin)
        thisExp.addData('time_trialEnd', time_trialEnd)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.100000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'InnerLoop'
    
    
    # --- Prepare to start Routine "TaskBlockEndTimer" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    TaskBlockEndTimerComponents = []
    for thisComponent in TaskBlockEndTimerComponents:
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
    
    # --- Run Routine "TaskBlockEndTimer" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TaskBlockEndTimerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TaskBlockEndTimer" ---
    for thisComponent in TaskBlockEndTimerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from TaskBlockEndTimer_2
    time_TaskBlockEnd = globalClock.getTime()
    
    thisExp.addData('time_TaskBlockEnd', time_TaskBlockEnd)
    # the Routine "TaskBlockEndTimer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Adder_and_Baseline" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Add
    BlockNo = BlockNo + 1
    # Run 'Begin Routine' code from EndBlockTimer
    time_RestBlockBegin = globalClock.getTime()
    # keep track of which components have finished
    Adder_and_BaselineComponents = [FixationPoint, PreInstrWarning2]
    for thisComponent in Adder_and_BaselineComponents:
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
    
    # --- Run Routine "Adder_and_Baseline" ---
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixationPoint* updates
        if FixationPoint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixationPoint.frameNStart = frameN  # exact frame index
            FixationPoint.tStart = t  # local t and not account for scr refresh
            FixationPoint.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixationPoint, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FixationPoint.started')
            FixationPoint.setAutoDraw(True)
        if FixationPoint.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixationPoint.tStartRefresh + 19-frameTolerance:
                # keep track of stop time/frame for later
                FixationPoint.tStop = t  # not accounting for scr refresh
                FixationPoint.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FixationPoint.stopped')
                FixationPoint.setAutoDraw(False)
        
        # *PreInstrWarning2* updates
        if PreInstrWarning2.status == NOT_STARTED and tThisFlip >= 19-frameTolerance:
            # keep track of start time/frame for later
            PreInstrWarning2.frameNStart = frameN  # exact frame index
            PreInstrWarning2.tStart = t  # local t and not account for scr refresh
            PreInstrWarning2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreInstrWarning2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreInstrWarning2.started')
            PreInstrWarning2.setAutoDraw(True)
        if PreInstrWarning2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > PreInstrWarning2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                PreInstrWarning2.tStop = t  # not accounting for scr refresh
                PreInstrWarning2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PreInstrWarning2.stopped')
                PreInstrWarning2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Adder_and_BaselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Adder_and_Baseline" ---
    for thisComponent in Adder_and_BaselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from EndBlockTimer
    time_RestBlockEnd = globalClock.getTime()
    
    thisExp.addData('time_RestBlockBegin', time_RestBlockBegin)
    thisExp.addData('time_RestBlockEnd', time_RestBlockEnd)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-20.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "EndOfExperiment" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
EndExperimentText.setText('You have now completed the experiment. Thank you.')
# Run 'Begin Routine' code from End_Experiment_Timer
time_ExperimentEnd = globalClock.getTime()
thisExp.addData('time_ExperimentEnd', time_ExperimentEnd)
# keep track of which components have finished
EndOfExperimentComponents = [EndExperimentText]
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
while continueRoutine and routineTimer.getTime() < 4.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndExperimentText* updates
    if EndExperimentText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndExperimentText.frameNStart = frameN  # exact frame index
        EndExperimentText.tStart = t  # local t and not account for scr refresh
        EndExperimentText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndExperimentText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EndExperimentText.started')
        EndExperimentText.setAutoDraw(True)
    if EndExperimentText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EndExperimentText.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            EndExperimentText.tStop = t  # not accounting for scr refresh
            EndExperimentText.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EndExperimentText.stopped')
            EndExperimentText.setAutoDraw(False)
    
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
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-4.000000)

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
