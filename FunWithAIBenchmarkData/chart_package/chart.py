#chart.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filename):
    # Use the correct file path based on where the file is located
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