import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("acw_user_data.csv")
df.head()

mean_salary = df["Yearly Salary (GBP)"].mean()
print("Mean Salary:", mean_salary)

median_age = df["Age (Years)"].median()
print("Median Age:", median_age)

# calculate number of bins
bin_width = 5
num_bins = int((df["Age (Years)"].max() - df["Age (Years)"].min()) / bin_width)
print("Number of bins:", num_bins)

# plot histogram
sns.histplot(df["Age (Years)"], bins=num_bins)
plt.title("Age Distribution")
plt.show()

# fix data errors using seaborn
sns.boxplot(df["Dependants"])
plt.title("Dependents Distribution")
plt.show()

# plot histogram with conditioned variable
sns.histplot(data=df, x="Age (Years)", bins="auto", hue="Marital Status")
plt.title("Age Distribution by Marital Status")
plt.show()

sns.scatterplot(data=df, x="Distance Commuted to Work (miles)", y="Yearly Salary (GBP)")
plt.title("Commuted Distance vs Salary")
plt.show()

sns.scatterplot(data=df, x="Age (Years)", y="Yearly Salary (GBP)")
plt.title("Age vs Salary")
plt.show()

sns.scatterplot(data=df, x="Age (Years)", y="Yearly Salary (GBP)", hue="Dependants")
plt.title("Age vs Salary by Dependents")
plt.show()

# save plots to file
sns.histplot(df["age"], bins=num_bins)
plt.title("Age Distribution")
plt.savefig("age_distribution.png")

sns.boxplot(df["dependents"])
plt.title("Dependents Distribution")
plt.savefig("dependents_distribution.png")

sns.histplot(data=df, x="age", bins="auto", hue="marital_status")
plt.title("Age Distribution by Marital Status")
plt.savefig("age_distribution_by_marital_status.png")

sns.scatterplot(data=df, x="commute_distance", y="salary")
plt.title("Commuted Distance vs Salary")
plt.savefig("commuted_distance_vs_salary.png")

sns.scatterplot(data=df, x="age", y="salary")
plt.title("Age vs Salary")
plt.savefig("age_vs_salary.png")

sns.scatterplot(data=df, x="age", y="salary", hue="dependents")
plt.title("Age vs Salary by Dependents")
plt.savefig("age_vs_salary_by_dependents.png")