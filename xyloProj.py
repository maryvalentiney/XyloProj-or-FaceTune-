import OSC

def attention (data):
    if data < 50:
        print ("note0")
    else: 
        pass

def browFurrow (data):
    if data > 70:
        print ("note1")
    else:
        pass

def  browRaise (data):
    if data > 50:
        print ("note2")
    else: 
        pass

def eyeClosure (data):
    if data > 80:
        print ("note6")
    else:
        pass

def jawDrop (data):
    if 95 < data < 100:
        print ("note9")
    else: 
        pass

def lipPucker (data):
    if 80 < data < 99:
        print ("note13")
    else: 
        pass


def dataHandler(addr, tags, data, client_address):
    attention(data[0])
    browFurrow(data[1])
    browRaise(data[2])
    eyeClosure(data[6])
    jawDrop(data[9])
    lipPucker(data[13])
    

if __name__ == "__main__":
    o = OSC.OSCServer(('127.0.0.1', 6448))  # listen on  port 3333
    # calls the function named exampleHandler() for OSC messages received with the /example address
    # add more handlers the same way
    o.addMsgHandler('/wek/inputs', dataHandler)
    o.serve_forever()


    


    