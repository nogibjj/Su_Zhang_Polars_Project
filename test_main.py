from main import load_dataset_pl, describe_stat, group_by, build_histogram
import pandas as pd
from pyinstrument import Profiler

data = load_dataset_pl("healthcare_dataset.csv")


def test_describe_stat():
    """testing out if describe_stat function works"""
    output = describe_stat(data, ["Age", "Billing Amount"])
    assert output is not None


def test_group_by():
    """testing out if group_by function works"""
    output_grouby = group_by(data, "Blood Type")
    assert output_grouby is not None


def test_build_histogram():
    """testing out if build_histogram works"""
    output_hist = build_histogram(data)
    assert output_hist is None


# Define loading dataset function using pandas:
def load_dataset_pd(dataset):
    df_pd = pd.read_csv(dataset)
    return df_pd


# Use Profiler to compare pandas and polars
with Profiler(interval=0.1) as profiler:
    check_pl = "healthcare_dataset.csv"
    df = load_dataset_pl(check_pl)
    print(df.shape)
    print(df["Age"].mean())
    print(df["Age"].median())

print("-------Below is summary profile for Polars--------")
profiler.print()

with Profiler(interval=0.1) as profiler:
    check_pd = "healthcare_dataset.csv"
    df = load_dataset_pd(check_pd)
    print(df.shape)
    print(df["Age"].mean())
    print(df["Age"].median())

print("-------Below is summary profile for Pandas--------")
profiler.print()


if __name__ == "__main__":
    test_describe_stat()
    test_group_by()
    test_build_histogram()
