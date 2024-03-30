from sklearn.feature_extraction.text import TfidfVectorizer

texts = ["Soft kitty lyrics:", "Soft kitty, warm kitty", "Little ball of fur", "Happy kitty, sleepy kitty", "Purr, purr, purr"]
tfidf_vec = TfidfVectorizer()
tfidf = tfidf_vec.fit_transform(texts)
print(tfidf)