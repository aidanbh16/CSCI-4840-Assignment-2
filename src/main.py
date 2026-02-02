import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel("data/tips.xlsx")
df = pd.DataFrame(data)

def scatterplot(df):
    x = np.array(df["total_bill"])
    y = np.array(df["tip"])
    size = np.array(df["size"])

    fig, ax = plt.subplots()
    ax.scatter(x, y, s=size**2, c="blue")
    ax.set_xlabel("Total Bill")
    ax.set_ylabel("Tips")
    ax.set_title("Total Bill vs Tips")
    plt.show()

def barplot(df):
    males = df.loc[df["sex"] == "Male", "tip"].mean()
    females = df.loc[df["sex"] == "Female", "tip"].mean()
    x = ["males", "females"]
    y = np.array([males, females])

    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel("Sexes")
    ax.set_ylabel("Average Tip")
    ax.set_title("Average Tip Grouped by Sex")
    plt.show()

def boxplot(df):
    days = df["day"].unique()
    data = [df.loc[df["day"] == d, "total_bill"] for d in days]

    fig, ax = plt.subplots()
    ax.boxplot(data, labels=days)
    ax.set_xlabel("Days of the Week")
    ax.set_ylabel("Total Bill")
    ax.set_title("Total Bill For Each day")
    plt.show()

boxplot(df)