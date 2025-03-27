# File Name: chart.py
# Student Name: Colton Ramsey, Lucas Iceman, Zach Bell
# email: ramseyc6@mail.uc.edu, icemanlc@mail.uc.edu, bellzj@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 03/25/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Modify a VS Python project to add some data visualization.
# Brief Description of what this module does: This module pops up a chart in the console window
# the image of Blastoise the pokemon.
# Citations: ChatGPT to understand how to show an image.
# Anything else that's relevant: None

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filename):
    filepath = 'dataPackage/MMLU/data/business_ethics_test.csv'
    df = pd.read_csv(filepath, encoding='utf-8')
    return df

def clean_data(df):
    df.columns = ['Question', 'Option_A', 'Option_B', 'Option_C', 'Option_D', 'Correct_Answer']
    return df

def plot_answer_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(x=df['Correct_Answer'], palette='viridis')
    plt.xlabel("Correct Answer Choices")
    plt.ylabel("Frequency")
    plt.title("Distribution of Correct Answers")
    plt.show()

def main():
    filename = 'business_ethics_test.csv'
    df = load_data(filename)
    df = clean_data(df)
    plot_answer_distribution(df)

if __name__ == "__main__":
    main()