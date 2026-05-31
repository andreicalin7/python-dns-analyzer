import dns.resolver
from logger import log_result
from colorama import Fore


def resolve_domain(domain, record_type):

    try:

        result = dns.resolver.resolve(domain, record_type)

        print(Fore.GREEN + f"\n{record_type} Records for {domain}:\n")

        for record in result:
            record_message = f"{domain} {record_type} -> {record}"

            print(Fore.CYAN + record_message)

            log_result(record_message)


    except dns.resolver.NXDOMAIN:

        print(Fore.RED + "Domain does not exist.")


    except dns.resolver.NoAnswer:

        print(Fore.YELLOW + f"No {record_type} records found.")


    except Exception as error:

        print(Fore.RED + f"Unexpected error: {error}")

def reverse_lookup(ip):

    try:

        result = dns.resolver.resolve_address(ip)

        print(Fore.GREEN + f"\nReverse DNS for {ip}:\n")

        for record in result:

            record_message = f"{ip} -> {record}"

            print(Fore.CYAN + record_message)

            log_result(record_message)


    except dns.resolver.NXDOMAIN:

        print(Fore.RED + "Domain does not exist.")


    except dns.resolver.NoAnswer:

        print(Fore.YELLOW + f"No {record_type} records found.")


    except Exception as error:

        print(Fore.RED + f"Unexpected error: {error}")