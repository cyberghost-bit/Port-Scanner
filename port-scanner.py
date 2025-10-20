import socket
import sys
import time
import concurrent.futures

if len(sys.argv) != 2:
    print("Usage : script.py [HOST]")
    sys.exit()

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    conn = s.connect_ex((ip, port))
    if conn == 0:
        try:
            service = socket.getservbyport(port)
        except Exception:
            service = "Unknown Service"
        return (port, service)
    else:
        return None

def scanner():
    host = sys.argv[1]
    ports = (20, 21, 22, 23, 25, 53, 69, 80, 139, 137, 443, 445, 1433, 1434, 3306, 3389, 8000, 8080, 8443)
    ip = socket.gethostbyname(host)

    print(f"Starting Scan on Host {host} ({ip})")
    start_time=time.time()

    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, ip, port) for port in ports}
        for futures in concurrent.futures.as_completed(futures):
            result=futures.result()
            if result is not None:
                open_ports.append(result)
    
    print("PORT\tSTATE\tSERVICE")
    for port, service in open_ports:
        print(f"{port}/tcp\topen\t{service}")
    end_time=time.time()
    print(f"\nScan completed in {end_time - start_time:.2f} seconds")

scanner()
