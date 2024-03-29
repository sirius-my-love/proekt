import re
import nltk
text = 'Для начала мы решили вручную проанализировать клиентские отзывы о банке Тинькофф. jhjfjgf'


def cleared_list(text):
    c = text.lower()
    c = re.sub(r"[A-Za-z!#$%&'()*+,./:;<=>?@[\]^_`{|}~—\"\-]+", ' ', c)
    c = c.strip()
    words = c.split()
    res = []
    stopwords = nltk.corpus.stopwords.words('russian')
    stopwords.append("тинькофф")
    for k in words:
        if k not in stopwords:
            res.append(k)
    return res


print(cleared_list(text))