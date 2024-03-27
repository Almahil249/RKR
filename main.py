import pandas as pd

df = pd.DataFrame(data={'data': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 23, 15]})
even_numbers = df[df['data'] % 2 == 0]
divisible_by_3_and_5 = df[(df['data'] % 3 == 0) & (df['data'] % 5 == 0)]
probability_even = len(even_numbers) / len(df)
probability_divisible_by_3_and_5 = len(divisible_by_3_and_5) / len(df)

print("Probability of selecting an even number:", probability_even)
print("Probability of selecting a number divisible by 3 and 5:", probability_divisible_by_3_and_5)
