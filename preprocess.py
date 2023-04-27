import pandas as pd

# Step 1: Load the user data  
# Prompt the user to enter the file name/path
file_name = input("Enter the file name/path: ")
df = pd.DataFrame()
filename = "/Users/sushama/Desktop/Sushama/UIUC/Course_Content/Spring23/Independent_Study/Datasets/dashboard_sample/DSTL/" + str(file_name)
print(filename)

# Determine the file extension and load the file into a pandas dataframe
if filename.endswith('.csv'):
    df = pd.read_csv(filename)
elif file_name.endswith('.xlsx') or filename.endswith('.xls'):
    df = pd.read_excel(filename)
else:
    print("Invalid file type. Please enter a CSV or Excel file.")

# The following two statements would be a part of the Dashboard or the website when it is developed so these prompts will either be 
# added as html components under Dash layout or through javascript. For now, it's here to understand the flow. 
print("This is your dataset: \n", df.head(5))

# Step 2: Data cleaning
cleaning = input("\n Please type 'auto' for automatic data preparation (Null value rows will be deleted and columns will be categorized into categorical and numerical) or type 'manual' for manually selecting among your data cleaning options: \n")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def auto(df):
    df = df.dropna()
    numerical = []
    categorical = []
    rec = []
    for column in df.columns:
        if is_number(df[column][0]) != True:
            categorical.append(column)
        elif df[column].nunique() < 0.1*(len(df)):
            categorical.append(column)
            rec.append(column)
        else:
            numerical.append(column)

    return df, numerical, categorical

def clean_module(df): 
    clean = input("Let's begin with data cleaning.\n Please type 'delete' to delete the rows containing null values, 'zero' to replace the null values with zero or 'mean' to fill the null values with the average value for that column: \n")
    if clean.lower() == "delete":
        df = df.dropna()
    elif clean.lower() == "zero":
        df = df.fillna(0)
    elif clean.lower() == "mean":
        df = df.fillna(df.mean())
    else:
        print("Select a valid input")
        clean_module(df)
    return df

def categorize(df):
    numerical = []
    categorical = []
    print("Enter 'numerical' if the following attribute contains only quantitative number inputs. Enter 'categorical' if the attribute is qualitative. Type 'column' to see the column preview. \n")
    for i in df.columns.tolist():
        print(i)
        type = input(": ")
        if type.lower() == "numerical":
            numerical.append(i)
        elif type.lower() == "categorical":
            categorical.append(i)
        else:
            input("Invalid input. Please enter either 'numerical' or 'categorical'.")
    return numerical, categorical

if cleaning.lower() == "auto":
    df, numerical, categorical = auto(df)
    
elif cleaning.lower() == "manual":    
    # Get an input to understand what kind of cleaning the user prefers. They can select auto and get 
    df = clean_module(df)
    numerical, categorical = categorize(df)

else:
    print("\nPlease enter a valid input. \n")

print("Numerical: ", numerical)
print("Categorical: ", categorical)
# print("Please ")



