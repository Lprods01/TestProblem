# %% [markdown]
# ###Preprocessing

# %%
import pandas as pd
import numpy as np
import warnings

# %%
my_data = pd.read_csv("TestData.csv")

# %%
my_data.head()

# %%
my_data.isna().sum()

# %%
my_data.rename(columns={'Resale Value': 'Resale Value ($)', 'Resale Per Ticket': 'Resale Per Ticket ($)', 'Resale Difference': 'Resale Difference ($)'}, inplace=True)

# %%
my_data.dtypes

# %%
my_data.head()

# %%
warnings.filterwarnings("ignore", message="The default value of regex will change from True to False in a future version.", category=FutureWarning)
my_data["Resale Value ($)"] = my_data["Resale Value ($)"].str.replace('$', '')
my_data["Resale Per Ticket ($)"] = my_data["Resale Per Ticket ($)"].str.replace('$', '')
my_data["Resale Difference ($)"] = my_data["Resale Difference ($)"].str.replace('$', '')

# %%
my_data['Resale Value ($)'] = my_data['Resale Value ($)'].str.replace(',', '').astype(float)
my_data["Resale Per Ticket ($)"] = my_data["Resale Per Ticket ($)"].str.replace(',', '').astype(float)
my_data["Resale Difference ($)"] = my_data["Resale Difference ($)"].str.replace(',', '').astype(float)

# %%
my_data.head()

# %%
my_data['Resale Date'] = pd.to_datetime(my_data['Resale Date'], format='%m/%d/%Y')

# %%
my_data.head()

# %%
my_data.dtypes

# %% [markdown]
# ###Statistical Summary

# %%
my_data.describe()

# %% [markdown]
# ###Dataframe Summary

# %%
my_data.info()

# %% [markdown]
# ###Question 1: Total Resale Value

# %%
total_resale_value = my_data['Resale Value ($)'].sum()
print("Total Resale Value: $", total_resale_value,)

# %% [markdown]
# ###Question 2: Total Resale Value by Item

# %%
total_resale_value_by_item = my_data.groupby('Item')['Resale Value ($)'].sum()
print("Total Resale Value by Item: ", total_resale_value_by_item)

# %%


