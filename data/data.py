import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("cereal.csv")
# print(df.head(5))

data = df[["name", "mfr"]]
x = ["kellogs", "general Mills", "post", "quaker oats", "ralstone purina", "nabisco", "american home food products"]
y = data["mfr"].value_counts()
df2 = df["fiber"].mean()
print("Average fiber in all cereal is: " + str(df2))

# fig = plt.figure(figsize = (10, 5))

plt.bar(x, y)
plt.show()


