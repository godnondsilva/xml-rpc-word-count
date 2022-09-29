from xmlrpc.server import SimpleXMLRPCServer

def word_count(filename):
    words={}
    with open(filename) as f:
        for data in f.readlines():
            end = -1 if data[-1] == '\n' else len(data)
            for item in data[:end].split(" "):
                words.setdefault(item, 0)
                words[item]+=1
    return words

server3 = SimpleXMLRPCServer(("localhost", 8087))
print("Server running")
server3.register_function(word_count, "word_count")
server3.serve_forever()