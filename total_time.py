import sys
import csv
import os
import re
import librosa

def main():
    filename = 'total_time_test_no10.csv'
    file_exists = os.path.isfile(filename)
    with open(filename, 'a+', newline='') as csvfile:
        headers = ['participants', 'game', 'time', 'total_time', 'alcohol', 'drugs', 'relationship']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        if not file_exists:
            writer.writeheader()

        directory = r'/home/luuk_janssen/scriptie/laughter-detection/input_06551148780646751832'
        total_time = 0
        for file in sorted(os.listdir(directory)):
            file_path = directory+'/'+file
            time = round(librosa.get_duration(filename=file_path))
            game = file[21:23]
            participants = file[:20]
            total_time = total_time + time
            print(participants, game, time, total_time)
            writer.writerow({'participants': participants, 'game': game, 'time': time, 'total_time': total_time,
                            'alcohol': 'NY', 'drugs': 'N', 'relationship': 'NR-male'})


if __name__ == "__main__":
    main()