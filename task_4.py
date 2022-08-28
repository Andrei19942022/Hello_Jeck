# 4.	Перевести строку в массив по пробелу "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "lists", "they", "are", "my", "favorite"]

a = "Robin Singh"
a_split = a.split(" ")
print(a_split)

b = "I love arrays they are my favorite"
b_replace = b.replace('arrays', 'lists')
b_split = b_replace.split(" ")
print(b_split)
