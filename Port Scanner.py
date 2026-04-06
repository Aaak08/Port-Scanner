import socket

def port_scanner(target, start_port, end_port):
    print(f"Scanning {target}...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket()
        sock.settimeout(0.5)
        result = sock.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    print("Scan complete.")
            
    
        

target = input("Enter target IP: ")
port_scanner(target, 1, 100)