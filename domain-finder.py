import whois
from itertools import product

c = 1
file1 = open("domains-available.txt", "w")
alphabet = "abcdefghijklmnopqrstuvwxyz"  # Letters you would like to use.
domain_length = 4
for x in product(alphabet, repeat=domain_length):
    pref = "".join(x)  # Separate pref variable to set additional conditions for domain.
    domain = pref + ".ee"
    c += 1

    # Example condition, checks if pattern is ABBA. Feel free to change.
    # If you don't want to use then just set it to: condition = True
    condition = (pref[0] == pref[3]) and (pref[1] == pref[2])

    if c % 1000 == 0:
        print(c)  # Shows that program works in console.
    if condition and whois.whois(domain).status is None:
        file1.write(domain + "\n")

file1.close()
print("Done!")
