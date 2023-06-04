# This is a script designed to extract volume timings for the n-Back fMRI 
# psychopy task by Colwell et al. (2023) for open source usage. 
# You may need to modify elements of the script if you have changed the block
# design, but the fundemental structural of the script remains the same. 

# You will extract timings based on global time (gt) minus the the timing of
# first slice (t0) when five scanner triggers have completed. So for example,
# when we calculate the time of onset for the first rest period, it will be:
    
#    (Inital_rest_begin_gt - t0)

# If using for commercial or academic publications, please cite the original
# psychopy zenodo/github depository found in the task README.md file.

# WARNING: This script will NOT work on incomplete csv files.
# If you encounter any issues, please contact Michael Colwell 
# (michaelcolwell92@gmail.com / michael.colwell@psych.ox.ac.uk)

import os
import csv
import glob
import pandas as pd
import decimal

# Create a new empty dataframe
nback_df = pd.DataFrame()

# Set the directory for the CSV files
data_dir = r'C:\Users\micha\Desktop\n_back_Timings'

# Construct the file path pattern using os.path.join()
file_pattern = os.path.join(data_dir, '*N-Back*.csv')

# Search for CSV files with "n-back" in their names in the specified directory
csv_files = glob.glob(file_pattern)

# Create a list to hold the new rows
new_rows = []

# Loop over each CSV file
for csv_file in csv_files:
    # Extract the desired values from the CSV file
    with open(csv_file, 'r') as input_file:
        reader = csv.reader(input_file)
        
        # Loop over each row in the CSV file
        for i, row in enumerate(reader):
            # If this is the second row
            if i == 1:
                # Extract the value in column 72 (index 71)
                participant_id = row[71]
                visit = row[73]
            # Extract t0
            if i == 10:
                # Extract the value in column 43 (index 42)
                t0 = row[42]
            if i == 10:
                # Extract and convert rest period one
                initial_rest_begin = row[43]
                initial_rest_end = row[44]
                Initial_rest_begin_t0 = float(initial_rest_begin) - float(t0)
                Initial_rest_length = float(initial_rest_end) - float(initial_rest_begin)
            if i == 20:
                # Extract and convert rest period two
                One_Rest_begin = row[65]
                One_Rest_end = row[66]
                One_Rest_begin_t0 = float(One_Rest_begin) - float(t0)
                One_Rest_length = float(One_Rest_end) - float(One_Rest_begin)
            if i == 31:
                # Extract and convert rest period three
                Two_Rest_begin = row[65]
                Two_Rest_end = row[66]
                Two_Rest_begin_t0 = float(Two_Rest_begin) - float(t0)
                Two_Rest_length = float(Two_Rest_end) - float(Two_Rest_begin)
            if i == 42:
                # Extract and convert rest period four
                Three_Rest_begin = row[65]
                Three_Rest_end = row[66]
                Three_Rest_begin_t0 = float(Three_Rest_begin) - float(t0)
                Three_Rest_length = float(Three_Rest_end) - float(Three_Rest_begin)
            if i == 53:
                # Extract and convert rest period five
                Four_Rest_begin = row[65]
                Four_Rest_end = row[66]
                Four_Rest_begin_t0 = float(Four_Rest_begin) - float(t0)
                Four_Rest_length = float(Four_Rest_end) - float(Four_Rest_begin)
            if i == 64:
                # Extract and convert rest period six
                Five_Rest_begin = row[65]
                Five_Rest_end = row[66]
                Five_Rest_begin_t0 = float(Five_Rest_begin) - float(t0)
                Five_Rest_length = float(Five_Rest_end) - float(Five_Rest_begin)
            if i == 75:
                # Extract and convert rest period seven
                Six_Rest_begin = row[65]
                Six_Rest_end = row[66]
                Six_Rest_begin_t0 = float(Six_Rest_begin) - float(t0)
                Six_Rest_length = float(Six_Rest_end) - float(Six_Rest_begin)
            if i == 86:
                # Extract and convert rest period eight
                Seven_Rest_begin = row[65]
                Seven_Rest_end = row[66]
                Seven_Rest_begin_t0 = float(Seven_Rest_begin) - float(t0)
                Seven_Rest_length = float(Seven_Rest_end) - float(Seven_Rest_begin)
            if i == 97:
                # Extract and convert rest period nine
                Eight_Rest_begin = row[65]
                Eight_Rest_end = row[66]
                Eight_Rest_begin_t0 = float(Eight_Rest_begin) - float(t0)
                Eight_Rest_length = float(Eight_Rest_end) - float(Eight_Rest_begin)
            if i == 108:
                # Extract and convert rest period ten
                Nine_Rest_begin = row[65]
                Nine_Rest_end = row[66]
                Nine_Rest_begin_t0 = float(Nine_Rest_begin) - float(t0)
                Nine_Rest_length = float(Nine_Rest_end) - float(Nine_Rest_begin)
            if i == 119:
                # Extract and convert rest period eleven
                Ten_Rest_begin = row[65]
                Ten_Rest_end = row[66]
                Ten_Rest_begin_t0 = float(Ten_Rest_begin) - float(t0)
                Ten_Rest_length = float(Ten_Rest_end) - float(Ten_Rest_begin)
            if i == 130:
                # Extract and convert rest period twelve
                Eleven_Rest_begin = row[65]
                Eleven_Rest_end = row[66]
                Eleven_Rest_begin_t0 = float(Eleven_Rest_begin) - float(t0)
                Eleven_Rest_length = float(Eleven_Rest_end) - float(Eleven_Rest_begin)
            if i == 141:
                # Extract and convert rest period thirteen
                Twleve_Rest_begin = row[65]
                Twleve_Rest_end = row[66]
                Twleve_Rest_begin_t0 = float(Twleve_Rest_begin) - float(t0)
                Twleve_Rest_length = float(Twleve_Rest_end) - float(Twleve_Rest_begin)
            if i == 152:
                # Extract and convert rest period fourteen
                Thirteen_Rest_begin = row[65]
                Thirteen_Rest_end = row[66]
                Thirteen_Rest_begin_t0 = float(Thirteen_Rest_begin) - float(t0)
                Thirteen_Rest_length = float(Thirteen_Rest_end) - float(Thirteen_Rest_begin)
            if i == 163:
                # Extract and convert rest period fifteen
                Fourteen_Rest_begin = row[65]
                Fourteen_Rest_end = row[66]
                Fourteen_Rest_begin_t0 = float(Fourteen_Rest_begin) - float(t0)
                Fourteen_Rest_length = float(Fourteen_Rest_end) - float(Fourteen_Rest_begin)
            if i == 174:
                # Extract and convert rest period sixteen
                Fifteen_Rest_begin = row[65]
                Fifteen_Rest_end = row[66]
                Fifteen_Rest_begin_t0 = float(Fifteen_Rest_begin) - float(t0)
                Fifteen_Rest_length = float(Fifteen_Rest_end) - float(Fifteen_Rest_begin)
            if i == 185:
                # Extract and convert rest period seventeen (final)
                Sixteen_Rest_begin = row[65]
                Sixteen_Rest_end = row[66]
                Sixteen_Rest_begin_t0 = float(Sixteen_Rest_begin) - float(t0)
                Sixteen_Rest_length = float(Sixteen_Rest_end) - float(Sixteen_Rest_begin)

                Initial_rest_begin_t0 = decimal.Decimal(Initial_rest_begin_t0)
                Initial_rest_begin_t0 = Initial_rest_begin_t0.quantize(decimal.Decimal('0.000001'), rounding=decimal.ROUND_HALF_UP)

                # Create df for rest periods
                rests_df = pd.DataFrame({'Rest_start_t': [Initial_rest_begin_t0, One_Rest_begin_t0, Two_Rest_begin_t0, Three_Rest_begin_t0, Four_Rest_begin_t0, Five_Rest_begin_t0, Six_Rest_begin_t0, Seven_Rest_begin_t0, 
                                               Eight_Rest_begin_t0, Nine_Rest_begin_t0, Ten_Rest_begin_t0, Eleven_Rest_begin_t0, Twleve_Rest_begin_t0, Thirteen_Rest_begin_t0, Fourteen_Rest_begin_t0, Fifteen_Rest_begin_t0, Sixteen_Rest_begin_t0], 
                                         'Rest_length': [Initial_rest_length, One_Rest_length, Two_Rest_length, Three_Rest_length, Four_Rest_length, Five_Rest_length, Six_Rest_length, Seven_Rest_length, Eight_Rest_length, Nine_Rest_length,
                                                         Ten_Rest_length, Eleven_Rest_length, Twleve_Rest_length, Thirteen_Rest_length, Fourteen_Rest_length, Fifteen_Rest_length, Sixteen_Rest_length],
                                         'Ones' : ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']})
               
                # Create a new folder for rests to save the file
                output_folder = os.path.join(data_dir, 'Rests')
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                
                # Construct the file name
                file_name = 'nback_' + str(participant_id) + '_' + str(visit) + '_' + 'Resting_timing' + '.txt'  
                
                # Write the new dataframe to a new TXT file
                rests_df.to_csv(os.path.join(output_folder, file_name), sep='\t', index=False, header=False)

            ################################################
            # Convert and extract 0-back block 1
            if i == 10:
                Block1_Zeroback_begin = row[60]
            if i == 19:  
                Block1_Zeroback_end = row[61]
                Block1_Zeroback_begin_t0 = float(Block1_Zeroback_begin) - float(t0)
                Block1_Zeroback_length = float(Block1_Zeroback_end) - float(Block1_Zeroback_begin)   
            # Convert and extract 0-back block 2
            if i == 65:
                Block2_Zeroback_begin = row[60]
            if i == 74:  
                Block2_Zeroback_end = row[61]
                Block2_Zeroback_begin_t0 = float(Block2_Zeroback_begin) - float(t0)
                Block2_Zeroback_length = float(Block2_Zeroback_end) - float(Block2_Zeroback_begin)   
            # Convert and extract 0-back block 3
            if i == 109:
                Block3_Zeroback_begin = row[60]
            if i == 118:  
                Block3_Zeroback_end = row[61]
                Block3_Zeroback_begin_t0 = float(Block3_Zeroback_begin) - float(t0)
                Block3_Zeroback_length = float(Block3_Zeroback_end) - float(Block3_Zeroback_begin) 
            # Convert and extract 0-back block 4
            if i == 153:
                Block4_Zeroback_begin = row[60]
            if i == 162:  
                Block4_Zeroback_end = row[61]
                Block4_Zeroback_begin_t0 = float(Block4_Zeroback_begin) - float(t0)
                Block4_Zeroback_length = float(Block4_Zeroback_end) - float(Block4_Zeroback_begin) 

                # Create df for zeroback periods
                zeroback_df = pd.DataFrame({'Zeroback_start_t': [Block1_Zeroback_begin_t0,Block2_Zeroback_begin_t0,Block3_Zeroback_begin_t0,Block4_Zeroback_begin_t0],
                                            'Block_length': [Block1_Zeroback_length,Block2_Zeroback_length,Block3_Zeroback_length,Block4_Zeroback_length],
                                         'Ones' : ['1','1','1','1']})
               
                # Create a new folder for zeroback to save the file
                output_folder2 = os.path.join(data_dir, 'Zeroback')
                if not os.path.exists(output_folder2):
                    os.makedirs(output_folder2)
                # Construct the file name
                file_name2 = 'nback_' + str(participant_id) + '_' + str(visit) + '_' + 'Zeroback' + '.txt'  
                # Write the new dataframe to a new TXT file
                zeroback_df.to_csv(os.path.join(output_folder2, file_name2), sep='\t', index=False, header=False)
                
                ################################################

            # Convert and extract 1-back block 1
            if i == 21:
                Block1_Oneback_begin = row[60]
            if i == 30:  
                Block1_Oneback_end = row[61]
                Block1_Oneback_begin_t0 = float(Block1_Oneback_begin) - float(t0)
                Block1_Oneback_length = float(Block1_Oneback_end) - float(Block1_Oneback_begin)   
            # Convert and extract 1-back block 2
            if i == 54:
                Block2_Oneback_begin = row[60]
            if i == 63:  
                Block2_Oneback_end = row[61]
                Block2_Oneback_begin_t0 = float(Block2_Oneback_begin) - float(t0)
                Block2_Oneback_length = float(Block2_Oneback_end) - float(Block2_Oneback_begin)   
            # Convert and extract 1-back block 3
            if i == 131:
                Block3_Oneback_begin = row[60]
            if i == 140:  
                Block3_Oneback_end = row[61]
                Block3_Oneback_begin_t0 = float(Block3_Oneback_begin) - float(t0)
                Block3_Oneback_length = float(Block3_Oneback_end) - float(Block3_Oneback_begin) 
            # Convert and extract 1-back block 4
            if i == 164:
                Block4_Oneback_begin = row[60]
            if i == 173:  
                Block4_Oneback_end = row[61]
                Block4_Oneback_begin_t0 = float(Block4_Oneback_begin) - float(t0)
                Block4_Oneback_length = float(Block4_Oneback_end) - float(Block4_Oneback_begin) 

                # Create df for oneback periods
                oneback_df = pd.DataFrame({'Oneback_start_t': [Block1_Oneback_begin_t0,Block2_Oneback_begin_t0,Block3_Oneback_begin_t0,Block4_Oneback_begin_t0],
                                            'Block_length': [Block1_Oneback_length,Block2_Oneback_length,Block3_Oneback_length,Block4_Oneback_length],
                                         'Ones' : ['1','1','1','1']})
               
                # Create a new folder for oneback to save the file
                output_folder3 = os.path.join(data_dir, 'Oneback')
                if not os.path.exists(output_folder3):
                    os.makedirs(output_folder3)
                # Construct the file name
                file_name3 = 'nback_' + str(participant_id) + '_' + str(visit) + '_' + 'Oneback' + '.txt'      
                # Write the new dataframe to a new TXT file
                oneback_df.to_csv(os.path.join(output_folder3, file_name3), sep='\t', index=False, header=False)
                
                ################################################
                
            # Convert and extract 2-back block 1
            if i == 32:
                Block1_Twoback_begin = row[60]
            if i == 41:  
                Block1_Twoback_end = row[61]
                Block1_Twoback_begin_t0 = float(Block1_Twoback_begin) - float(t0)
                Block1_Twoback_length = float(Block1_Twoback_end) - float(Block1_Twoback_begin)   
            # Convert and extract 2-back block 2
            if i == 87:
                Block2_Twoback_begin = row[60]
            if i == 96:  
                Block2_Twoback_end = row[61]
                Block2_Twoback_begin_t0 = float(Block2_Twoback_begin) - float(t0)
                Block2_Twoback_length = float(Block2_Twoback_end) - float(Block2_Twoback_begin)   
            # Convert and extract 2-back block 3
            if i == 120:
                Block3_Twoback_begin = row[60]
            if i == 129:  
                Block3_Twoback_end = row[61]
                Block3_Twoback_begin_t0 = float(Block3_Twoback_begin) - float(t0)
                Block3_Twoback_length = float(Block3_Twoback_end) - float(Block3_Twoback_begin) 
            # Convert and extract 2-back block 4
            if i == 142:
                Block4_Twoback_begin = row[60]
            if i == 151:  
                Block4_Twoback_end = row[61]
                Block4_Twoback_begin_t0 = float(Block4_Twoback_begin) - float(t0)
                Block4_Twoback_length = float(Block4_Twoback_end) - float(Block4_Twoback_begin) 

                # Create df for twoback periods
                Twoback_df = pd.DataFrame({'Twoback_start_t': [Block1_Twoback_begin_t0,Block2_Twoback_begin_t0,Block3_Twoback_begin_t0,Block4_Twoback_begin_t0],
                                            'Block_length': [Block1_Twoback_length,Block2_Twoback_length,Block3_Twoback_length,Block4_Twoback_length],
                                         'Twos' : ['1','1','1','1']})
               
                # Create a new folder for twoback to save the file
                output_folder4 = os.path.join(data_dir, 'Twoback')
                if not os.path.exists(output_folder4):
                    os.makedirs(output_folder4)
                # Construct the file name
                file_name4 = 'nback_' + str(participant_id) + '_' + str(visit) + '_' + 'Twoback' + '.txt'  
                # Write the new dataframe to a new TXT file
                Twoback_df.to_csv(os.path.join(output_folder4, file_name4), sep='\t', index=False, header=False)
                
                ################################################    
                
            # Convert and extract 3-back block 1
            if i == 43:
                # Extract and convert rest period seventeen (final)
                Block1_Threeback_begin = row[60]
            if i == 52:  
                Block1_Threeback_end = row[61]
                Block1_Threeback_begin_t0 = float(Block1_Threeback_begin) - float(t0)
                Block1_Threeback_length = float(Block1_Threeback_end) - float(Block1_Threeback_begin)   
            # Convert and extract 3-back block 2
            if i == 76:
                Block2_Threeback_begin = row[60]
            if i == 85:  
                Block2_Threeback_end = row[61]
                Block2_Threeback_begin_t0 = float(Block2_Threeback_begin) - float(t0)
                Block2_Threeback_length = float(Block2_Threeback_end) - float(Block2_Threeback_begin)   
            # Convert and extract 3-back block 3
            if i == 98:
                Block3_Threeback_begin = row[60]
            if i == 107:  
                Block3_Threeback_end = row[61]
                Block3_Threeback_begin_t0 = float(Block3_Threeback_begin) - float(t0)
                Block3_Threeback_length = float(Block3_Threeback_end) - float(Block3_Threeback_begin) 
            # Convert and extract 3-back block 4
            if i == 175:
                Block4_Threeback_begin = row[60]
            if i == 184:  
                Block4_Threeback_end = row[61]
                Block4_Threeback_begin_t0 = float(Block4_Threeback_begin) - float(t0)
                Block4_Threeback_length = float(Block4_Threeback_end) - float(Block4_Threeback_begin) 

                # Create df for threeback periods
                Threeback_df = pd.DataFrame({'Threeback_start_t': [Block1_Threeback_begin_t0,Block2_Threeback_begin_t0,Block3_Threeback_begin_t0,Block4_Threeback_begin_t0],
                                            'Block_length': [Block1_Threeback_length,Block2_Threeback_length,Block3_Threeback_length,Block4_Threeback_length],
                                         'Threes' : ['1','1','1','1']})
               
                # Create a new folder for zeroback to save the file
                output_folder5 = os.path.join(data_dir, 'Threeback')
                if not os.path.exists(output_folder5):
                    os.makedirs(output_folder5)
                # Construct the file name
                file_name5 = 'nback_' + str(participant_id) + '_' + str(visit) + '_' + 'Threeback' + '.txt'     
                # Write the new dataframe to a new TXT file
                Threeback_df.to_csv(os.path.join(output_folder5, file_name5), sep='\t', index=False, header=False)
                
                ################################################     
                
            # Convert and extract instructions set 1
            if i == 10:
                Instructions1_begin = row[47]
                Instructions1_end = row[48]
                Instructions1_begin_t0 = float(Instructions1_begin) - float(t0)
                Instructions1_length = float(Instructions1_end) - float(Instructions1_begin)     
                # Convert and extract instructions set 2
            if i == 21:
                Instructions2_begin = row[47]
                Instructions2_end = row[48]
                Instructions2_begin_t0 = float(Instructions2_begin) - float(t0)
                Instructions2_length = float(Instructions2_end) - float(Instructions2_begin)               
                # Convert and extract instructions set 3
            if i == 32:
                Instructions3_begin = row[47]
                Instructions3_end = row[48]
                Instructions3_begin_t0 = float(Instructions3_begin) - float(t0)
                Instructions3_length = float(Instructions3_end) - float(Instructions3_begin)   
                # Convert and extract instructions set 4
            if i == 43:
                Instructions4_begin = row[47]
                Instructions4_end = row[48]
                Instructions4_begin_t0 = float(Instructions4_begin) - float(t0)
                Instructions4_length = float(Instructions4_end) - float(Instructions4_begin)
                # Convert and extract instructions set 5
            if i == 54:
                Instructions5_begin = row[47]
                Instructions5_end = row[48]
                Instructions5_begin_t0 = float(Instructions5_begin) - float(t0)
                Instructions5_length = float(Instructions5_end) - float(Instructions5_begin)   
                # Convert and extract instructions set 6
            if i == 65:
                Instructions6_begin = row[47]
                Instructions6_end = row[48]
                Instructions6_begin_t0 = float(Instructions6_begin) - float(t0)
                Instructions6_length = float(Instructions6_end) - float(Instructions6_begin)   
                # Convert and extract instructions set 7
            if i == 76:
                Instructions7_begin = row[47]
                Instructions7_end = row[48]
                Instructions7_begin_t0 = float(Instructions7_begin) - float(t0)
                Instructions7_length = float(Instructions7_end) - float(Instructions7_begin)   
                # Convert and extract instructions set 8
            if i == 87:
                Instructions8_begin = row[47]
                Instructions8_end = row[48]
                Instructions8_begin_t0 = float(Instructions8_begin) - float(t0)
                Instructions8_length = float(Instructions8_end) - float(Instructions8_begin)   
                # Convert and extract instructions set 9
            if i == 98:
                Instructions9_begin = row[47]
                Instructions9_end = row[48]
                Instructions9_begin_t0 = float(Instructions9_begin) - float(t0)
                Instructions9_length = float(Instructions9_end) - float(Instructions9_begin)   
                # Convert and extract instructions set 10
            if i == 109:
                Instructions10_begin = row[47]
                Instructions10_end = row[48]
                Instructions10_begin_t0 = float(Instructions10_begin) - float(t0)
                Instructions10_length = float(Instructions10_end) - float(Instructions10_begin)   
                # Convert and extract instructions set 11
            if i == 120:
                Instructions11_begin = row[47]
                Instructions11_end = row[48]
                Instructions11_begin_t0 = float(Instructions11_begin) - float(t0)
                Instructions11_length = float(Instructions11_end) - float(Instructions11_begin)   
                # Convert and extract instructions set 12
            if i == 131:
                Instructions12_begin = row[47]
                Instructions12_end = row[48]
                Instructions12_begin_t0 = float(Instructions12_begin) - float(t0)
                Instructions12_length = float(Instructions12_end) - float(Instructions12_begin)   
                # Convert and extract instructions set 13
            if i == 142:
                Instructions13_begin = row[47]
                Instructions13_end = row[48]
                Instructions13_begin_t0 = float(Instructions13_begin) - float(t0)
                Instructions13_length = float(Instructions13_end) - float(Instructions13_begin)   
                # Convert and extract instructions set 14
            if i == 153:
                Instructions14_begin = row[47]
                Instructions14_end = row[48]
                Instructions14_begin_t0 = float(Instructions14_begin) - float(t0)
                Instructions14_length = float(Instructions14_end) - float(Instructions14_begin)   
                # Convert and extract instructions set 15
            if i == 164:
                Instructions15_begin = row[47]
                Instructions15_end = row[48]
                Instructions15_begin_t0 = float(Instructions15_begin) - float(t0)
                Instructions15_length = float(Instructions15_end) - float(Instructions15_begin)   
                # Convert and extract instructions set 16
            if i == 175:
                Instructions16_begin = row[47]
                Instructions16_end = row[48]
                Instructions16_begin_t0 = float(Instructions16_begin) - float(t0)
                Instructions16_length = float(Instructions16_end) - float(Instructions16_begin)   
                
                # Create df for instruction periods (regressor)
                Instructions_df = pd.DataFrame({'Instructions_start_t': [Instructions1_begin_t0, Instructions2_begin_t0, Instructions3_begin_t0, Instructions4_begin_t0, Instructions5_begin_t0, Instructions6_begin_t0, Instructions7_begin_t0,
                                                                      Instructions8_begin_t0, Instructions9_begin_t0, Instructions10_begin_t0, Instructions11_begin_t0, Instructions12_begin_t0, Instructions13_begin_t0, Instructions14_begin_t0,
                                                                      Instructions15_begin_t0, Instructions16_begin_t0],
                                             'Instructions_length': [Instructions1_length, Instructions2_length, Instructions3_length, Instructions4_length, Instructions5_length, Instructions6_length, Instructions7_length, 
                                                                     Instructions8_length, Instructions9_length, Instructions10_length, Instructions11_length, Instructions12_length, Instructions13_length, Instructions14_length,
                                                                     Instructions15_length, Instructions16_length],
                                             'Ones' : ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']})
                # Create a new folder for zeroback to save the file
                output_folder6 = os.path.join(data_dir, 'InstructionsPeriod_Regress')
                if not os.path.exists(output_folder6):
                    os.makedirs(output_folder6)
                # Construct the file name
                file_name6 = 'nback_' + str(participant_id) + '_' + str(visit) + '_' + 'Instructions_timings' + '.txt'     
                # Write the new dataframe to a new TXT file
                Instructions_df.to_csv(os.path.join(output_folder6, file_name6), sep='\t', index=False, header=False)

                ################################################     
                
            # Convert and extract ending screening timings (regress)
            if i == 185:
                Ending_begin = row[66]
                Ending_begin_t0 = float(Ending_begin) - float(t0)
                Ending_length = 100 #End screen until the scan ends    

                # Create df for ending period
                Ending_df = pd.DataFrame({'Ending_start_t': [Ending_begin_t0],
                                            'Block_length': [Ending_length],
                                         'Ones' : ['1']})
               
                # Create a new folder for zeroback to save the file
                output_folder7 = os.path.join(data_dir, 'Ending_timing_Regress')
                if not os.path.exists(output_folder7):
                    os.makedirs(output_folder7)
                # Construct the file name
                file_name7 = 'nback_' + str(participant_id) + '_' + str(visit) + '_' + 'Ending_timing' + '.txt'     
                # Write the new dataframe to a new TXT file
                Ending_df.to_csv(os.path.join(output_folder7, file_name7), sep='\t', index=False, header=False)

                ################################################     
               
            #This is optional - these are the short ISIs between the instructions and the start of each block. You may want to regress these out.
                
            if i == 10:
                PRE_ISI_1_begin = row[49]
                PRE_ISI_1_end = row[60]
                PRE_ISI_1_begin_t0 = float(PRE_ISI_1_begin) - float(t0)
                PRE_ISI_1_length = float(PRE_ISI_1_end) - float(PRE_ISI_1_begin)    
            if i == 21:
                PRE_ISI_2_begin = row[49]
                PRE_ISI_2_end = row[60]
                PRE_ISI_2_begin_t0 = float(PRE_ISI_2_begin) - float(t0)
                PRE_ISI_2_length = float(PRE_ISI_2_end) - float(PRE_ISI_2_begin) 
            if i == 32:
                PRE_ISI_3_begin = row[49]
                PRE_ISI_3_end = row[60]
                PRE_ISI_3_begin_t0 = float(PRE_ISI_3_begin) - float(t0)
                PRE_ISI_3_length = float(PRE_ISI_3_end) - float(PRE_ISI_3_begin)   
            if i == 43:
                PRE_ISI_4_begin = row[49]
                PRE_ISI_4_end = row[60]
                PRE_ISI_4_begin_t0 = float(PRE_ISI_4_begin) - float(t0)
                PRE_ISI_4_length = float(PRE_ISI_4_end) - float(PRE_ISI_4_begin)   
            if i == 54:
                PRE_ISI_5_begin = row[49]
                PRE_ISI_5_end = row[60]
                PRE_ISI_5_begin_t0 = float(PRE_ISI_5_begin) - float(t0)
                PRE_ISI_5_length = float(PRE_ISI_5_end) - float(PRE_ISI_5_begin)   
            if i == 65:
                PRE_ISI_6_begin = row[49]
                PRE_ISI_6_end = row[60]
                PRE_ISI_6_begin_t0 = float(PRE_ISI_6_begin) - float(t0)
                PRE_ISI_6_length = float(PRE_ISI_6_end) - float(PRE_ISI_6_begin)   
            if i == 76:
                PRE_ISI_7_begin = row[49]
                PRE_ISI_7_end = row[60]
                PRE_ISI_7_begin_t0 = float(PRE_ISI_7_begin) - float(t0)
                PRE_ISI_7_length = float(PRE_ISI_7_end) - float(PRE_ISI_7_begin)   
            if i == 87:
                PRE_ISI_8_begin = row[49]
                PRE_ISI_8_end = row[60]
                PRE_ISI_8_begin_t0 = float(PRE_ISI_8_begin) - float(t0)
                PRE_ISI_8_length = float(PRE_ISI_8_end) - float(PRE_ISI_8_begin)   
            if i == 98:
                PRE_ISI_9_begin = row[49]
                PRE_ISI_9_end = row[60]
                PRE_ISI_9_begin_t0 = float(PRE_ISI_9_begin) - float(t0)
                PRE_ISI_9_length = float(PRE_ISI_9_end) - float(PRE_ISI_9_begin)   
            if i == 109:
                PRE_ISI_10_begin = row[49]
                PRE_ISI_10_end = row[60]
                PRE_ISI_10_begin_t0 = float(PRE_ISI_10_begin) - float(t0)
                PRE_ISI_10_length = float(PRE_ISI_10_end) - float(PRE_ISI_10_begin)   
            if i == 120:
                PRE_ISI_11_begin = row[49]
                PRE_ISI_11_end = row[60]
                PRE_ISI_11_begin_t0 = float(PRE_ISI_11_begin) - float(t0)
                PRE_ISI_11_length = float(PRE_ISI_11_end) - float(PRE_ISI_11_begin)   
            if i == 131:
                PRE_ISI_12_begin = row[49]
                PRE_ISI_12_end = row[60]
                PRE_ISI_12_begin_t0 = float(PRE_ISI_12_begin) - float(t0)
                PRE_ISI_12_length = float(PRE_ISI_12_end) - float(PRE_ISI_12_begin)   
            if i == 142:
                PRE_ISI_13_begin = row[49]
                PRE_ISI_13_end = row[60]
                PRE_ISI_13_begin_t0 = float(PRE_ISI_13_begin) - float(t0)
                PRE_ISI_13_length = float(PRE_ISI_13_end) - float(PRE_ISI_13_begin)   
            if i == 153:
                PRE_ISI_14_begin = row[49]
                PRE_ISI_14_end = row[60]
                PRE_ISI_14_begin_t0 = float(PRE_ISI_14_begin) - float(t0)
                PRE_ISI_14_length = float(PRE_ISI_14_end) - float(PRE_ISI_14_begin)   
            if i == 164:
                PRE_ISI_15_begin = row[49]
                PRE_ISI_15_end = row[60]
                PRE_ISI_15_begin_t0 = float(PRE_ISI_15_begin) - float(t0)
                PRE_ISI_15_length = float(PRE_ISI_15_end) - float(PRE_ISI_15_begin)   
            if i == 175:
                PRE_ISI_16_begin = row[49]
                PRE_ISI_16_end = row[60]
                PRE_ISI_16_begin_t0 = float(PRE_ISI_16_begin) - float(t0)
                PRE_ISI_16_length = float(PRE_ISI_16_end) - float(PRE_ISI_16_begin)   

                # Create df for instruction periods (regressor)
                PRE_ISI_df = pd.DataFrame({'PRE_ISI_start_t': [PRE_ISI_1_begin_t0, PRE_ISI_2_begin_t0, PRE_ISI_3_begin_t0, PRE_ISI_4_begin_t0, PRE_ISI_5_begin_t0, PRE_ISI_6_begin_t0, PRE_ISI_7_begin_t0, PRE_ISI_8_begin_t0,
                                                               PRE_ISI_9_begin_t0, PRE_ISI_10_begin_t0, PRE_ISI_11_begin_t0, PRE_ISI_12_begin_t0, PRE_ISI_13_begin_t0, PRE_ISI_14_begin_t0, PRE_ISI_15_begin_t0, PRE_ISI_16_begin_t0],
                                             'PRE_ISI_length': [PRE_ISI_1_length, PRE_ISI_2_length, PRE_ISI_3_length, PRE_ISI_4_length, PRE_ISI_5_length, PRE_ISI_6_length, PRE_ISI_7_length, PRE_ISI_8_length, 
                                                                PRE_ISI_9_length,PRE_ISI_10_length, PRE_ISI_11_length, PRE_ISI_12_length, PRE_ISI_13_length, PRE_ISI_14_length, PRE_ISI_15_length, PRE_ISI_16_length],
                                             'Ones' : ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']})
                # Create a new folder for zeroback to save the file
                output_folder7 = os.path.join(data_dir, 'PRE_ISI_timings_Regress')
                if not os.path.exists(output_folder7):
                    os.makedirs(output_folder7)
                # Construct the file name
                file_name7 = 'nback_' + str(participant_id) + '_' + str(visit) + '_' + 'PRE_ISI_timings' + '.txt'     
                # Write the new dataframe to a new TXT file
                PRE_ISI_df.to_csv(os.path.join(output_folder7, file_name7), sep='\t', index=False, header=False)

### End of Script