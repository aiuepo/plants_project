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

#中央値
median_Length=df["Length"].median()
print(f"中央値: {median_Length}")

#最小値最大値
min_Length=df["Length"].min()
max_Length=df["Length"].max()
print(f"最小値: {min_Length}")
print(f"最大値: {max_Length}")

#分散
var_length=df["Length"].var()
print(f"分散: {var_length}")


#四分位数
q1=df["Length"].quantile(0.25)
q3=df["Length"].quantile(0.75)
print(f"第一四分位数: {q1}")
print(f"第一四分位数: {q3}")
print(f"IQR: {q3 - q1}")