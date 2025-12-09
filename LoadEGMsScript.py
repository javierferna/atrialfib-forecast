# Load file example
import lzma
import pickle
import pandas as pd
import os
import re

# Load the Excel file with map names
excel_path = 'D:/ML HEALTHCARE/CARDIO FINAL PROJECT/MapsInfo.xlsx'
maps_df = pd.read_excel(excel_path)

# Create a dictionary mapping patient date to map_name (AF column)
patient_to_map = dict(zip(maps_df['Patient'], maps_df['AF']))

# Directory containing EGM files
egms_dir = 'D:/ML HEALTHCARE/CARDIO FINAL PROJECT/EGMS'

# Process all files in the EGMS folder
for filename in os.listdir(egms_dir):
    if filename.endswith('_EGMs.xz'):
        # Extract patient date from filename (e.g., "Patient 2021_11_10_EGMs.xz" -> "2021_11_10")
        match = re.search(r'Patient (\d{4}_\d{2}_\d{2})_EGMs\.xz', filename)
        if match:
            patient_date = match.group(1)

            # Get map_name from the Excel mapping
            map_name = patient_to_map.get(patient_date)

            if map_name is None:
                print(f"Warning: No map_name found for {filename}")
                continue

            # Load the file
            load_file_path = os.path.join(egms_dir, filename)
            with lzma.open(load_file_path, 'rb') as f:
                file_content = pickle.load(f)

            # Get the map index
            map_index = file_content['map'].tolist().index(map_name)

            # Get bipolar EGMs
            bipolar_EGMs = file_content['bipolar'][map_index]
            print(f"{filename}: map_name='{map_name}', shape={bipolar_EGMs.shape}")

# Now bipolar_EGMs can be used for further analysis
# For the forecasting problem use 1000 samples and try to predict the next 250 samples

# Let me know if you need further assistance! grios@ing.uc3m.es