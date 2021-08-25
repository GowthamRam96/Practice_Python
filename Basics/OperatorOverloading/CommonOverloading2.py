#Indexingn and Slicing
class Indexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index): # Called for index or slice
        print('getitem:', index)
        return self.data[index] # Perform index or slice


X = Indexer()
print(X[0]) # Indexing sends __getitem__ an integer
print(X[2:4]) # Slicing sends __getitem__ a slice object

#Results
'''
getitem: 0
5
getitem: slice(2, 4, None)
[7, 8]
'''
