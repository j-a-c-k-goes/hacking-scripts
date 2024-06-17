"""
Overview
# ------------------------------------------------------------
This script is a port scanner. It searches a range of ports, displays open/close status.

Concepts covered from Build
-------------------------------------
- Network Connectivity
- Script Timeouts
- Target Server Status
- Rate Limiting
- Port Spectrum
- Threading

Notes on Ports
-----------------------------------------------------
0 - 1023        well knowns, standard protocols
                80  (HTTP)
                443 (HTTPS)
                25  (SMTP)
1024 - 49151    standards, often used by software apps
49152 - 65535   backroom, often temp connections
"""
# ------------------------------------------------------------
import socket # network functions
import sys    
import threading
# ------------------------------------------------------------
def port_scanner( port ):
  try:
    current_socket      = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    current_socket.settimeout(5)
    current_connection  = current_socket.connect( ( target, port ) )
    print( f'Port { port } is open' )
    current_connection.close()
  except Exception as error:
    # print( f" Port { port } blocked." )
    pass
# ------------------------------------------------------------
if __name__ == "__main__":
    if (len(sys.argv) != 4):
      print("Insufficient arguments.")
      target      = input( "Enter the target IP address to scan: " )
      start_port  = int( input( "Enter port number to start scanning at: " ) )
      end_port    = int( input( "Enter port number to conclude scanning at: ") )
    else:
      target      = str(sys.argv[1])
      start_port  = int(sys.argv[2])  
      end_port    = int(sys.argv[3])
    try:  
      print( "\nResults" )
      print( "----------------------------------------------------" )
      for port in range( start_port, end_port + 1 ):
        thread = threading.Thread( target=port_scanner, args=( port, ) )
        thread.start()
      print( "\n" )
    except Exception as error:
      print("Error: ", error)