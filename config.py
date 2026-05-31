import argparse

parser = argparse.ArgumentParser(
    description="Python DNS Analyzer"
)

parser.add_argument(
    "--domain",
    help="Target domain"
)

parser.add_argument(
    "--type",
    default="A",
    help="DNS record type"
)

parser.add_argument(
    "--reverse",
    help="Perform reverse DNS lookup on IP"
)

args = parser.parse_args()

DOMAIN = args.domain
RECORD_TYPE = args.type.upper()
REVERSE_IP = args.reverse