import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
dataf = pd.get_dummies(data['whoAmI'])
print(dataf)

print("---------------------------------------------------------------")

a = 20
print("   human  robot")
for i in range(a):
    if lst[i] == "human":
        print(i, "    True  False")
    else:
        print(i, "   False  True")

print("---------------------------------------------------------------")
a = 20
lsth = []
lstr = []
for i in range(a):
     if lst[i] == "human":
         lsth.append('True')
         lstr.append('False')
     else:
         lsth.append('False')
         lstr.append('True')
df = pd.DataFrame({'human': lsth, 'robot': lstr})
print(df)

print("---------------------------------------------------------------")

