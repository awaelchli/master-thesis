"""
Plots for the experiment on LSTM memory capabilities
"""
import matplotlib.pyplot as plt

# the width of the bars
width = 0.5
linetype = 'bo-'
show = False

#########################
# Look-back vs. Accuracy
#########################
plt.clf()

x = (1, 2, 3, 4, 5)
y = (0.9999, 0.7495, 0.7208, 0.6452, 0.6744)

#plt.bar(x, y, width, color='b')
plt.plot(x, y, linetype)
plt.xticks(x)
plt.ylim((0.5, 1.01))

# add some text for labels, title and axes ticks
plt.title('Accuracy vs. Look-back')
plt.ylabel('Accuracy')
plt.xlabel('Look-back')

plt.savefig('./accuracy-vs-look-back.pdf')

if show:
    plt.show()


#########################
# Look-back vs. Accuracy
#########################
plt.clf()

x = (1, 2, 3, 4, 5, 6, 7)
y = (0.6744, 0.7404, 0.8276, 0.9258, 0.9433, 1.0000, 1.0000)

#plt.bar(x, y, width, color='b')
plt.plot(x, y, linetype)
plt.xticks(x)
plt.ylim((0.5, 1.01))

# add some text for labels, title and axes ticks
plt.title('Accuracy vs. Hidden Size')
plt.ylabel('Accuracy')
plt.xlabel('Hidden Size')

plt.savefig('./accuracy-vs-hidden-size.pdf')

if show:
    plt.show()