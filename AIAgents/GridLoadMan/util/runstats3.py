import pandas as pd


def is_float(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False


# Read the CSV file
# Assuming the CSV file has columns: 'datetime', 'price', 'load'
df = pd.read_csv('stats.csv', parse_dates=['datetime'])

# Set datetime as the index
df.set_index('datetime', inplace=True)
# Iterating over rows using iterrows()

# Iterating over rows using iterrows()
for index, row in df.iterrows():
    print(f"Row Index: {index}")
    
    # Iterating through columns in the row
    for column_name, value in row.items():
        print(f"Column: {column_name}, Value: {value}")
        if column_name == "price":
            if (is_float(value)):
                if(float(value) > 30.0):
                    print("price > 30")
        if column_name == "price.1":
            if (is_float(value)):
                if(float(value) > 30.0):
                    print("price.1 > 30")
        if column_name == "price.2":
            if (is_float(value)):
                if(float(value) > 30.0):
                    print("price.2 > 30")
        if column_name == "price.3":
            if (is_float(value)):
                if(float(value) > 30.0):
                    print("price.3 > 30")
        if column_name == "load":
            if (is_float(value)):
                if(float(value) > 30.0):
                    print("load > 30")
        if column_name == "load.1":
            if (is_float(value)):
                if(float(value) > 30.0):
                    print("load.1 > 30")
        if column_name == "load.2":
            if (is_float(value)):
                if(float(value) > 30.0):
                    print("load.2 > 30")
        if column_name == "load.3":
            if (is_float(value)):
                if(float(value) > 30.0):
                    print("load.3 > 30")
    
    # Add a separator for readability between rows
    print("---")
