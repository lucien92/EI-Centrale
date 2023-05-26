import os

path_to_folder = "/home/lucien/datascience.stackexchange.com"

L = []
for filename in os.listdir(path_to_folder):
    L.append(filename)

print(L)