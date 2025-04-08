import pandas as pd
import requests
import os
import numpy as np

def make_folders():
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    os.makedirs("src", exist_ok=True)

def read_csv(file_path):
    return pd.read_csv(file_path)

def filter_employees(df):
    return df[df['Age'] > 30]

def calculate_tax(df):
    df['salary_after_tax'] = df['Salary'].map(lambda x: x * 0.9)
    return df

def write_csv(df, output_path):
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    make_folders()
    input_file = 'input/data.csv'
    output_file = 'output/employees_after_tax.csv'

    df = read_csv(input_file)
    filtered = filter_employees(df)
    taxed = calculate_tax(filtered)
    write_csv(taxed, output_file)
