from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("russian")
text = ['начала', 'решили', 'вручную', 'проанализировать', 'клиентские', 'отзывы', 'банке']

#теперь необходимо получить начальные формы слов.
#функция stemming позволяет отбрасывать окончания в словах.

def stemming(text):
    lem_text = []
    for t in text:
        lem_text.append(stemmer.stem(t))
    return lem_text

#испробуем функцию для очищенного перед этим списка. 

print(stemming(text))

#Output: ['нача', 'реш', 'вручн', 'проанализирова', 'клиентск', 'отзыв', 'банк']
