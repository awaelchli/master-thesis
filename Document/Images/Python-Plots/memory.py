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
plt.figure(figsize=(4, 3))

x = (1, 2, 3, 4, 5)
y = (0.9999, 0.7495, 0.7208, 0.6452, 0.6744)

#plt.bar(x, y, width, color='b')
plt.plot(x, y, linetype)
plt.xticks(x)
plt.ylim((0.5, 1.01))

# add some text for labels, title and axes ticks
#plt.title('Accuracy vs. Look-back')
plt.ylabel('Accuracy')
plt.xlabel('Look-back m')
plt.grid()

plt.savefig('./accuracy-vs-look-back.pdf', bbox_inches='tight')


if show:
    plt.show()


##########################
# Hidden size vs. Accuracy
##########################
plt.figure(figsize=(4, 3))

x = (1, 2, 3, 4, 5, 6, 7)
y = (0.6744, 0.7404, 0.8276, 0.9258, 0.9433, 1.0000, 1.0000)

#plt.bar(x, y, width, color='b')
plt.plot(x, y, linetype)
plt.xticks(x)
plt.ylim((0.5, 1.01))

# add some text for labels, title and axes ticks
#plt.title('Accuracy vs. Hidden Size')
plt.ylabel('Accuracy')
plt.xlabel('Hidden Size d')
plt.grid()

plt.savefig('./accuracy-vs-hidden-size.pdf', bbox_inches='tight')

if show:
    plt.show()


###################################################
# Look-back vs. Accuracy with increased hidden size
###################################################
plt.figure(figsize=(4, 3))

x = (6, 7, 8, 9, 10, 11, 12, 13, 14)
y = (1.0000, 1.0000, 1.0000, 0.9892, 0.9720, 0.9125, 0.8691, 0.7456, 0.6877)

#plt.bar(x, y, width, color='b')
plt.plot(x, y, linetype)
plt.xticks(x)
plt.ylim((0.5, 1.01))

# add some text for labels, title and axes ticks
#plt.title('Accuracy vs. Look-back')
plt.ylabel('Accuracy')
plt.xlabel('Look-back m')
plt.grid()

plt.savefig('./accuracy-vs-look-back2.pdf', bbox_inches='tight')

if show:
    plt.show()


####################
# More training data
####################
plt.figure(figsize=(4, 3))

x = (1e5, 2e5, 3e5, 4e5, 5e5)
y = (0.6877, 0.8836, 0.8046, 0.9484, 0.9943)

#plt.bar(x, y, width, color='b')
plt.plot(x, y, linetype)
plt.xticks(x)
plt.ylim((0.5, 1.01))

# add some text for labels, title and axes ticks
#plt.title('Accuracy vs. Look-back')
plt.ylabel('Accuracy')
plt.xlabel('Amount of data N')
plt.grid()

plt.savefig('./more-training-data.pdf', bbox_inches='tight')

if show:
    plt.show()