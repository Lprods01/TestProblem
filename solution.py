import pandas as pd

def readingFile(file_path):
    data = pd.read_csv(file_path, sep=",")
    return data
    
def totalResaleValue(data):
    #remove ALL $ to calculate resale value 
    data["Resale Value"] = data["Resale Value"].replace(["\$", ","],  "", regex=True).astype(float)
    total_resale_value = data["Resale Value"].sum()
    return total_resale_value 

#groups items together to sum up value
def itemResaleValue(data):
    group_value = dict()
    group_value = data.groupby(["Item"])["Resale Value"].sum()
     

    #     if item in group_value.keys():
    #         group_value[item] += data[item]["Resale Value"]
    #     else:
    #         group_value[item] = data[item]["Resale Value"]
    return group_value


#prints all information needed
def displayData(total_sum, item_sum):
    print(f"The total resale value is ${total_sum}")
    print("The total resale value per item are:")
    for key, value in item_sum.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    file = "TestData.csv"
    
    data = readingFile(file)
    total_sum = totalResaleValue(data)
    item_sum = itemResaleValue(data)
    displayData(total_sum, item_sum)
    
    