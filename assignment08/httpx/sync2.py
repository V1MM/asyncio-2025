import requests
import time

urls = ["https://httpbin.org/delay/3"] * 5

start = time.time()
for url in urls :
    resonse = requests.get(url)
    print(resonse.status_code)
print("Total Time : ", time.time() - start)
