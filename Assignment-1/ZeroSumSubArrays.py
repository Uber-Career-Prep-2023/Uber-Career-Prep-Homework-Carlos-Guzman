"""
Given an array of integers, count the number of subarrays that sum to zero.

Examples:
Input Array: [4, 5, 2, -1, -3, -3, 4, 6, -7]
Output: 2
(Subarrays: [5, 2, -1, -3, -3], [-3, 4, 6, -7])

Input Array: [1, 8, 7, 3, 11, 9]
Output: 0

Input Array: [8, -5, 0, -2, 3, -4]
Output: 2
(Subarrays: [0], [8, -5, 0, -2, 3, -4])



"""

#naive aproach
#window slide technique

# array = [4, 5, 2, -1, -3, -3, 4, 6, -7]
# window_size = 0
# left_pointer = 0
# contador = 0
# aux = 1
# suma = sum(array[:aux])
# prueba = 0
# while window_size < len(array)-1:
#     #print("iteracion "+str(prueba))
#     #prueba += 1
#     if suma == 0:
#         #print('entro en el primer if')
#         contador += 1
#         suma = (suma + array[aux+window_size]) - array[left_pointer]
#         aux += 1
#         left_pointer += 1
#         print(array[left_pointer:aux+window_size])
#     elif aux+window_size >= len(array)-1:
#         #print('entro en el segundo if')
#         window_size += 1
#         aux = 1
#         left_pointer = 0
#         suma = sum(array[:aux+window_size])
#     else:
#         #print('entro en el tercer if')
#         aux += 1
#         #print(suma,window_size,aux,array[:aux+window_size])
#         suma = (suma + array[aux+window_size]) - array[left_pointer]
#         left_pointer += 1
    
# print(contador)



# second naive 

# array = [4, 5, 2, -1, -3, -3, 4, 6, -7]
# contador = 0
# for i in range(len(array)):
#     suma = 0
#     for j in range(i, len(array)):
#         suma += array[j]
#         if suma == 0:
#             contador += 1
# print(contador)

#solution O(n) hashtable technique time 48 min sorry for the time 

arr = [4,5,2,-2]

def count_zero_sum_subarrays(arr):
    count = 0
    sum_dict = {0: [-1]}
    cum_sum = 0
    for i in range(len(arr)):
        cum_sum += arr[i]
        if cum_sum in sum_dict:
            count += len(sum_dict[cum_sum])
        #if cum_sum in sum_dict:
            sum_dict[cum_sum].append(i)
        else:
            sum_dict[cum_sum] = [i]
    print(sum_dict)
    return count

print(count_zero_sum_subarrays(arr))
