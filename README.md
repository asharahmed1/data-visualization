# data-visualization
A personal project for the visualization of data using Pandas &amp; Seaborn (Python libs)

# The Assignment
Your task is to help your client gain a better understanding of their customer data by creating visualizations using Pandas and Seaborn. To begin, you will need to read in the original CSV file provided with the assignment.

First, extract the data series for Salary and Age, and compute the mean salary and median age.

Next, create univariate plots for Age and Dependents, fixing any data errors with Seaborn. For the Age plot, determine the number of bins required for a bin width of 5, and for the Dependents plot, use Seaborn to correct any errors.

Then, create multivariate plots for Commuted distance against Salary, Age against Salary, and Age against Salary conditioned by Dependents.

Lastly, your client has requested the ability to save the plots you've produced. Include a Notebook cell that enables them to do so.

# My proposed solution
Before proceeding to the tasks, I will assume that the dataset is in CSV format and is located in the same directory as the Jupyter Notebook you are working on. 

Let's start by importing the libs

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

Now, let's load the dataset into a pandas DataFrame object and preview the first few rows.

```python
df = pd.read_csv("users.csv")
df.head()
```
 Obtain the Data Series for Salary, and Age, and calculate the following:

a. Mean Salary

```python
mean_salary = df["salary"].mean()
print("Mean Salary:", mean_salary)
```
b. Median Age

```python
median_age = df["age"].median()
print("Median Age:", median_age)
```
 Perform univariate plots of the following data attributes:

a. Age, calculating how many bins would be required for a bin_width of 5.

```python

# calculate number of bins
bin_width = 5
num_bins = int((df["age"].max() - df["age"].min()) / bin_width)
print("Number of bins:", num_bins)

# plot histogram
sns.histplot(df["age"], bins=num_bins)
plt.title("Age Distribution")
plt.show()
```
b. Dependents, fixing data errors with seaborn itself.

```python
# fix data errors using seaborn
sns.boxplot(df["dependents"])
plt.title("Dependents Distribution")
plt.show()
```
c. Age (of default bins), conditioned on Marital Status

```python
# plot histogram with conditioned variable
sns.histplot(data=df, x="age", bins="auto", hue="marital_status")
plt.title("Age Distribution by Marital Status")
plt.show()
```
 Perform multivariate plots with the following data attributes:

a. Commuted distance against salary.

```python
sns.scatterplot(data=df, x="commute_distance", y="salary")
plt.title("Commuted Distance vs Salary")
plt.show()
```
b. Age against Salary

```python
sns.scatterplot(data=df, x="age", y="salary")
plt.title("Age vs Salary")
plt.show()
```
c. Age against Salary conditioned by Dependents

```python
sns.scatterplot(data=df, x="age", y="salary", hue="dependents")
plt.title("Age vs Salary by Dependents")
plt.show()
```
Your client would like the ability to save the plots which you have produced. Provide a Notebook cell which can do this.

```python
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
```
This code will save the plots in the same directory as the Jupyter.

