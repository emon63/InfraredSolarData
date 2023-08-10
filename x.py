import json
import shutil
import os

# Specify the path to your JSON file
json_file_path = './module-metadata.json'

# Open the JSON file for reading
with open(json_file_path, 'r') as json_file:
    # Load JSON data from the file
    data = json.load(json_file)
# Now you can work with the 'data' variable which contains the JSON content

anomaly_array=[]
for key, value in data.items():
    anomaly = value["anomaly_class"]
    if anomaly not in anomaly_array:
        anomaly_array.append(anomaly)
print(anomaly_array)
for anomaly in anomaly_array:
    path='./'+anomaly
    print(path)
    os.mkdir(path)
for key, value in data.items():
    anomaly_class = value["anomaly_class"]
    image_filepath = value.get("image_filepath")
    image_filepath='./'+image_filepath
    destination_path = './'+anomaly_class
    shutil.copy(image_filepath, destination_path)
    print("Copied:", key)
