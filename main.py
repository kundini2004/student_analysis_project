from analysis import load_data, calculate_averages, assign_grades
from visualization import plot_subject_wise, plot_grade_distribution

df = load_data("data/students.csv")
df = calculate_averages(df)
df = assign_grades(df)

plot_subject_wise(df)
plot_grade_distribution(df)
