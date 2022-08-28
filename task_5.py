# 5.	Дан список ["I", "love", "lists", "they", "are", "my", "favorite"]
# из него строку => "I love arrays they are my favorite"

a = ["I", "love", "lists", "they", "are", "my", "favorite"]
a[2] = 'arrays'
a_join = ' '.join(a)
print(a_join)