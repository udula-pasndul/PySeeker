 
# pyseeker/utils/logger.py
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_banner(text):
    print(f"{Fore.CYAN}{Style.BRIGHT}{text}")

def print_info(text):
    print(f"{Fore.BLUE}{text}")

def print_success(text):
    print(f"{Fore.GREEN}{text}")

def print_warning(text):
    print(f"{Fore.YELLOW}{text}")

def print_error(text):
    print(f"{Fore.RED}{text}")