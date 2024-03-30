from sklearn.cluster import AgglomerativeClustering
num_clusters = 5
agglo1 = AgglomerativeClustering(n_clusters=num_clusters, affinity='euclidean') #cosine, l1, l2, manhattan
get_ipython().magic('time answer = agglo1.fit_predict(sent_embs)')

#были получены 5 кластеров, остаётся выяснить, за какую тему отвечает каждая из групп.

cl = {}
for cluster, data in tqdm(report.groupby('AGGLOM'), desc=method):
    arr = ' '.join(data['НФ'].values).split()
    arr_morph = []
    for k in arr:
        arr_morph.append(morph.parse(k)[0].normal_form) 
    cl[method+'_'+str(cluster)] = Counter([x.replace('ё', 'е') for x in arr_morph if x not in stopwords]).most_common(10) 

#для каждого кластера подсчитали все входящие слова и ТОП10 из них были представлены в качестве основной темы.
