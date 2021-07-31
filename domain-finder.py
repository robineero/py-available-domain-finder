import whois
from itertools import product

domains_available = open("domains_available.txt", "w")
alphabet = "abcdefghijklmnopqrstuvwxyz"  # Letters you would like to use.
domain_length = 3
for x in product(alphabet, repeat=domain_length):
    body = "".join(x)  # Separate pref variable to set additional conditions for domain.
    domain = body + ".ee"

    # Example condition, checks if pattern is ABA. Feel free to change.
    # If you don't want to use then just set it to: condition = True
    condition = (body[0] == body[2])

    if condition and whois.whois(domain).status is None:
        print(f"{domain} - available")
        domains_available.write(domain + "\n")

domains_available.close()
print("Done!")
