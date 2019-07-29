#!/usr/bin/env python3
# Obtains the status codes from a list of domains in `domain_list.txt`
# and outputs as JSON list of dictionaries.

# Standard Library
import json

# Third Party
import requests


def main():
    filename = "domain_list.txt"
    with open(filename, "r") as domain_list:
        domains = []
        for domain in domain_list:
            domain = domain.strip()
            request = requests.get(domain)
            ret = {"domain": domain, "status": request.status_code}
            domains.append(ret)
    output_list = json.dumps(domains, indent=4)
    print(output_list)


if __name__ == "__main__":
    main()
