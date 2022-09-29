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

server2 = SimpleXMLRPCServer(("localhost", 8086))
print("Server running")
server2.register_function(word_count, "word_count")
server2.serve_forever()