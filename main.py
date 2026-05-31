from colorama import init

from config import DOMAIN, RECORD_TYPE, REVERSE_IP
from resolver import resolve_domain, reverse_lookup


init(autoreset=True)


if REVERSE_IP:

    reverse_lookup(REVERSE_IP)

else:

    resolve_domain(DOMAIN, RECORD_TYPE)