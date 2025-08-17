###########*************LINE CHART************
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# x = [0,1,2,3,4]
# y = [0,2,4,6,8]
# ##setting the size
# plt.figure(figsize = (5,3) , dpi = 300)
# plt.plot(x,y , label = '2x',color = 'red' , linewidth = 2 , linestyle = "--"  , marker = ".", markersize = 10 , markeredgecolor = 'blue')

# ##line number 2
# x2 = np.arange(0,4.5,0.5)
# print(x2)
# #shorthand notation is '[color][marker][line]'
# # plt.plot(x,y , 'r^-' ,label = '2x')
# plt.title('Our first graph', fontdict = {'fontname' : 'Comic Sans MS' , 'fontsize' : 20})
# plt.xlabel('X axis') # can use fontdict for this as well
# plt.ylabel('Y axis')
# plt.plot(x2[:6],x2[:6]**2 , label = "x^2" , color = "blue" , linewidth = 2 , marker = "*" ,markersize = 10 )
# plt.plot(x2[4:],x2[4:]**2 , label = "x^2" , color = "blue" , linestyle = "--" ,linewidth = 2 , marker = "*" ,markersize = 10 )
# plt.xticks([0,1,2,3,4])
# plt.yticks([0,2,4,6,8,10])
# plt.savefig('mygraph.png' , dpi = 300)

# plt.show()


######*******************BAR CHART************

# labels = ['A','B','C']
# values = [1,4,2]
# plt.figure(figsize= (6,4))
# patterns = ['/','O','*']
# bars = plt.bar(labels , values)
# for bar in bars:
#     bar.set_hatch(patterns.pop(0))
# # bars[0].set_hatch('/')
# # bars[1].set_hatch('O')
# # bars[2].set_hatch('*')





# plt.show()

#*************Line graph*******************
gas = pd.read_csv('/Users/ajitk/Desktop/Rudransh/Python/gas_prices.csv')
plt.figure(figsize = (8,5) , dpi = 100)

plt.plot(gas.Year , gas.USA , 'b.-')
plt.plot(gas.Year , gas.Canada , 'r.-')
plt.plot(gas.Year , gas["South Korea"] , 'g.-')

plt.xticks(gas.year[::3])
plt.xlabel('Year')
plt.ylabel('USD')
plt.legend()
plt.show()
