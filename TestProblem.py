import csv
from datetime import datetime


input_file = "TestData.csv"
total_resale_value_txt = "total_resale_value.txt"
resale_value_by_item_txt = "resale_value_by_item.txt"

# define a function to clean the data
def clean_data(item):
    item["Resale Value"] = float(item["Resale Value"].replace("$", "").replace(",", ""))
    item["Resale Per Ticket"] = float(item["Resale Per Ticket"].replace("$", ""))
    item["Resale Date"] = datetime.strptime(item["Resale Date"], "%m/%d/%Y")
    return item

# read the input CSV file and clean the data
with open(input_file, "r") as f:
    reader = csv.DictReader(f)
    data = [clean_data(item) for item in reader]

# compute the total resale value
total_resale_value = sum(item["Resale Value"] for item in data)


resale_value_by_item = {}
for item in data:
    item_name = item["Item"]
    resale_value = item["Resale Value"]
    resale_value_by_item[item_name] = resale_value_by_item.get(item_name, 0) + resale_value



total_resale_value = round(total_resale_value, 2)
total_resale_value_txt = open(total_resale_value_txt, "w")
total_resale_value_txt.write(f"${total_resale_value}")
total_resale_value_txt.close()


resale_value_by_item_txt = open(resale_value_by_item_txt, "w")
for item, resale_value in resale_value_by_item.items():
    resale_value_by_item_txt.write(f"{item}: ${round(resale_value, 2)}\n")
resale_value_by_item_txt.close()