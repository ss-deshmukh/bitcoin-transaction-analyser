import json
import random
from datetime import datetime, timedelta

def generate_random_addresses(num):
    base = "1BoatSLRHtKNngkdXEeobR76b53LETtpyT"
    addresses = []
    for i in range(num):
        # Generate mock address by changing some characters randomly
        random_address = ''.join(random.choices(base, k=len(base)))
        addresses.append({
            "address": random_address,
            "times_in_mixer": random.randint(0, 10),
            "criminal_activities": random.randint(0, 5),
            "high_volume_transactions": random.randint(0, 20),
            "last_active_date": (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
        })
    return addresses

# Number of addresses to generate
num_addresses = 1000
btc_addresses = generate_random_addresses(num_addresses)

# Saving the addresses to a JSON file
with open('btc_addresses.json', 'w') as json_file:
    json.dump(btc_addresses, json_file, indent=4)

print(f"Generated {num_addresses} mock Bitcoin addresses and saved to btc_addresses.json")
