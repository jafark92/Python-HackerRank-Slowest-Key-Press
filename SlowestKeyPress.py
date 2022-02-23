import string

keyTimes = keyTimes = [[0,2], [1,3], [0,7]]

dict_keytimes = {}
for k in enumerate(keyTimes):
    if k[0]==0:
        dict_keytimes[0] = keyTimes[0][1]
    else:
        dict_keytimes[k[0]] = keyTimes[k[0]][1] - keyTimes[k[0]-1][1]

max_key = max(dict_keytimes, key=dict_keytimes.get)
print("The Slowest Key was", "'"+string.ascii_lowercase[keyTimes[max_key][0]]+"'")
