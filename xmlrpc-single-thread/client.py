import xmlrpc.client
PORTS = [8085, 8086, 8087]
proxies = []
words = {}

for port in PORTS:
    proxies.append(xmlrpc.client.ServerProxy(f"http://localhost:{port}/"))

def merge_words(dct):
    for (key, value) in dct.items():
        words.setdefault(key, 0)
        words[key]+=int(value)

for i in range(1, len(proxies)+1):
    merge_words(proxies[i-1].word_count(f'../data/data{i}.txt'))

print(words)
