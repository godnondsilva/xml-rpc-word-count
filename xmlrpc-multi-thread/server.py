from xmlrpc.server import SimpleXMLRPCServer
import threading 

class WorkerThread (threading.Thread):
    def __init__(self, localhost, port):
        threading.Thread.__init__(self)
        self.worker = SimpleXMLRPCServer((localhost, port))

    def word_count(self, filename):
        words={}
        with open(filename) as f:
            for data in f.readlines():
                end = -1 if data[-1] == '\n' else len(data)
                for item in data[:end].split(" "):
                    words.setdefault(item, 0)
                    words[item]+=1
        return words
      
    def run(self):
        self.worker.register_function(self.word_count, "word_count")
        self.worker.serve_forever()
    

WorkerThread("localhost", 8085).start()
WorkerThread("localhost", 8086).start()
WorkerThread("localhost", 8087).start()
print("Server is running")