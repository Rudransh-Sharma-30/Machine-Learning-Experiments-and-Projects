# import numpy as np

# new_matrix = np.array([[1,2],[4,5]], dtype = 'int64')
# # print(new_matrix)


# # a = new_matrix.ndim
# # b = new_matrix.shape
# # c = new_matrix.dtype
# # d = new_matrix.itemsize
# # e = new_matrix.nbytes
# # f = new_matrix.size
# # g = new_matrix[1,1]
# # h = new_matrix[0,:]
# # i = new_matrix[1,:-1]
# # j = new_matrix[:-1,1]
# # k = new_matrix[0,::-2]

# # print(a,b,c,d,e,f,g,h,i,j,k)

# # matrix = np.full_like(new_matrix,4)
# # m2 = np.full((2,2),99)
# # print(matrix , m2)

# #np.random.rand(2,2)
# #np.random.random_sample(new_matrix.shape)
# # np.random.randint(7,(2,2))
# # m3 = np.repeat(new_matrix,2,axis = 0) #axis = 0 helps us operate vertically whereas axis = 1 helps us operate horizontally for a 2d matrix
# # print(m3)

# # output = np.ones((5,5))
# # output[1:4,1:4] = np.zeros((3,3))
# # output[2,2] = 9
# # print(output)
# # m3 = np.identity(3)
# # x = np.linalg.det(new_matrix)
# # print(x)
# # print(new_matrix.reshape(1,4))
# v1 = np.array([1,2,3,4])
# v2 = np.array([5,6,7,8])
# v3 = np.vstack([v1,v2,v1])
# v4 = np.hstack([v1,v2,v1])
# print(v4,v3)
# file_date = np.genfromtxt('data.doc',delimiter=',')
# print(file_date.astype('int32'))
# file_date[file_date > 2] #we can use "~" which basically means "not"