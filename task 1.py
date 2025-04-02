# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 13:10:01 2025

@author: Lenovo
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset properly
df = pd.read_csv(
    r"C:\Users\Lenovo\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_13582\API_SP.POP.TOTL_DS2_en_csv_v2_13582.csv",
    skiprows=4,  # Skip metadata rows
    encoding="latin1"  # Use an alternative encoding
)

# Select 2023 population data and drop NaNs
if '2023' in df.columns:
    population_2023 = df[['Country Name', '2023']].dropna()

    # Convert population to numeric
    population_2023['2023'] = pd.to_numeric(population_2023['2023'], errors='coerce')

    # Plot histogram
    plt.figure(figsize=(10, 6))
    plt.hist(population_2023['2023'].dropna(), bins=30, edgecolor='black', alpha=0.7)
    plt.xlabel('Population in 2023')
    plt.ylabel('Number of Countries')
    plt.title('Distribution of Population Across Countries in 2023')
    plt.xscale('log')  # Log scale to handle large differences in population sizes
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)

    # Show the plot
    plt.show()