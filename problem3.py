AllStudents = ['Ahmed','Mohamed', 'Wael', 'Peter', 'Sherif' ,'Noha', 'Mona', 'Sally','Dina', 'Mary']

EventA = ['Ahmed','Mohamed' 'Wael','Peter','Sally', 'Dina', 'Mary'] #Students who like music
EventB = ['Ahmed', 'Mohamed', 'Wael', 'Peter', 'Sherif','Mary'] #Students who like football
EventC = ['Ahmed', 'Mohamed', 'Wael', 'Peter','Mary']#Students who

likes_Music = len(EventA) / len(AllStudents)
likes_Football = len(EventB) / len(AllStudents)
likes_Music_and_Football = len(EventC) / len(AllStudents)

print("Probability of selecting a student who likes music:", likes_Music)   
print("Probability of selecting a student who likes football:", likes_Football)
print("Probability of selecting a student who likes music and football:", likes_Music_and_Football)
print("Probability of selecting a student who likes music Or football:", likes_Music + likes_Football - likes_Music_and_Football)
print("Probability of selecting a student who likes nethir:", 1-(likes_Music + likes_Football - likes_Music_and_Football))
print("Probability of selecting a student who likes music and not football:", likes_Music - likes_Music_and_Football)

