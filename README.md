# Проект в рамках "Сириус ИИ". Инструмент для анализа клиентских отзывов.

Команда разработки: 

- :white_check_mark: [Kravtsova Helen (в роли Python-разработчика)](https://github.com/lenakravt)
- :white_check_mark: [Ivanova Maria (в роли дизайнера и копирайтера)](https://github.com/theivanovamary)

## Описание проекта:
Файл [parser.ru](https://github.com/sirius-my-love/proekt/blob/main/parser.py) парсит отзывы клиентов с сайта. При этом использованы стандартные библиотеки requests и BeautifulSoup.

В файле [cleared.ру](https://github.com/sirius-my-love/proekt/blob/main/cleared.py) производится предварительная обработка текста посредством nltk (удаление stop-слов, пунктуации, лишних символов.)

В файле [stemming.ру](https://github.com/sirius-my-love/proekt/blob/main/stemming.py) происходит стемминг слов.

С помощью word2vec создается 1000 мерный вектор и производится вычисление значений токенов.

Далее для получения предсказания мы вычисляем среднее значение по всем векторам токенов в предложении
Обучение классификатора настроений клиентов производится в качестве примера с помощью DecisionTreeClassifier и Xgboost. Accuracy 75% на мой взгляд неплохо.
В последующем будет реализована модель на Pytorch
## Инструкция по установке:

## Надеемся Вам понравится наш проект!)
![Logo](https://static.theceomagazine.net/wp-content/uploads/2018/09/18094615/2018.08.13_AndrewCannington_AI-revolution-gender-biased_subbed.jpg)
