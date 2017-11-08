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
plt.ylim((0.5, 1.05))

# add some text for labels, title and axes ticks
#plt.title('Accuracy vs. Look-back')
plt.ylabel('Accuracy')
plt.xlabel('Look-back m')
plt.grid()

plt.savefig('./memory/accuracy-vs-look-back.pdf', bbox_inches='tight')


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
plt.ylim((0.5, 1.05))

# add some text for labels, title and axes ticks
#plt.title('Accuracy vs. Hidden Size')
plt.ylabel('Accuracy')
plt.xlabel('Hidden Size d')
plt.grid()

plt.savefig('./memory/accuracy-vs-hidden-size.pdf', bbox_inches='tight')

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
plt.ylim((0.5, 1.05))

# add some text for labels, title and axes ticks
#plt.title('Accuracy vs. Look-back')
plt.ylabel('Accuracy')
plt.xlabel('Look-back m')
plt.grid()

plt.savefig('./memory/accuracy-vs-look-back2.pdf', bbox_inches='tight')

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
plt.ylim((0.5, 1.05))

# add some text for labels, title and axes ticks
#plt.title('Accuracy vs. Look-back')
plt.ylabel('Accuracy')
plt.xlabel('Amount of data N')
plt.grid()

plt.savefig('./memory/more-training-data.pdf', bbox_inches='tight')

if show:
    plt.show()


##################################
# Multiple classes and more layers
##################################
plt.figure(figsize=(5, 3))

x = tuple(range(2, 16))
y1 = (1.0000, 0.9999, 0.9998, 0.9987, 0.9957, 0.9704, 0.9343, 0.9129, 0.8365, 0.7561, 0.7114, 0.6656, 0.6522, 0.5748)
y2 = (1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.9999, 0.9998, 0.9998, 0.9992, 0.9801, 0.9883, 0.9730, 0.9313, 0.9317)

#plt.bar(x, y, width, color='b')
plt.plot(x, y1, 'bo-', label='One layer')
plt.plot(x, y2, 'ro-', label='Two layers')
plt.xticks(x)
plt.ylim((0.5, 1.05))
plt.legend(loc=3)

# add some text for labels, title and axes ticks
#plt.title('Accuracy vs. Look-back')
plt.ylabel('Accuracy')
plt.xlabel('Number of classes C')
plt.grid()

plt.savefig('./memory/accuracy-vs-multiple-classes-and-layers.pdf', bbox_inches='tight')

if show:
    plt.show()


################################
# Regression vs. Classification
################################
plt.figure(figsize=(5, 3))

x = tuple(range(2, 16))
y1 = (1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.9677, 0.9605, 0.7400, 0.9955, 0.8814, 0.9040)
y2 = (1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.9998, 0.9955, 0.9998, 0.0900, 0.0822, 0.0757, 0.0717, 0.0667)
#y3 = [1 / i for i in range(2, 16)]

#plt.bar(x, y, width, color='b')
plt.plot(x, y1, 'bo-', label='Classification')
plt.plot(x, y2, 'ro-', label='Regression')
#plt.plot(x, y3, '--', color='gray', label='Chance')
plt.xticks(x)
plt.ylim((0, 1.05))
plt.legend(loc=3)

# add some text for labels, title and axes ticks
#plt.title('Accuracy vs. Look-back')
plt.ylabel('Accuracy')
plt.xlabel('Number of classes C')
plt.grid()

plt.savefig('./memory/classificaton-vs-regression-num-classes.pdf', bbox_inches='tight')

if show:
    plt.show()