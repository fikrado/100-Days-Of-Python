import pandas as pd

data = pd.read_csv("squarl.csv")
sq = len(data[data["Primary Fur Color"] == "Gray"])
print(sq)
sq1 = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(sq1)
sq2 = len(data[data["Primary Fur Color"] == "Black"])
print(sq2)

data_dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [sq, sq1, sq2]

}
df = pd.DataFrame(data_dic)
df.to_csv("new.csv")




