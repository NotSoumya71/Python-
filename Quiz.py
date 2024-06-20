#!/usr/bin/env python
# coding: utf-8

# In[3]:


# The function:
def quiz(ques, ans, score):
    user_ans = input(ques)
    if user_ans.lower() == ans.lower():
        print("Correct :)")
        score += 1
    else:
        print("Wrong :( \nThe answer was", ans)
    return score

score = 0

# The questions and answers:
q1 = "What is the name of the galaxy in which we live? "
a1 = "Milky Way"
q2 = "What is the name of the force which keeps the planets in orbit around the sun? "
a2 = "Gravity"
q3 = "What is the term for a natural satellite? "
a3 = "moon"
q4 = "Who was the second man to step on the moon? "
a4 = "Buzz Aldrin"
q5 = "Which is the largest moon of Saturn? "
a5 = "Titan"
q6 = "The speed of which object is considered the fastest?"
a6 = "light"
q7 = "What planet is the hottest in the solar system?"
a7 = "Venus"
q8 = "In which layer of the atmosphere do planes fly?"
a8 = "Stratosphere"
q9 = "Who is known for discovering different planets and moons?"
a9 = "Galileo Galilei"
q10 = "What galaxy is the closest to Milky Way?"
a10 = "Andromeda"

# The calling:
score = quiz(q1, a1, score)
score = quiz(q2, a2, score)
score = quiz(q3, a3, score)
score = quiz(q4, a4, score)
score = quiz(q5, a5, score)
score = quiz(q6, a6, score)
score = quiz(q7, a7, score)
score = quiz(q8, a8, score)
score = quiz(q9, a9, score)
score = quiz(q10, a10, score)
print("Your final score is", score)


#Code for a space quiz :O


# In[ ]:




