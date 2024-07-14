import csv

row_list = [["Tom and Jerry", "Fred Quimby", 4],
            ["Breakfast at Tiffany's", "Blake Edwards"],
            ["Casablanca", "Michael Curtiz", 2],
            ["The Sound of Music", "Robert Wise", 1],
            ["Gone with the Wind", "Victor Fleming", 3]]

with open('Videolibrary.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)