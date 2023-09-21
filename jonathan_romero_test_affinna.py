import pandas as pd

if __name__ == "__main__":
    file = pd.read_csv('TestData.csv')
    
    #cleaning up the resale value column ( taking out the $ sign and commas)
    file['Resale Value'] = file['Resale Value'].str.replace('$', '').str.replace(',', '').astype(float)
    
    #calculating the total resale value
    resale_value_total = file['Resale Value'].sum()
    
    #calculating the resale value by item
    resale_value_by_item = file.groupby('Item')['Resale Value'].sum().reset_index()
    
    #turning the resale value total into a dataframe
    resale_value_total = pd.DataFrame({'Resale Value Total': [resale_value_total]})
    
    #exporting both answers to csv files
    resale_value_total.to_csv('ResaleValueTotal.csv', index=False)
    resale_value_by_item.to_csv('ResaleValueByItem.csv', index=False)