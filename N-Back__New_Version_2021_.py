#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 21, 2022, at 17:56
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'N-Back (New Version 2021)'  # from the Builder filename that created this script
expInfo = {'participant': 'P', 'Study Name': '', 'Task Version (required to run)': '1 or 2', 'PRE/POST': 'Pre or Post'}
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
    originPath='C:\\Users\\micha\\Desktop\\nback_2021_psychopy_version-main\\N-Back__New_Version_2021_.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Start_Code"
Start_CodeClock = core.Clock()
TaskVersion = expInfo['Task Version (required to run)'] 

TaskVersion = TaskVersion.replace(' ', '')

if TaskVersion == '1':
        VersionSelection = 'Conditions/NbackMaster_v1.xlsx'
        PracticeSelection = 'Conditions/NbackMasterPract_v1.xlsx'
        
if TaskVersion == '2':
        VersionSelection = 'Conditions/NbackMaster_v2.xlsx'
        PracticeSelection = 'Conditions/NbackMasterPract_v2.xlsx'
win.setMouseVisible(False)
BlockNo = 1
PractNo = 1

# Initialize components for Routine "StartExpInst"
StartExpInstClock = core.Clock()
TaskVersionText = visual.TextStim(win=win, name='TaskVersionText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
InstrKey1 = keyboard.Keyboard()

# Initialize components for Routine "MainInstru1"
MainInstru1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "Maininstru2"
Maininstru2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "MainInstru3"
MainInstru3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "InstructionsPractice"
InstructionsPracticeClock = core.Clock()
PractIn1 = visual.TextStim(win=win, name='PractIn1',
    text='',
    font='Open Sans',
    pos=(0, -0.10), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PractIn2 = visual.TextStim(win=win, name='PractIn2',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
PractInstructionPass = keyboard.Keyboard()
PractBlock1 = visual.TextStim(win=win, name='PractBlock1',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Practice_ISI"
Practice_ISIClock = core.Clock()
ISI_Pract_Fixation = visual.TextStim(win=win, name='ISI_Pract_Fixation',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial_practice"
trial_practiceClock = core.Clock()
N_backP = visual.TextStim(win=win, name='N_backP',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KeyPractice = keyboard.Keyboard()

# Initialize components for Routine "PracticeFeedbackRoutine"
PracticeFeedbackRoutineClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PractAdder"
PractAdderClock = core.Clock()

# Initialize components for Routine "Transition"
TransitionClock = core.Clock()
TransitionText = visual.TextStim(win=win, name='TransitionText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "Transition2"
Transition2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "InstructionsTrial"
InstructionsTrialClock = core.Clock()
MainInt1 = visual.TextStim(win=win, name='MainInt1',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
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

# Initialize components for Routine "Trial_ISI"
Trial_ISIClock = core.Clock()
ISI_Main = visual.TextStim(win=win, name='ISI_Main',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=1.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial_proper"
trial_properClock = core.Clock()
N_backD = visual.TextStim(win=win, name='N_backD',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Adder"
AdderClock = core.Clock()

# Initialize components for Routine "EndOfExperiment"
EndOfExperimentClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Start_Code"-------
continueRoutine = True
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
Start_CodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start_Code"-------
while continueRoutine:
    # get current time
    t = Start_CodeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Start_CodeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_CodeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_Code"-------
for thisComponent in Start_CodeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Start_Code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "StartExpInst"-------
continueRoutine = True
# update component parameters for each repeat
VersionT = ('This is the n-back task version '+'"'+ TaskVersion + '"'
+'\n \n \n Please press spacebar to continue to the instructions.')
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
StartExpInstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartExpInst"-------
while continueRoutine:
    # get current time
    t = StartExpInstClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartExpInstClock)
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
        theseKeys = InstrKey1.getKeys(keyList=['space'], waitRelease=False)
        _InstrKey1_allKeys.extend(theseKeys)
        if len(_InstrKey1_allKeys):
            InstrKey1.keys = _InstrKey1_allKeys[-1].name  # just the last key pressed
            InstrKey1.rt = _InstrKey1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartExpInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartExpInst"-------
for thisComponent in StartExpInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('TaskVersionText.started', TaskVersionText.tStartRefresh)
thisExp.addData('TaskVersionText.stopped', TaskVersionText.tStopRefresh)
# check responses
if InstrKey1.keys in ['', [], None]:  # No response was made
    InstrKey1.keys = None
thisExp.addData('InstrKey1.keys',InstrKey1.keys)
if InstrKey1.keys != None:  # we had a response
    thisExp.addData('InstrKey1.rt', InstrKey1.rt)
thisExp.addData('InstrKey1.started', InstrKey1.tStartRefresh)
thisExp.addData('InstrKey1.stopped', InstrKey1.tStopRefresh)
thisExp.nextEntry()
# the Routine "StartExpInst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "MainInstru1"-------
continueRoutine = True
# update component parameters for each repeat
text.setText("During the n-back, you will see a series of letters appear on the screen. Only one letter will appear on screen at one time. \n\nYou will need to press 'spacebar' on your keyboard according to rules you are given about the letters. \n\nPlease press spacebar to continue.")
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
MainInstru1Components = [text, key_resp_4]
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
MainInstru1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "MainInstru1"-------
while continueRoutine:
    # get current time
    t = MainInstru1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=MainInstru1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
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
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MainInstru1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MainInstru1"-------
for thisComponent in MainInstru1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "MainInstru1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Maininstru2"-------
continueRoutine = True
# update component parameters for each repeat
text_2.setText('The rules are different each time. For example, one rule will be to press the spacebar when you see a letter appear twice in a row. Please press spacebar as quickly and accurately as possible. \n\nDuring the task, letters are both uppercase and lowercase (e.g. E and e). Both uppercase and lowercase letters are treated as the same (i.e. E = e).\n\nPlease press spacebar to continue.')
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Maininstru2Components = [text_2, key_resp_3]
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
Maininstru2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Maininstru2"-------
while continueRoutine:
    # get current time
    t = Maininstru2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Maininstru2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
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
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Maininstru2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Maininstru2"-------
for thisComponent in Maininstru2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Maininstru2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "MainInstru3"-------
continueRoutine = True
# update component parameters for each repeat
text_3.setText('You will be alerted whenever a new rule is given during a break screen. When these rules appear, you may take a short break if needed. \n\nBefore you begin the task, you will take part in some practice runs. These will give you feedback on whether responses are correct or incorrect.\n\nPlease press spacebar to begin practice.')
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
MainInstru3Components = [text_3, key_resp_2]
for thisComponent in MainInstru3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
MainInstru3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "MainInstru3"-------
while continueRoutine:
    # get current time
    t = MainInstru3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=MainInstru3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
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
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MainInstru3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MainInstru3"-------
for thisComponent in MainInstru3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "MainInstru3" was not non-slip safe, so reset the non-slip timer
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
    
    # ------Prepare to start Routine "InstructionsPractice"-------
    continueRoutine = True
    # update component parameters for each repeat
    PractIn1.setColor('red', colorSpace='rgb')
    PractIn1.setText(InstructionsP)
    PractIn1.setHeight(0.05)
    PractIn2.setColor('white', colorSpace='rgb')
    PractIn2.setPos((0, -0.25))
    PractIn2.setText("Please press 'spacebar' to begin.")
    PractIn2.setHeight(0.05)
    PractInstructionPass.keys = []
    PractInstructionPass.rt = []
    _PractInstructionPass_allKeys = []
    PractIns = ("Practice Block: " + str(PractNo) + " of 4")
    PractBlock1.setColor('green', colorSpace='rgb')
    PractBlock1.setPos((0.00, 0.20))
    PractBlock1.setText(PractIns)
    PractBlock1.setHeight(0.05)
    # keep track of which components have finished
    InstructionsPracticeComponents = [PractIn1, PractIn2, PractInstructionPass, PractBlock1]
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
    InstructionsPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "InstructionsPractice"-------
    while continueRoutine:
        # get current time
        t = InstructionsPracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionsPracticeClock)
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
            PractIn1.setAutoDraw(True)
        
        # *PractIn2* updates
        if PractIn2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            PractIn2.frameNStart = frameN  # exact frame index
            PractIn2.tStart = t  # local t and not account for scr refresh
            PractIn2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PractIn2, 'tStartRefresh')  # time at next scr refresh
            PractIn2.setAutoDraw(True)
        
        # *PractInstructionPass* updates
        waitOnFlip = False
        if PractInstructionPass.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            PractInstructionPass.frameNStart = frameN  # exact frame index
            PractInstructionPass.tStart = t  # local t and not account for scr refresh
            PractInstructionPass.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PractInstructionPass, 'tStartRefresh')  # time at next scr refresh
            PractInstructionPass.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(PractInstructionPass.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(PractInstructionPass.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if PractInstructionPass.status == STARTED and not waitOnFlip:
            theseKeys = PractInstructionPass.getKeys(keyList=['space'], waitRelease=False)
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
            PractBlock1.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "InstructionsPractice"-------
    for thisComponent in InstructionsPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practicetrials.addData('PractIn1.started', PractIn1.tStartRefresh)
    practicetrials.addData('PractIn1.stopped', PractIn1.tStopRefresh)
    practicetrials.addData('PractIn2.started', PractIn2.tStartRefresh)
    practicetrials.addData('PractIn2.stopped', PractIn2.tStopRefresh)
    # check responses
    if PractInstructionPass.keys in ['', [], None]:  # No response was made
        PractInstructionPass.keys = None
    practicetrials.addData('PractInstructionPass.keys',PractInstructionPass.keys)
    if PractInstructionPass.keys != None:  # we had a response
        practicetrials.addData('PractInstructionPass.rt', PractInstructionPass.rt)
    practicetrials.addData('PractInstructionPass.started', PractInstructionPass.tStartRefresh)
    practicetrials.addData('PractInstructionPass.stopped', PractInstructionPass.tStopRefresh)
    practicetrials.addData('PractBlock1.started', PractBlock1.tStartRefresh)
    practicetrials.addData('PractBlock1.stopped', PractBlock1.tStopRefresh)
    # the Routine "InstructionsPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
        
        # ------Prepare to start Routine "Practice_ISI"-------
        continueRoutine = True
        # update component parameters for each repeat
        if InnerLoopPractice.thisN == 0: # only on the first trial
            jitters = [1.04, 1.065, 1.09, 1.115, 1.14, 1.165, 1.19,
        1.215, 1.24, 1.265, 1.29, 1.315, 1.34, 1.365, 1.39, 1.415,
        1.44, 1.465, 1.49, 1.515, 1.54, 1.565, 1.59, 1.615, 1.64,
        1.665, 1.69, 1.715, 1.74, 1.765, 1.79, 1.815, 1.84, 1.865,
        1.89, 1.915, 1.94, 1.965, 1.99, 2.015] # create the list
            shuffle(jitters) # randomise its order
        
        current_jitter = jitters.pop() # extract one entry on each trial
        thisExp.addData('ISIjitterPractice', current_jitter) # record in the data for this trial
        
        
        ISI_Pract_Fixation.setText('+')
        # keep track of which components have finished
        Practice_ISIComponents = [ISI_Pract_Fixation]
        for thisComponent in Practice_ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Practice_ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Practice_ISI"-------
        while continueRoutine:
            # get current time
            t = Practice_ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Practice_ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ISI_Pract_Fixation* updates
            if ISI_Pract_Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ISI_Pract_Fixation.frameNStart = frameN  # exact frame index
                ISI_Pract_Fixation.tStart = t  # local t and not account for scr refresh
                ISI_Pract_Fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI_Pract_Fixation, 'tStartRefresh')  # time at next scr refresh
                ISI_Pract_Fixation.setAutoDraw(True)
            if ISI_Pract_Fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ISI_Pract_Fixation.tStartRefresh + current_jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    ISI_Pract_Fixation.tStop = t  # not accounting for scr refresh
                    ISI_Pract_Fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ISI_Pract_Fixation, 'tStopRefresh')  # time at next scr refresh
                    ISI_Pract_Fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Practice_ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Practice_ISI"-------
        for thisComponent in Practice_ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        InnerLoopPractice.addData('ISI_Pract_Fixation.started', ISI_Pract_Fixation.tStartRefresh)
        InnerLoopPractice.addData('ISI_Pract_Fixation.stopped', ISI_Pract_Fixation.tStopRefresh)
        # the Routine "Practice_ISI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial_practice"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        N_backP.setText(LettersDisplayedP)
        KeyPractice.keys = []
        KeyPractice.rt = []
        _KeyPractice_allKeys = []
        # keep track of which components have finished
        trial_practiceComponents = [N_backP, KeyPractice]
        for thisComponent in trial_practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_practice"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_practiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_practiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *N_backP* updates
            if N_backP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                N_backP.frameNStart = frameN  # exact frame index
                N_backP.tStart = t  # local t and not account for scr refresh
                N_backP.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(N_backP, 'tStartRefresh')  # time at next scr refresh
                N_backP.setAutoDraw(True)
            if N_backP.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > N_backP.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    N_backP.tStop = t  # not accounting for scr refresh
                    N_backP.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(N_backP, 'tStopRefresh')  # time at next scr refresh
                    N_backP.setAutoDraw(False)
            
            # *KeyPractice* updates
            waitOnFlip = False
            if KeyPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                KeyPractice.frameNStart = frameN  # exact frame index
                KeyPractice.tStart = t  # local t and not account for scr refresh
                KeyPractice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KeyPractice, 'tStartRefresh')  # time at next scr refresh
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
                    win.timeOnFlip(KeyPractice, 'tStopRefresh')  # time at next scr refresh
                    KeyPractice.status = FINISHED
            if KeyPractice.status == STARTED and not waitOnFlip:
                theseKeys = KeyPractice.getKeys(keyList=['space'], waitRelease=False)
                _KeyPractice_allKeys.extend(theseKeys)
                if len(_KeyPractice_allKeys):
                    KeyPractice.keys = _KeyPractice_allKeys[-1].name  # just the last key pressed
                    KeyPractice.rt = _KeyPractice_allKeys[-1].rt
                    # was this correct?
                    if (KeyPractice.keys == str(CorrectnessP)) or (KeyPractice.keys == CorrectnessP):
                        KeyPractice.corr = 1
                    else:
                        KeyPractice.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_practice"-------
        for thisComponent in trial_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        InnerLoopPractice.addData('N_backP.started', N_backP.tStartRefresh)
        InnerLoopPractice.addData('N_backP.stopped', N_backP.tStopRefresh)
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
        InnerLoopPractice.addData('KeyPractice.started', KeyPractice.tStartRefresh)
        InnerLoopPractice.addData('KeyPractice.stopped', KeyPractice.tStopRefresh)
        if KeyPractice.corr==1:
                PracticeFeedback = 'Correct'
                FeedbackColour = 'green'
        
        if KeyPractice.corr==0:
                PracticeFeedback = 'Incorrect'
                FeedbackColour = 'red'
        
        if KeyPractice.corr==0 and KeyPractice.keys== None:
                PracticeFeedback = 'Miss (too slow)'
                FeedbackColour = 'orange'
        
        # ------Prepare to start Routine "PracticeFeedbackRoutine"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        text_4.setColor(FeedbackColour, colorSpace='rgb')
        text_4.setText(PracticeFeedback)
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
        PracticeFeedbackRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "PracticeFeedbackRoutine"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = PracticeFeedbackRoutineClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeFeedbackRoutineClock)
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
                text_4.setAutoDraw(True)
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeFeedbackRoutineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeFeedbackRoutine"-------
        for thisComponent in PracticeFeedbackRoutineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        InnerLoopPractice.addData('text_4.started', text_4.tStartRefresh)
        InnerLoopPractice.addData('text_4.stopped', text_4.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'InnerLoopPractice'
    
    
    # ------Prepare to start Routine "PractAdder"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    PractAdderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PractAdder"-------
    while continueRoutine:
        # get current time
        t = PractAdderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PractAdderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PractAdderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PractAdder"-------
    for thisComponent in PractAdderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "PractAdder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practicetrials'


# ------Prepare to start Routine "Transition"-------
continueRoutine = True
# update component parameters for each repeat
TransitionText.setText('You have now completed the practice runs. Please take a break if required.\n\nPress spacebar to continue')
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
TransitionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Transition"-------
while continueRoutine:
    # get current time
    t = TransitionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TransitionClock)
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
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TransitionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Transition"-------
for thisComponent in TransitionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('TransitionText.started', TransitionText.tStartRefresh)
thisExp.addData('TransitionText.stopped', TransitionText.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "Transition" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Transition2"-------
continueRoutine = True
# update component parameters for each repeat
text_5.setText('You will begin the main task on the next screen.\n\nPlease keep in mind you will no longer receive visual feedback (i.e. correct/incorrect/miss) on the main task.\n\nPlease press spacebar to begin the main task.')
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
Transition2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Transition2"-------
while continueRoutine:
    # get current time
    t = Transition2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Transition2Clock)
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
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Transition2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Transition2"-------
for thisComponent in Transition2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
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
    
    # ------Prepare to start Routine "InstructionsTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    MainInt1.setPos((0, -0.10))
    MainInt1.setText(Instructions)
    MainInt1.setHeight(0.05)
    MainInt2.setPos((0, -0.25))
    MainInt2.setText("Please press 'spacebar' to begin.")
    MainInt2.setHeight(0.05)
    InstructionPass.keys = []
    InstructionPass.rt = []
    _InstructionPass_allKeys = []
    MainIns = ('Task Block: '+ str(BlockNo) + ' of 16')
    Blocks1.setPos((0.00, 0.20))
    Blocks1.setText(MainIns)
    Blocks1.setHeight(0.05)
    # keep track of which components have finished
    InstructionsTrialComponents = [MainInt1, MainInt2, InstructionPass, Blocks1]
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
    InstructionsTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "InstructionsTrial"-------
    while continueRoutine:
        # get current time
        t = InstructionsTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionsTrialClock)
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
        
        # *MainInt2* updates
        if MainInt2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            MainInt2.frameNStart = frameN  # exact frame index
            MainInt2.tStart = t  # local t and not account for scr refresh
            MainInt2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MainInt2, 'tStartRefresh')  # time at next scr refresh
            MainInt2.setAutoDraw(True)
        
        # *InstructionPass* updates
        waitOnFlip = False
        if InstructionPass.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionPass.frameNStart = frameN  # exact frame index
            InstructionPass.tStart = t  # local t and not account for scr refresh
            InstructionPass.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionPass, 'tStartRefresh')  # time at next scr refresh
            InstructionPass.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(InstructionPass.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(InstructionPass.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if InstructionPass.status == STARTED and not waitOnFlip:
            theseKeys = InstructionPass.getKeys(keyList=['space'], waitRelease=False)
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
            Blocks1.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "InstructionsTrial"-------
    for thisComponent in InstructionsTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('MainInt1.started', MainInt1.tStartRefresh)
    trials.addData('MainInt1.stopped', MainInt1.tStopRefresh)
    trials.addData('MainInt2.started', MainInt2.tStartRefresh)
    trials.addData('MainInt2.stopped', MainInt2.tStopRefresh)
    # check responses
    if InstructionPass.keys in ['', [], None]:  # No response was made
        InstructionPass.keys = None
    trials.addData('InstructionPass.keys',InstructionPass.keys)
    if InstructionPass.keys != None:  # we had a response
        trials.addData('InstructionPass.rt', InstructionPass.rt)
    trials.addData('InstructionPass.started', InstructionPass.tStartRefresh)
    trials.addData('InstructionPass.stopped', InstructionPass.tStopRefresh)
    trials.addData('Blocks1.started', Blocks1.tStartRefresh)
    trials.addData('Blocks1.stopped', Blocks1.tStopRefresh)
    # the Routine "InstructionsTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
        
        # ------Prepare to start Routine "Trial_ISI"-------
        continueRoutine = True
        # update component parameters for each repeat
        if InnerLoop.thisN == 0: # only on the first trial
            jitters = [1.01, 1.0162, 1.0224, 1.0286, 1.0348, 1.041, 1.0472, 1.0534,
        1.0596, 1.0658, 1.072, 1.0782, 1.0844, 1.0906, 1.0968,
        1.103, 1.1092, 1.1154, 1.1216, 1.1278, 1.134, 1.1402, 1.1464,
        1.1526, 1.1588, 1.165, 1.1712, 1.1774, 1.1836, 1.1898, 1.196,
        1.2022, 1.2084, 1.2146, 1.2208, 1.227, 1.2332, 1.2394, 1.2456, 1.2518,
        1.258, 1.2642, 1.2704, 1.2766, 1.2828, 1.289, 1.2952, 1.3014,
        1.3076, 1.3138, 1.32, 1.3262, 1.3324, 1.3386, 1.3448, 1.351,
        1.3572, 1.3634, 1.3696, 1.3758, 1.382, 1.3882, 1.3944, 1.4006,
        1.4068, 1.413, 1.4192, 1.4254, 1.4316, 1.4378, 1.444, 1.4502,
        1.4564, 1.4626, 1.4688, 1.475, 1.4812, 1.4874, 1.4936, 1.4998,
        1.506, 1.5122, 1.5184, 1.5246, 1.5308, 1.537, 1.5432, 1.5494,
        1.5556, 1.5618, 1.568, 1.5742, 1.5804, 1.5866, 1.5928, 1.599,
        1.6052, 1.6114, 1.6176, 1.6238, 1.63, 1.6362, 1.6424, 1.6486,
        1.6548, 1.661, 1.6672, 1.6734, 1.6796, 1.6858, 1.692, 1.6982,
        1.7044, 1.7106, 1.7168, 1.723, 1.7292, 1.7354, 1.7416, 1.7478,
        1.754, 1.7602, 1.7664, 1.7726, 1.7788, 1.785, 1.7912, 1.7974,
        1.8036, 1.8098, 1.816, 1.8222, 1.8284, 1.8346, 1.8408, 1.847,
        1.8532, 1.8594, 1.8656, 1.8718, 1.878, 1.8842, 1.8904, 1.8966, 
        1.9028, 1.909, 1.9152, 1.9214, 1.9276, 1.9338, 1.94, 1.9462,
        1.9524, 1.9586, 1.9648, 1.971, 1.9772, 1.9834, 1.9896, 1.9958] # create the list
            shuffle(jitters) # randomise its order
        
        current_jitter = jitters.pop() # extract one entry on each trial
        thisExp.addData('ISIjitter', current_jitter) # record in the data for this trial
        
        
        
        ISI_Main.setPos((0, 0))
        ISI_Main.setOri(0.0)
        ISI_Main.setText('+')
        ISI_Main.setFlip('None')
        # keep track of which components have finished
        Trial_ISIComponents = [ISI_Main]
        for thisComponent in Trial_ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Trial_ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Trial_ISI"-------
        while continueRoutine:
            # get current time
            t = Trial_ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Trial_ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ISI_Main* updates
            if ISI_Main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ISI_Main.frameNStart = frameN  # exact frame index
                ISI_Main.tStart = t  # local t and not account for scr refresh
                ISI_Main.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI_Main, 'tStartRefresh')  # time at next scr refresh
                ISI_Main.setAutoDraw(True)
            if ISI_Main.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ISI_Main.tStartRefresh + current_jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    ISI_Main.tStop = t  # not accounting for scr refresh
                    ISI_Main.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ISI_Main, 'tStopRefresh')  # time at next scr refresh
                    ISI_Main.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trial_ISI"-------
        for thisComponent in Trial_ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Trial_ISI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial_proper"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        N_backD.setText(LettersDisplayed)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        trial_properComponents = [N_backD, key_resp]
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
        trial_properClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_proper"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_properClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_properClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *N_backD* updates
            if N_backD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                N_backD.frameNStart = frameN  # exact frame index
                N_backD.tStart = t  # local t and not account for scr refresh
                N_backD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(N_backD, 'tStartRefresh')  # time at next scr refresh
                N_backD.setAutoDraw(True)
            if N_backD.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > N_backD.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    N_backD.tStop = t  # not accounting for scr refresh
                    N_backD.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(N_backD, 'tStopRefresh')  # time at next scr refresh
                    N_backD.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
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
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # was this correct?
                    if (key_resp.keys == str(Correctness)) or (key_resp.keys == Correctness):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_properComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_proper"-------
        for thisComponent in trial_properComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        InnerLoop.addData('N_backD.started', N_backD.tStartRefresh)
        InnerLoop.addData('N_backD.stopped', N_backD.tStopRefresh)
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
        InnerLoop.addData('key_resp.started', key_resp.tStartRefresh)
        InnerLoop.addData('key_resp.stopped', key_resp.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'InnerLoop'
    
    
    # ------Prepare to start Routine "Adder"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    AdderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Adder"-------
    while continueRoutine:
        # get current time
        t = AdderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AdderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AdderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Adder"-------
    for thisComponent in AdderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Adder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "EndOfExperiment"-------
continueRoutine = True
# update component parameters for each repeat
text_6.setText("You have now completed the experiment. Thank you.\n\nPlease inform the researcher.\n\nPress 'escape' to close this window.")
# keep track of which components have finished
EndOfExperimentComponents = [text_6]
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
EndOfExperimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndOfExperiment"-------
while continueRoutine:
    # get current time
    t = EndOfExperimentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndOfExperimentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndOfExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndOfExperiment"-------
for thisComponent in EndOfExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# the Routine "EndOfExperiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
