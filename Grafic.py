from datetime import timedelta
# %matplotlib inline

import matplotlib.pyplot as plt
import pandas as pd
distantion = int(input('дистанция: '))
name = input('класс лодки/ фамилия: ')

lst = [('speed', 'spm', 'watt')]
x_1 = timedelta(minutes=0, seconds=0)
dist = 100
for _ in range(int(distantion / 50)):
    x_0 = input()
    x = timedelta(minutes=int(x_0[0]), seconds=float(x_0[2:6]))

    # x_0[7:13]
    lst.append(
        (str(dist), str(100 / float(str(x - x_1)[5:9])), x_0[7:],
         str(round((100 / float(str(x - x_1)[5:])) ** 3 * 2.8, 1))))
    dist += 100
    x_1 = x

with open('check.csv', 'w') as file:
    for i in lst:
        s = ','.join(i)
        file.write(s)
        file.write('\n')

df = pd.read_csv('D:/Python_Programm/check.csv', encoding='windows-1251', sep=',')
df['ave_speed'] = round(df.speed.mean(), 1)
df['ave_spm'] = df.spm.mean()
df['ave_watt'] = df.watt.mean()

# fig = plt.figure()

fig, ax = plt.subplots(facecolor=(1, .5, 0))

plt.subplot(3,1, 1)
plt.title(f'{name}')
ax.set_facecolor((0.21, 0.21, 0.21))
plt.plot(df['speed'], color='r', label='speed', marker='o', lw=4)
plt.plot(df['ave_speed'], color=(0, 0.38, 0.38), linestyle='--', label='ave_speed', linewidth=3)
plt.legend()
plt.grid(True)

plt.subplot(3,1, 2)

ax.set_facecolor((.42, .23, .15))
plt.plot(df['watt'], color='r', label='watt', marker='o', lw=4)
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3)

ax.set_facecolor((0.21, 0.21, 0.21))
plt.plot(df['spm'], color='r', label='spm', marker='o', lw=4)
plt.plot(df['ave_spm'], color=(0, 0.38, 0.38), linestyle='--', label='ave_spm', linewidth=3)
plt.legend()
plt.grid(True)

plt.show()

# 0:20.3 1:59.3 33
# 0:38.3 1:54.3 34
# 0:53.2 1:56.3 33
# 1:12.3 1:56.3 33
# 1:30.8 2:05.3 28
# 1:56.3 2:10.3 29
# 2:16.3 2:01.3 30
# 2:36.3 2:05.3 33
# 2:56.3 2:10.3 32
# 3:18.3 2:14.2 30
