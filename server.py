from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os
server = SimpleXMLRPCServer(('localhost' ,3000), allow_none = True)

prices = {'Phone' : 20000 , 'Bag' : 2000 , 'Cable' : 300 , 'TV' : 30000 , 'Chair' : 2500}
def load_data():
    return prices

def calculate_total(cart):
   total = 0
   for k, v in cart.items():
        total += prices[k] * v
   return total
   
server.register_function(load_data)
server.register_function(calculate_total)

if __name__ == '__main__':
    try :
        print('Serving ... ')
        server.serve_forever()
    except KeyboardInterrupt:
       print ('Exiting ')
