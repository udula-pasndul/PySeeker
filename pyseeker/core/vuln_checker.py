# pyseeker/core/vuln_checker.py
from ..utils.logger import print_info, print_warning

# A small, static database of known vulnerable software versions.
# In a real-world scenario, this would be much larger.
VULN_DB = {
    "Apache/2.4.29": ["CVE-2019-0211 (Apache Privilege Escalation)"],
    "OpenSSH_7.2p2": ["CVE-2016-10012 (OpenSSH Auth Bypass)"],
    "vsftpd 2.3.4": ["CVE-2011-2523 (vsftpd Backdoor)"],
    "nginx/1.14.0": ["CVE-2019-20372 (nginx memory exhaustion)"],
    "nginx/1.14": ["CVE-2019-20372 (nginx memory exhaustion)"],
    "nginx/1.16": ["CVE-2019-20372 (nginx memory exhaustion)"],
    "Apache/2.4": ["CVE-2019-0211 (Apache Privilege Escalation)"],
    "Apache/2.2": ["CVE-2017-15710 (Apache mod_session_crypto)"],
    "OpenSSH": ["CVE-2016-10012 (OpenSSH Auth Bypass)"],
    "ProFTPD": ["CVE-2019-12815 (ProFTPD mod_copy)"],
    "MySQL": ["CVE-2019-2628 (MySQL Privilege Escalation)"],
    "PostgreSQL": ["CVE-2019-10164 (PostgreSQL Privilege Escalation)"],
}

def check_vulnerabilities(service_info):
    """
    Checks a service string against the local vulnerability database.
    Returns True if vulnerabilities were found, False otherwise.
    """
    print_info("[*] Checking for vulnerabilities in identified services...")
    found_vulns = False
    
    if not service_info:
        print_info("[*] No service info provided for vulnerability check.")
        return False
    
    for service, cves in VULN_DB.items():
        if service.lower() in service_info.lower():
            found_vulns = True
            print_warning(f"[!!!] POTENTIAL VULNERABILITY FOUND!")
            print_warning(f"    Service: {service}")
            print_warning(f"    Banner: {service_info}")
            for cve in cves:
                print_warning(f"    -> {cve}")
    
    if not found_vulns:
        print_info("[*] No vulnerabilities found in the local database for the detected services.")
    
    return found_vulns
