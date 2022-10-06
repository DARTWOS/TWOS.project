# ### Practice

# **You have 100 cats.**

# One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.
# 1. The first round, you stop at every cat, placing a hat on each one.
# 2. The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# 3. The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# 4. You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
# Write a program that simply outputs which cats have hats at the end.

cats = []
cats_in_hats =[]
b = 'no'
for a in range(100):
 cats.append(b)

for a in range(100):
 for x in range(a, len(cats), a +1):
  if cats[x] == 'no':
   cats[x] = 'yes'
  else:
   cats[x] = 'no'


for x in range(0, len(cats)):
 if cats[x] == 'yes':
  cats_in_hats.append(x+1)
print('there will be cats in hats with numbers', cats_in_hats)






