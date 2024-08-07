import sys
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def portscan_logo():
    print("""
          
 ███▄    █ ▓█████▄▄▄█████▓  ▄████  ██░ ██  ▒█████   █    ██  ██▓    
 ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒ ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒ ██  ▓██▒▓██▒    
▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▒██░▄▄▄░▒██▀▀██░▒██░  ██▒▓██  ▒██░▒██░    
▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ░▓█  ██▓░▓█ ░██ ▒██   ██░▓▓█  ░██░▒██░    
▒██░   ▓██░░▒████▒ ▒██▒ ░ ░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒▒█████▓ ░██████▒
░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░    ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░
░ ░░   ░ ▒░ ░ ░  ░   ░      ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░ ▒  ░
   ░   ░ ░    ░    ░      ░ ░   ░  ░  ░░ ░░ ░ ░ ▒   ░░░ ░ ░   ░ ░   
         ░    ░  ░              ░  ░  ░  ░    ░ ░     ░         ░  ░

""")

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)  # 타임아웃 시간을 줄임
        result = s.connect_ex((target, port))
        if result == 0:
            return port
        s.close()
    except socket.error:
        return None
    return None

def main():
    portscan_logo()

    target = input("NetGhoul Target? : ")
    print(f"Scanning Target : {target}")
    print(f"Scanning Started... {str(datetime.now())}")
    
    open_ports = []

    try:
        with ThreadPoolExecutor(max_workers=500) as executor:
            results = executor.map(scan_port, [target] * 65535, range(1, 65536))
            for port in results:
                if port:
                    open_ports.append(port)
                    print(f"[+] Port {port} is open")


    except KeyboardInterrupt:
        print("\n NetGhoul exit ")
        sys.exit()

    except socket.error:
        print("\n Host not responding :(")
        sys.exit()

    print(f"Scanning port 100% Completed at {datetime.now()}")
    print("Open ports: ", open_ports)

if __name__ == "__main__":
    main()











 
    






