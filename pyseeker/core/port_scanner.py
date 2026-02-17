# pyseeker/core/port_scanner.py
import socket
import threading
from ..utils.logger import print_info, print_success, print_warning

def grab_banner(ip, port, timeout=2):
    """Attempts to grab the banner from an open port."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((ip, port))
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        s.close()
        return banner if banner else None
    except socket.timeout:
        return None
    except ConnectionRefusedError:
        return None
    except Exception:
        return None

def scan_port(ip, port, open_ports, lock, timeout=1):
    """Scans a single port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            with lock:
                open_ports.append(port)
                print_success(f"[+] Port {port} is OPEN")
                banner = grab_banner(ip, port)
                if banner:
                    print_warning(f"    Banner: {banner}")
    except socket.error:
        pass
    finally:
        sock.close()

def run_port_scan(target, ports, max_threads=100):
    """
    Scans a target for open ports using multithreading.
    
    Args:
        target: IP address or hostname to scan
        ports: List of port numbers to scan
        max_threads: Maximum number of concurrent threads
    
    Returns:
        List of open port numbers
    """
    print_info(f"[*] Starting port scan on {target} for ports: {ports[0]}-{ports[-1]}")
    
    open_ports = []
    threads = []
    lock = threading.Lock()

    # Limit the number of concurrent threads
    for i, port in enumerate(ports):
        thread = threading.Thread(target=scan_port, args=(target, port, open_ports, lock))
        threads.append(thread)
        thread.start()
        
        # Limit thread creation to avoid overwhelming the system
        if (i + 1) % max_threads == 0:
            # Wait for threads in this batch to complete
            for t in threads[-max_threads:]:
                t.join()

    # Wait for all remaining threads
    for thread in threads:
        thread.join()

    return open_ports
