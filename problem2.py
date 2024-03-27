coine = ['H','T']
import random
coine = random.choices(coine, k=100)



print("the probability of getting 1 heads is: ", coine.count('H')/len(coine))
print("the probability of getting 1 tails is: ", coine.count('T')/len(coine))
print("the probability of getting 1 heads or 1 tails is: ", coine.count('H')/len(coine) + coine.count('T')/len(coine))
print("the probability of getting  nither heads nor tails is: ", 1-(coine.count('H')/len(coine) + coine.count('T')/len(coine)))

20210405 