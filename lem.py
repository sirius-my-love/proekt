from pymystem3 import Mystem


def lemmatize_function(text):
    lemm = Mystem().lemmatize(text)
    return ''.join(lemm)


tx = ['начала', 'решили', 'вручную', 'проанализировать', 'клиентские', 'отзывы', 'банке']
new_tx = []
for i in tx:
    new_tx.append(lemmatize_function(i))
print(new_tx)