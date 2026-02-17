# pyseeker/core/subdomain_scanner.py
import dns.resolver
import dns.exception
from ..utils.logger import print_info, print_success, print_error


DEFAULT_SUBDOMAINS = ['www', 'mail', 'ftp', 'admin', 'test', 'dev', 'api', 'blog']

def discover_subdomains(domain, wordlist_path):
    """
    Discovers subdomains for a given domain using a wordlist.
    """
    print_info(f"[*] Starting subdomain discovery for: {domain}")
    subdomains_found = set()

    try:
        with open(wordlist_path, 'r') as f:
            subdomains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print_error(f"[-] Wordlist not found at {wordlist_path}. Using default small list.")
        subdomains = DEFAULT_SUBDOMAINS

    # Create a resolver with timeout settings
    resolver = dns.resolver.Resolver()
    resolver.timeout = 2
    resolver.lifetime = 2

    for sub in subdomains:
        full_domain = f"{sub}.{domain}"
        try:
            # Use DNS resolver to check for A records (IPv4 address)
            answers = resolver.resolve(full_domain, 'A')
            if answers:
                print_success(f"[+] Found subdomain: {full_domain}")
                subdomains_found.add(full_domain)
        except dns.resolver.NXDOMAIN:
            # This is expected for most subdomains, so we fail silently.
            pass
        except dns.resolver.NoAnswer:
            # No A record but domain exists
            pass
        except dns.resolver.Timeout:
            # DNS query timed out
            pass
        except dns.exception.DNSException as e:
            # Catch other DNS-related exceptions
            pass
        except Exception as e:
            print_error(f"[-] An unexpected error occurred: {e}")

    return list(subdomains_found)
