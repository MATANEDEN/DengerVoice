import csv


def write_to_csv(list_text):


    with open('testing_csv\our_test.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(list_text)
        writer.writerow([])
        writer.writerow(['bed', 'cat', 'down', 'eight', 'five', 'four', 'go', 'happy', 'house', 'left', 'nine', 'no', 'off', 'on', 'one', 'seven', 'sheila', 'six', 'stop', 'three', 'two', 'up', 'wow', 'yes', 'zero'])

