import csv
import os

dir = "/var/Datasets/originali/RECOLA/RECOLA-Audio-recordings"

with open('data_file.csv', mode='w') as data_file:
	data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	data_writer.writerow(['file'])

	sorted_listdir = sorted(os.listdir(dir))
	for path in sorted_listdir:
		full_path = os.path.join(dir, path)
		if os.path.isfile(full_path):
			data_writer.writerow([full_path])


