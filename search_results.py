#pip install google
from googlesearch import search

query = input("Enter what you want to search: ")
result = int(input("How many results do you want: "))

search_results = []
for i in search(query, num=result, stop=result, pause=2.0):
    search_results.append(i)

print("Search Results:")
for url in search_results:
    print(url)
