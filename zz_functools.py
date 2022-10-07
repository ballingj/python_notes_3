from functools import lru_cache
import requests

@lru_cache(maxsize=32)
def get_with_cache(url):
    try:
        r = requests.get(url)
        return r.text
    except:
        return "Not Found"


for url in ["https://google.com/",
            "https://martinheinz.dev/",
            "https://reddit.com/",
            "https://google.com/",
            "https://dev.to/martinheinz",
            "https://google.com/"]:
    get_with_cache(url)

print(get_with_cache.cache_info())
# CacheInfo(hits=2, misses=4, maxsize=32, currsize=4)
print(get_with_cache.cache_parameters())
# {'maxsize': 32, 'typed': False}