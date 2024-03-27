coine = ['H','T']
counter = 1

#generate a series of flips as data
import random
coine = random.choices(coine, k=100)

#count the number of heads and tails
heads = coine.count('H')
tails = coine.count('T')

#calculate the probabilities
prob_heads = heads/len(coine)
prob_tails = tails/len(coine)

#print first set of results
print("Number of time data is generated: ", counter)
print("the number of heads is: ", heads)
print("the number of tails is: ", tails)
print("the probability of getting heads is: ", prob_heads*100, "%")
print("the probability of getting tails is: ", prob_tails*100, "%")
print("Number of time data is generated: ", counter)
print(" ")



#keep generating data until the probability of getting heads is =0.5 and the probability of getting tails is =0.5
while prob_heads != 0.5 and prob_tails != 0.5:
    coine = random.choices(coine, k=100)
    heads = coine.count('H')
    tails = coine.count('T')
    prob_heads = heads/len(coine)
    prob_tails = tails/len(coine)
    counter += 1
    print("the number of heads is: ", heads)
    print("the number of tails is: ", tails)
    print("the probability of getting heads is: ", prob_heads*100, "%")
    print("the probability of getting tails is: ", prob_tails*100, "%")
    print("Number of time data is generated: ", counter)
    print(" ")
