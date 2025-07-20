import seaborn as sns
import matplotlib.pyplot as plt

def plot_subject_wise(df):
    subjects = df.columns[1:5]
    for subject in subjects:
        sns.barplot(x='Name', y=subject, data=df)
        plt.title(f"{subject} Scores")
        plt.show()

def plot_grade_distribution(df):
    sns.countplot(x='Grade', data=df)
    plt.title("Grade Distribution")
    plt.show()
