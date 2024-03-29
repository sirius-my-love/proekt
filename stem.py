from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("russian")
text = ['начала', 'решили', 'вручную', 'проанализировать', 'клиентские', 'отзывы', 'банке']


def stemming(text):
    lem_text = []
    for t in text:
        lem_text.append(stemmer.stem(t))
    return lem_text


print(stemming(text))