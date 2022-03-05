import pandas as pd
import json
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

class Recom:
    def __init__(self, book_name):
        self.df = pd.read_csv('samples/dataset.csv')
        self.books = pd.read_csv('samples/books.csv')
        self.number = 10
        self.threshold = 50
        self.book_name = book_name
        
        
        
    def KNN_model(self):
        
        temp = ""
        data = (self.df.groupby(by = ['title'])['rate'].count().reset_index().
            rename(columns = {'rate': 'Total-Rating'})[['title', 'Total-Rating']])

        result = pd.merge(data, self.df, on='title', left_index = True)
        result = result[result['Total-Rating'] >= self.threshold]
        result = result.reset_index(drop = True)

        matrix = result.pivot_table(index = 'title', columns = 'id', values = 'rate').fillna(0)
        up_matrix = csr_matrix(matrix)
        
        
        model = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
        model.fit(up_matrix)

        distances, indices = model.kneighbors(matrix.loc[self.book_name].values.reshape(1, -1), n_neighbors = self.number+1)
        print("\nRecommended books:\n")
        for i in range(0, len(distances.flatten())):
            if i > 0:           
                temp += matrix.index[indices.flatten()[i]]+str("/")
                temp.strip       
       
       
        result = temp.split("/")[:-1]
        
        return json.dumps({'title' : result})