import os
import csv

# Define the base directory
base_dir = 'data'

labels_dict = {
    'barszcz czerwony' : 1,
    'bigos' : 2,
    'kutia' : 3,
    'makowiec' : 4,
    'pierniki' : 5,
    'pierogi' : 6,
    'sernik' : 7,
    'zupa grzybowa' : 8,
}

# Create or overwrite the labels.csv file
with open('labels.csv', mode='w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['filename', 'label'])

    # Walk through the base directory
    for root, dirs, files in os.walk(base_dir):
        # Determine the class from the folder name
        class_name = os.path.basename(root)

        # Skip the base directory itself
        if class_name == os.path.basename(base_dir):
            continue

        # Rename files and write to CSV
        for i, file in enumerate(files, start=1):
            # Define the new file name
            new_name = f"{class_name.replace(' ','_')}_img_number_{i}{os.path.splitext(file)[1]}"
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_name)

            # Rename the file
            if old_path != new_path:
                os.rename(old_path, new_path)
            print(labels_dict[class_name])
            # Write the file name and class to the CSV file
            csvwriter.writerow([new_name, labels_dict[class_name]])

print("Renaming complete. Labels saved to labels.csv.")
