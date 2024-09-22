import polars as pl
import matplotlib.pyplot as plt

dataframe = None


# Load dataset from csv file using Polars
def load_dataset_pl(dataset):
    df = pl.read_csv(dataset)
    return df


# print the head of the datasets to showcase what variables do the dataset include
def print_head(df):
    data_head = df.head()
    print(data_head)
    return data_head


# describe the dataset's specific columns
def describe_stat(df, col_list):
    return df.select(col_list).describe()


# use value counts to summary the counts of categorical variables
def group_by(df, column_name):
    return df.select(pl.col(column_name).value_counts())


# create a histogram of 'Billing Amount' column in healthcare dataset
def build_histogram(df):
    plt.hist(
        df["Billing Amount"],
        bins=20,
        edgecolor="white",
    )
    plt.xlabel("Billing Amount")
    plt.ylabel("Frequency")
    plt.title("Billing Amount Histogram")
    plt.savefig("Billing_Amount_Hist.png")
    plt.show()


def save_to_markdown():
    describe_df = describe_stat(dataframe, ["Age", "Billing Amount"])
    markdown_table = str(describe_df)
    with open("healthcare_summary.md", "w", encoding="utf-8") as file:
        file.write("Healthcare Dataset Describe:\n")
        file.write(markdown_table)
        file.write("\nHistogram of Billing Amount Distribution\n")
        file.write("![Graph Description](Billing_Amount_Hist.png)")


# main to execute the functions.
if __name__ == "__main__":
    dataframe = load_dataset_pl("healthcare_dataset.csv")
    if dataframe is not None:
        print_head(dataframe)
        print(describe_stat(dataframe, ["Age", "Billing Amount"]))
        print(group_by(dataframe, "Blood Type"))
        print(group_by(dataframe, "Medical Condition"))
        print(group_by(dataframe, "Admission Type"))
        print(group_by(dataframe, "Test Results"))
        build_histogram(dataframe)
        save_to_markdown()
    else:
        print("Dataset was not successfully loaded")
