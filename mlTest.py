

import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server


def lipPucker (address, *args):
  print (args[0])
  #if 80 < data < 99:
   # print ("note13")
  #else: 
   # print("pass")
    #pass

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=6448, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/wek/inputs", print)
  dispatcher.map("/wek/inputs", lipPucker)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()