import pandas as pd


def is_float(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False
# Calibrate the game level and duration

# Read the CSV file
# Assuming the CSV file has columns: 'datetime', 'price', 'load'
df_stats = pd.read_csv('..\\data\\LMP_LOAD_STATS.csv', parse_dates=['datetime'])
df_data = pd.read_csv('..\\data\\LMP_LOAD_META.csv', parse_dates=['datetime'])
#df = pd.read_csv('stats.csv', parse_dates=['datetime'])

# Set datetime as the index
df_stats.set_index('datetime', inplace=True)
df_stats.index = df_stats.index.date

df_data.set_index('datetime', inplace=True)
# Iterating over rows using iterrows()
bronze_games = 0
bronze_price = 200
bronze_price_std = 50

silver_games = 0
silver_price = 225
silver_price_std = 25

gold_games_price = 0
gold_games_load = 0

#250/150000

gold_price = 250
gold_price_std = 10

bronze_load = 130000
bronze_load_std = 15000

silver_load = 140000
silver_load_std = 18000

gold_load=150000
gold_load_std = 20000

#my_datetime = ""
my_lastday = ""
# Iterating over rows using iterrows()
for index, row in df_stats.iterrows():
    #print(f"Row Index: {index}")
    my_datetime = index
     # Iterating through columns in the row
    do_std = False
    for column_name, value in row.items():
        #print(f"Column: {column_name}, Value: {value}")

        """
        if column_name == "price_mean":
            if (is_float(value)):
                if(float(value) > gold_price):
                    print("gold_price at " + str(my_datetime))
                elif (float(value) > silver_price):
                    print("silver_price at " + str(my_datetime))
                elif (float(value) > bronze_price):
                    print("bronze_price at " + str(my_datetime))
                
        if column_name == "price_min":
            if (is_float(value)):
                if(float(value) < 0.0):
                    print("price_min < 00 at " + str(my_datetime))
        """
        if column_name == "price_max":
            if (is_float(value)):
                if(float(value) > gold_price):
                    if my_lastday != my_datetime:
                        my_lastday = my_datetime
                        gold_games_price = gold_games_price + 1
                        print("alert gold_price at " + str(my_datetime))
                        std = row["price_std"]
                        mean = row["price_mean"]
                        print("alert gold_price std " + str(std) + " " + str(mean))
                        do_std = True
                    else:
                        pass
                elif (float(value) > silver_price):
                    #print("silver_price at " + str(my_datetime))
                    silver_games = silver_games + 1
                elif (float(value) > bronze_price):
                    #print("bronze_price at " + str(my_datetime))
                    bronze_games = bronze_games + 1

"""
        if do_std == True:
            if column_name == "price_std":
                if (is_float(value)):
                    if(float(value) > 0.0):
                        pass
                        print("alert gold_price_std: " + str(value))
                    elif (float(value) > silver_price_std):
                        #print("silver_price_std at " + str(my_datetime))
                        silver_games = silver_games + 1
                    elif (float(value) > bronze_price_std):
                        #print("bronze_price_std at " + str(my_datetime))
                        bronze_games = bronze_games + 1
            do_std = False
"""
# Add a separator for readability between rows
print("---")

my_lastday = ""


for index, row in df_stats.iterrows():
    my_datetime = index
     #print(f"Row Index: {index}")
    # Iterating through columns in the row

    do_std = False
    for column_name, value in row.items():
       # print(f"Column: {column_name}, Value: {value}")
        """
        if column_name == "load_mean":
            if (is_float(value)):
                if(float(value) > 120000.0):
                    print("load_mean > 120000 at " + str(my_datetime))
        if column_name == "load_min":
            if (is_float(value)):
                if(float(value) > 100000.0):
                    print("load_min > 100000 at " + str(my_datetime))
        """
        
        if column_name == "load_max":
            if (is_float(value)):
                if(float(value) > gold_load):
                    if my_lastday != my_datetime:
                        my_lastday = my_datetime
                        gold_games_load = gold_games_load + 1
                        print("alert gold_load at " + str(my_datetime))
                        std = row["price_std"]
                        mean = row["price_mean"]
                        print("alert gold_load std " + str(std) + " " + str(mean))
                        do_std = True
            elif (float(value) > silver_load):
                silver_games = silver_games + 1
                #print("silver_load at " + str(my_datetime))
            elif (float(value) > bronze_load):
                #print("bronze_load at " + str(my_datetime))
                bronze_games = bronze_games + 1

"""
        if do_std == True:
            if column_name == "load_std":
                if (is_float(value)):
                    if(float(value) > 0.0):
                        print("alert gold_load_std on " + str(my_datetime))
                        #gold_games = gold_games + 1
                        pass
                    elif (float(value) > silver_load_std):
                        #print("silver_load_std at " + str(my_datetime))
                        silver_games = silver_games + 1
                    elif (float(value) > bronze_load_std):
                        #print("bronze_load_std at " + str(my_datetime))
                        bronze_games = bronze_games + 1
            do_std = False
"""
    # Add a separator for readability between rows
    #print("---")

print ("gold_games_price = " + str(gold_games_price))
print ("gold_games_load = " + str(gold_games_load))
print ("silver_games = " + str(silver_games))
print ("bronze_games = " + str(bronze_games))

