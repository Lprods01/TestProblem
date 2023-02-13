import pandas as pd


def ResaleValue(sales_df):
    total_RV = 0
    for i in sales_df["Resale Value"]:
        try:
            Resale_Value = float(i[1:])
            total_RV = total_RV + Resale_Value
        except ValueError as e:
            if "," in i:
                i = i.replace(",", "")
            Resale_Value = float(i[1:])
            total_RV = total_RV + Resale_Value
    return total_RV


def ItemizedResaleValue(sales_df):
    RVList = []
    for item in sales_df.groupby(["Item"]):
        newRV = 0
        item_df = item[1]
        for i in item_df["Resale Value"]:
            try:
                RV_PerItem = float(i[1:])
                newRV = newRV + RV_PerItem
            except ValueError as e:
                if "," in i:
                    i = i.replace(",", "")
                RV_PerItem = float(i[1:])
                newRV = newRV + RV_PerItem
        RVList.append((item[0], newRV))
    return RVList


def main():
    sales_df = pd.read_csv("TestData.csv")
    with open("TotalResaleValue.txt", "w") as f:
        f.write("Total resale value is: {:.2f}".format(ResaleValue(sales_df)))

    with open("ItemResaleValue.txt", "w") as f2:
        for values in ItemizedResaleValue(sales_df):
            f2.write("Item {}: ${}\n".format(values[0], round(values[1], 2)))


if __name__ == "__main__":
    main()