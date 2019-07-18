import pickle

my_list = [123, 3.14159, 'omais', ['another list']]
pickle_file = open('my_list.pkl', 'wb')

pickle.dump(my_list, pickle_file)

pickle_file.close()

pickle_file2 = open('my_list.pkl','rb')
my_list2 = pickle.load(pickle_file2)
print(my_list2)
