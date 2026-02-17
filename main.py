#!/usr/bin/env python3
# main.py
import argparse
import socket
import os
from pyseeker.core.subdomain_scanner import discover_subdomains
from pyseeker.core.port_scanner import run_port_scan, grab_banner
from pyseeker.core.vuln_checker import check_vulnerabilities
from pyseeker.utils.logger import print_banner, print_info, print_success, print_error

def resolve_domain(domain):
    """Resolves a domain name to an IP address."""
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        print_error(f"Could not resolve hostname: {domain}")
        return None

def parse_ports(port_str):
    """Parses a port string like '1-1024' or '22,80,443' into a list of ints."""
    if '-' in port_str:
        start, end = map(int, port_str.split('-'))
        return list(range(start, end + 1))
    elif ',' in port_str:
        return list(map(int, port_str.split(',')))
    else:
        return [int(port_str)]

def get_wordlist_path():
    """Returns the default path to the subdomains wordlist."""
    # Get the directory where main.py is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, 'pyseeker', 'data', 'subdomains.txt')

def main():
    # Print banner
    print_banner(r"""
   _____ _       __         
  / ___/(_)___  / /_  __  __
  \__ \/ / __ \/ __ \/ / / /
 ___/ / / /_/ / /_/ / /_/ / 
/____/_/\____/_.___/\__, /  (created by shadow tracer[udulapasandul])
                   /____/   
    API-less Network Reconnaissance Tool
    """)
    
    parser = argparse.ArgumentParser(description="PySeeker - API-less Network Reconnaissance Tool")
    parser.add_argument('-d', '--domain', required=True, help="Target domain name (e.g., example.com)")
    parser.add_argument('-p', '--ports', default='1-1024', help="Port range to scan (e.g., 22,80,443 or 1-1024)")
    parser.add_argument('-s', '--skip-subdomains', action='store_true', help="Skip subdomain discovery")
    parser.add_argument('-v', '--skip-vuln-check', action='store_true', help="Skip vulnerability checking")
    
    args = parser.parse_args()
    
    domain = args.domain
    ports = parse_ports(args.ports)
    
    print_info(f"[*] Target: {domain}")
    print_info(f"[*] Port range: {args.ports}")
    
    # Resolve domain
    ip = resolve_domain(domain)
    if not ip:
        print_error("[!] Failed to resolve domain. Exiting.")
        return
    
    print_success(f"[+] Resolved {domain} to {ip}")
    
    # Subdomain discovery (optional)
    subdomains = []
    if not args.skip_subdomains:
        wordlist_path = get_wordlist_path()
        if not os.path.exists(wordlist_path):
            print_error(f"[!] Wordlist not found at {wordlist_path}")
        else:
            subdomains = discover_subdomains(domain, wordlist_path)
            print_info(f"[*] Found {len(subdomains)} subdomains")
    
    # Port scanning
    open_ports = run_port_scan(ip, ports)
    print_info(f"[*] Scan complete. Found {len(open_ports)} open ports.")
    
    # Service detection and vulnerability checking
    if open_ports and not args.skip_vuln_check:
        print_info("[*] Performing service detection...")
        for port in open_ports:
            banner = grab_banner(ip, port)
            if banner:
                print_success(f"[+] Port {port}: {banner}")
                check_vulnerabilities(banner)
            else:
                print_info(f"[*] Port {port}: Unknown service")
    
    print_success("[+] PySeeker scan complete!")

if __name__ == "__main__":
    main()
