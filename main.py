import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
uploaded = files.upload()
filename = list(uploaded..keys())[0]
df = pd.read_csv("country_vaccinations.csv")
df.head(10)
df.isnull().any()
subset = df.iloc[:5200, :]
plt.figure(figsize=(12, 8))