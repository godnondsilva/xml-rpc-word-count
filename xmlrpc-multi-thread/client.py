import xmlrpc.client
import threading

PORTS = [8085, 8086, 8087]
proxies = []
words = {}

def merge_words(dct):
    for (key, value) in dct.items():
        words.setdefault(key, 0)
        words[key]+=int(value)

class ClientThread(threading.Thread):
    def __init__(self, localhost, port, filename):
        threading.Thread.__init__(self)
        self.client=xmlrpc.client.ServerProxy(f"http://{localhost}:{port}/")
        self.filename = filename

    def run(self):
        merge_words(self.client.word_count(f'../data/{self.filename}.txt'))

c1 = ClientThread("localhost", 8085, "data1")
c1.start()
c2 = ClientThread("localhost", 8086, "data2")
c2.start()
c3 = ClientThread("localhost", 8087, "data3")
c3.start()

# Wait for threads to complete
c1.join()
c2.join()
c3.join()

# Print result
print(words)