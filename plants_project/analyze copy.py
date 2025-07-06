import pandas as pd
import matplotlib.pyplot as plt

#fijiのcsvを読みこむ
df=pd.read_csv("Results.csv")

#データの5行を表示
print(df)

#length列のヒストグラムを作成
plt.hist(df["Length"],bins=5)
plt.xlabel("Length")
plt.ylabel("count")
plt.title("Countlength Histogram")
plt.show()

#Length列平均
mean_Length=df["Length"].mean()
print(f"平均: {mean_Length}")
      
#Length列の標準偏差
std_Length=df["Length"].std()
print(f"標準偏差: {std_Length}")

plt.show()
