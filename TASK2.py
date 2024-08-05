import pandas as pd
data = pd.read_csv('/Users/Sanath/Downloads/Titanic-Dataset.csv')
data.head()
data.info()
data.describe()
missing_values = data.isnull().sum()
print(missing_values)
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop(columns=['Cabin'], inplace=True)
print(data.isnull().sum())

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='Survived', data=data)
plt.title('Survival Distribution')
plt.show()

sns.countplot(x='Pclass', data=data)
plt.title('Passenger Class Distribution')
plt.show()

sns.countplot(x='Sex', data=data)
plt.title('Gender Distribution')
plt.show()

sns.countplot(x='Embarked', data=data)
plt.title('Port of Embarkation Distribution')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data['Fare'], bins=30, kde=True)
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

sns.catplot(x='Sex', hue='Survived', kind='count', data=data)
plt.title('Survival Rate by Gender')
plt.show()

sns.catplot(x='Pclass', hue='Survived', kind='count', data=data)
plt.title('Survival Rate by Passenger Class')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data[data['Survived'] == 1]['Age'], bins=30, kde=True, color='green', label='Survived')
sns.histplot(data[data['Survived'] == 0]['Age'], bins=30, kde=True, color='red', label='Not Survived')
plt.title('Survival Rate by Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend()
plt.show()
