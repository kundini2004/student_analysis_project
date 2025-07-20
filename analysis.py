import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_averages(df):
    df['Total'] = df.iloc[:, 1:].sum(axis=1)
    df['Average'] = df['Total'] / (df.shape[1] - 1)
    return df

def assign_grades(df):
    def grade(avg):
        if avg >= 90: return 'A'
        elif avg >= 75: return 'B'
        elif avg >= 60: return 'C'
        elif avg >= 50: return 'D'
        else: return 'F'
    df['Grade'] = df['Average'].apply(grade)
    return df
