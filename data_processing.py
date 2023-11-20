import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer    
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def clean_data() :
    movies = pd.read_csv('Highest Holywood Grossing Movies.csv')

    ## data preprocessing
    movies.describe()
    # movies.head()
    # movies.isnull().sum()
    movies.dropna(inplace=True)
    # movies.duplicated().sum()
    movies['Tag'] = movies['Movie Info'] + movies['Genre']
    new_data = movies.drop(columns=['Movie Info', 'Genre', 'Budget (in $)', 'Domestic Sales (in $)', 'Running Time','Year', 'Distributor', 'Domestic Opening (in $)','International Sales (in $)','Release Date','World Wide Sales (in $)', 'License'])
    # print(new_data)

    ##
    cv = CountVectorizer(max_features = 1000, stop_words='english')
    vector = cv.fit_transform(new_data['Tag'].values.astype('U')).toarray()
    # vector.shape
    similarity = cosine_similarity(vector)
    # new_data[new_data['Title']=="Avengers: Endgame"].index[0]
    # new_data.info()

    # distance = sorted(list(enumerate(similarity[3])), reverse= True, key=lambda vector:vector[1])
    # for i in distance [0:6]:
    #     print(new_data.iloc[i[0]].Title)
 
# def recommend(movies):
#         index = new_data[new_data['Title']==movies].index[0]
#         distance = sorted(list(enumerate(similarity[index])), reverse= True, key=lambda vector:vector[1])
#         for i in distance [0:5]:
#             print(new_data.iloc[i[0]].Title)
          
    ##import file data
    pickle.dump(new_data, open('movies_list.pkl', 'wb'))
    pickle.dump(similarity, open('similarity.pkl', 'wb'))
    pickle.load(open('movies_list.pkl', 'rb')) 
    pickle.load(open('similarity.pkl', 'rb')) 

