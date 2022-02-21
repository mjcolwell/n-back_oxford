#################################################

# N-Back Task (PERL - Oxford)
Version 1.3 (21/02/2022)

Task made by Michael Colwell (michael.colwell@psych.ox.ac.uk)

Pre-processing scripts made by Hosana Tagomori (hosana.tagomori@lmh.ox.ac.uk) & Michael Colwell (michael.colwell@psych.ox.ac.uk)

Debugged by: Chloe Wigg, Amy Gillespie, Calum Guinea, & Tereza Ruzickova

## License: 
The task materials and preprocessing script are offered free of charge for researchers. 
It is requested that researchers who publish data using these materials (task or preprocessing script) cite the code for the task in relevant publications.

**Please cite the code below**:

Colwell, M., Tagomori, H., Murphy, S., & Harmer, H. (2021). N-Back Task (Version 1.3). Zenodo. https://doi.org/

This task is currently in-use in the Psychopharmacology and Emotion Laboratory (PERL) at the Department of Psychiatry, University of Oxford. Two ongoing psychopharmacology projects (FEN&COG - NCT05026398; PROGRESS) are currently using these tasks.

## Information
Requires 

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