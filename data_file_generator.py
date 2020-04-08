import csv
import os

dirAudio = "/var/Datasets/originali/RECOLA/RECOLA-Audio-recordings"
dirArousal = "/var/Datasets/originali/RECOLA/RECOLA-Annotation/emotional_behaviour/arousal"
dirValence = "/var/Datasets/originali/RECOLA/RECOLA-Annotation/emotional_behaviour/valence"
dirLabels = "labels"



"""
	
	"""

sorted_listAudio = sorted(os.listdir(dirAudio))
sorted_listArousal = sorted(os.listdir(dirArousal))
sorted_listValence = sorted(os.listdir(dirValence))

if (len(sorted_listAudio) != len(sorted_listValence)) or (len(sorted_listAudio) != len(sorted_listArousal)) or (len(sorted_listArousal) != len(sorted_listValence)):
	print("FATAL: different number of files in audio, valence and arousal directory")
	exit()

# WRITING LABELS FILES

for path in sorted_listArousal:
	times = []
	valence = []
	arousal = []

	with open(os.path.join(dirArousal, path)) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=';')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
			else:
				times.append(row[0])
				arousal.append((float(row[1]) + float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6]))/6.0)

	with open(os.path.join(dirValence, path)) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=';')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
			else:
				valence.append((float(row[1]) + float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6]))/6.0)

	with open(os.path.join(dirLabels, path ), mode = 'w') as label_file:
		data_writer = csv.writer(label_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

		data_writer.writerow(['time', 'arousal', 'valence'])

		for i in range(len(times)):
			data_writer.writerow([times[i], arousal[i], valence[i]])


# WRITING DATA FILE
sorted_listLabels = sorted(os.listdir(dirLabels))

with open('data_file.csv', mode='w') as data_file:
	data_writer = csv.writer(data_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	data_writer.writerow(['file', 'label'])

	#print(len(sorted_listAudio))
	for path in sorted_listAudio:
		full_path_audio = os.path.join(dirAudio, path)
		full_path_labels = os.path.join(dirLabels, path.split('.')[0] + '.csv')
		#print(full_path_audio)
		#print(full_path_labels)
		if os.path.isfile(full_path_audio) and os.path.isfile(full_path_labels):
			data_writer.writerow([full_path_audio, full_path_labels])




