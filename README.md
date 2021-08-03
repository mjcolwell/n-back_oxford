#################################################

N-Back Task - Updated for 2021 for Psychopy
Version 1.0 (01/06/2021)

Made by Michael Colwell (michael.colwell@psych.ox.ac.uk)

Debugged by: Chloe Wigg, Amy Gillespie, Calum Guinea, & Tereza Ruzickova

This is a standard N-Back working memory task, with four subtypes (n-types): 
zero-back, one-back, two-back, & three-back. 

Stimuli are displayed for 2000ms, with a random interstimulus interval of
between 1000-2000ms. The block design of the old n-back task on E-Prime has been
repurposed here (16 blocks total, 10 stimulus per block). There will only 
be 'target' stimuli around 2-3 times per each block (around 20-25%) as per
standard n-back design.

Each block has been mixed so that there is a different rule each block (permenant set-shifting). 
Four new practice blocks has been added to this version, as well as two seperate
versions of the task for pre/post design. You may generate new random lists
using a partially completed random array generation script provided in the
main folder ('ArrayScriptBase.py').

This task has been tested on a 120hz monitor but should work fine on a 
60hz monitor.

If you have any questions or encounter any bugs, please email
michael.colwell@psych.ox.ac.uk

#################################################