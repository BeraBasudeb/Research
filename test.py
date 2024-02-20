import numpy as np
import matplotlib.pyplot as plt

X = ['Mishra et al.', 'Rewal et al.', 'Islam and Basu','Dabra et al.','Feng et al.', 'Zhang et al.', 'Chang et al.', 'Irshad et al.', 'QRAC-IoD']
Ymsg = [3, 4, 6, 3, 3, 4, 4, 3, 3]
Zcomm = [14.530, 20.162, 20.546, 9.890, 9.730, 14.336, 10.752, 15.008, 11.521]

X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, Ymsg, 0.4, label = 'Number of messages', color='orange')
plt.bar(X_axis + 0.2, Zcomm, 0.4, label = 'Communication cost (in kilobit)', color='limegreen')

plt.xticks(X_axis, X, fontsize=25)
plt.yticks(fontsize=30)
#plt.xlabel("Groups", fontsize=20)
#plt.ylabel("Number of Students", fontsize=20)
#plt.title("Number of Students in each group", fontsize=20)
plt.legend(fontsize="35")
plt.grid(linestyle = "dashed")
plt.show()

