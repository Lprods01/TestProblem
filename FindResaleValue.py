import pandas as pd

def ResaleValueHandler(sales, case = "total"):
#Itemized Resale
    if case == "itemized":
        totalslist = []
        for item in sales.groupby(["Item"]):
            itemRV = 0
            itemtype = item[1]
            for x in itemtype["Resale Value"]:
                #Remove Commas
                if "," in x:
                    x = x.replace(",","")
                record = float(x[1:])
                itemRV += record
            totalslist.append((item[0], itemRV))
        return  totalslist
#Total Resale
    elif case == "total":
        totalresale = 0
        for sale in sales["Resale Value"]:
            #Remove Commas
            if "," in sale:
                sale = sale.replace(",","")
            record = float(sale[1:])
            totalresale += record
        return totalresale

def main():
    sales = pd.read_csv("TestData.csv")
    RVtotalout = "TotalResale.txt"
    RVitemout = "ResaleByItem.txt"

# Total Resale Value
    with open(RVtotalout, "w+") as out1:
        out1.write("The Total Resale Value is:${:.2f}".format(ResaleValueHandler(sales)))
    print("{} Output Successfully".format(RVtotalout))

# Resale Value By Item
    with open(RVitemout, "w+") as out2:
       for item in ResaleValueHandler(sales, "itemized"):
        out2.write("Item: {} Resale Value: ${:.2f}\n".format(item[0],item[1]))
    print("{} Output Successfully".format(RVitemout))

if __name__ == "__main__":
    main()