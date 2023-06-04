#################################################

# N-Back - fMRI and non-scanner tasks (PERL - Oxford)

Task of verbal working memory (n-back) made by Michael Colwell (michael.colwell@psych.ox.ac.uk).

## Version 1.5 (04/06/2023)

Latest version of the task overhauls older versions (1.4 and earlier) with new stimuli, optimisations and two task versions;

1. The scanner task version has been designed for use during fMRI acquisition
2. The  non-scanner task version can be completed standalone. This can be used to compliment the fMRI task for outside scanner practice.

Older versions of this task have been used within publications (e.g., https://www.sciencedirect.com/science/article/pii/S2772408523000686?via%3Dihub). This version of the task is currently in use in the several projects in PERL Oxford (PEACE - NCT05849675; FEN&COG - NCT05026398; PROGRESS).

## License: 

This release is open for free, academic use/modification. If you use this work in an academic paper/dissemination, **Please cite the code below**:

## Credits

Pre-processing scripts made by Hosana Tagomori (hosana.tagomori@lmh.ox.ac.uk) with optimisations by Michael Colwell.

Massive help from Marieke Martens (marieke.martens@psych.ox.ac.uk) in helping to create a neuroimaging version of the task.

Original debuggers: Chloe Wigg, Amy Gillespie, Calum Guinea, & Tereza Ruzickova

## Information

This is a standard N-Back working memory task, with four subtypes (n-types):  zero-back, one-back, two-back, & three-back. 

Stimuli are displayed for 2000ms, with a random interstimulus interval of between 1000-2000ms. The block design of the old n-back task on E-Prime has been repurposed here (16 blocks total, 10 stimulus per block). 
There will only  be 'target' stimuli around 2-3 times per each block (around 20-25%) as per standard n-back design.

Each block has been mixed so that there is a different rule each block (permenant set-shifting). Four new practice blocks has been added to this version, as well as two seperate versions of the task for pre/post design. 
You may generate new random lists using a partially completed random array generation script provided in the main folder ('ArrayScriptBase.py').

This task has been tested on a 120hz monitor but should work fine on a 60hz monitor.

If you have any questions or encounter any bugs, please email michael.colwell@psych.ox.ac.uk

## Instructions:

1. Download Psychopy (version v2020.2.8 and above) - https://www.psychopy.org/download.html
2. Once installed, unzip the contents of this folder to a location on your computer
3. Open the 'nback_2021_psychopy_version-main' folder and double click on 'N-Back__New_Version_2021_'
5. Click 'run' experiment - You can choose between two task versions ('1' and '2') for PRE/POST design.
6. Press run and follow onscreen instructions
7. Once the experiment has ended, you will find your test data in the 'data' folder.

--------
