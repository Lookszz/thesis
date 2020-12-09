import sys
import csv
import os
import re

def main():
    filename = 'laughing_time_test_no10.csv'
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as csvfile:
        headers = ['participants', 'game', 'laughing_time', 'laughing_time_tot']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        directory = r'/home/luuk_janssen/scriptie/laughter-detection/output_06551148780646751832'
        total_laugh_count = 0
        for file in sorted(os.listdir(directory)):
            game = file[21:23]
            file_path = directory+'/'+file
            participants = file[:20]
            #print(file_path)
            laugh_file = open(file_path)
            file_list = []
            for line in laugh_file:
                line = line.strip()
                line = line.replace('"', '')
                file_list.append(line)
            #print(file_list)
            counter = 0
            time = 0 
            for item in file_list:
                counter = counter + 1
                if item == 'laugh':
                    time = time + (int(float(file_list[counter-2])) - int(float(file_list[counter-3])))
                else:
                    pass
            total_laugh_count = total_laugh_count + time
            print(participants, game, time, total_laugh_count)

            writer.writerow({'participants': participants, 'game': game, 'laughing_time': time, 'laughing_time_tot': total_laugh_count})

if __name__ == "__main__":
    main()