from sklearn.feature_extraction.text import TfidfVectorizer

texts = ["Soft kitty lyrics:", "Soft kitty, warm kitty", "Little ball of fur", "Happy kitty, sleepy kitty", "Purr, purr, purr"]
tfidf_vec = TfidfVectorizer()
tfidf = tfidf_vec.fit_transform(texts)
print(tfidf) #пример работы модуля TfidfVectorizer


from collections import Counter


words = list(input())
test_counter = Counter(words) #считает количество вхождений каждого слова
a = test_counter.most_common(20) #принимает первые 20 часто встречаемых слов

w_i = dict()
i_w = dict()
for i, word in enumerate(test_counter.most_common(500)):
	w_i[word[0]] = i + 2
	i_w[i + 2] = word[0]
#print(w_i) - словарь, в котором ключем является "порядковый номер" слова
#print(i_w) - словарь, в котором ключем является само слово

def text(txt, w_i): #функкция позволяет представить текст в виде чисел, которые являются "порядковыми номерами"
	seq = []
	for word in txt:
		index = w_i.get(word, 1)
		if index != 1:
			seq.append(index)
	return seq


print(text(new_res[0], w_i))
