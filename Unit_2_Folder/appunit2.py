import csv

soda_companies = [
    {
        "name": "Coca Cola",
        "founded": 1874,
        "net_worth": 15.5
    },
{
    "name": "Pepsi",
    "founded": 1930,
    "net_worth": 20.6
    },
    {
     "name": "Dr. Pepper",
    "founded": 1975,
    "net_worth": 3.75
    },
    {
    "name": "Dr. Pibb",
    "founded": 1996,
    "net_worth": 1.25
    }
]

with open("test.csv", "w") as f:
    reader = csv.DictReader(f)

for company in reader: