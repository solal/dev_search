import time
start_time = time.time()



try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
query = "python for loop"
 
for j in search(query, stop=10):
    print(j)


print("--- %s seconds ---" % (time.time() - start_time))