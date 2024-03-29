import re
import nltk
text = 'Для начала мы решили вручную проанализировать клиентские отзывы о банке Тинькофф. jhjfjgf'

#функция cleared_list очищает текст от знаков препинания, латинских букв и прочих ненужных символов.

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

#принцип работы функции можно отследить на примере предложения text - результат работы - список слов в нижнем регистре.

print(cleared_list(text))

#Output: ['начала', 'решили', 'вручную', 'проанализировать', 'клиентские', 'отзывы', 'банке']
