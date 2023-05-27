import random

filename = 'user_logs.txt'
user_log = []

# Read the user log data from the text file
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(', ')
        user = {}
        for item in data:
            key, value = item.split(': ')
            user[key.strip()] = value.strip()
        user_log.append(user)
        
def malicious_entry():
    i = 0
    target = shuffler(generate_random_numbers())
    
    print(target)
    
    for _ in range(14):
        swap_data(target[i][0], target[i][1], 'Scan Access Card')
        
        if binary():
            swap_data(target[i][0], target[i][1], 'Room Area')
            
            if binary():
                swap_data(target[i][0], target[i][1], 'Input PIN')
                
                if far():
                    if binary():
                        user_log[target[i][0]]['Scan Fingerprint'] = user_log[target[i][1]]['Scan Fingerprint']
                    else:
                        user_log[target[i][1]]['Scan Fingerprint'] = user_log[target[i][0]]['Scan Fingerprint']
            else:
                user_log[target[i][0]]['Scan Fingerprint'] = "null"
                user_log[target[i][1]]['Scan Fingerprint'] = "null"
        else:
            user_log[target[i][0]]['Scan Fingerprint'] = "null"
            user_log[target[i][1]]['Scan Fingerprint'] = "null"
                
        i += 1

def swap_data(x, y, cat):
    z = user_log[x][cat]
    user_log[x][cat] = user_log[y][cat]
    user_log[y][cat] = z

def generate_random_numbers():
    return random.sample(range(100), 28)

def shuffler(numbers):
    random_array = []
    random.shuffle(numbers)
    for i in range(0, len(numbers), 2):
        entry = [numbers[i], numbers[i+1]] if i+1 < len(numbers) else [numbers[i]]
        random_array.append(entry)
    return random_array

def binary():
    return random.choice([True, False])

def far():
    chance = 0.00001
    if random.random() < chance:
        return True
    else:
        return False

# Generate malicious entry on user logs
malicious_entry()

for user in user_log:
    print(f"Time: {user['Time']}, Scan Access Card: {user['Scan Access Card']}, Input PIN: {user['Input PIN']}, Scan Fingerprint: {user['Scan Fingerprint']}, Room Area: {user['Room Area']}")

# Save the new user log data to a text file
with open(filename, 'w') as file:
    for entry in user_log:
        file.write(f"Time: {entry['Time']}, Scan Access Card: {entry['Scan Access Card']}, Input PIN: {entry['Input PIN']}, Scan Fingerprint: {entry['Scan Fingerprint']}, Room Area: {entry['Room Area']}\n")

print(f"Malicious entry saved to {filename}.")
    