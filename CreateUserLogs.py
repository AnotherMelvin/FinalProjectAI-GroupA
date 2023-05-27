import random

filename = 'employee_data.txt'
employee_data = []

# Read the employee data from the text file
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(', ')
        employee = {}
        for item in data:
            key, value = item.split(': ')
            employee[key.strip()] = value.strip()
        employee_data.append(employee)

def generate_user_log(employee_data, num_entries):
    i = 1
    t = 8
    user_log = []
    
    for _ in range(num_entries):
        while True:
            employee = random.choice(employee_data)
            
            if t >= int(employee['Start Time']) and t <= int(employee['Finish Time']):
                break

        pin = employee['PIN']
        access_card_id = employee['Access Card ID']
        fingerprint_id = employee['Fingerprint ID']
        division = employee['Division']
        
        log_entry = f"Time: {t}, Scan Access Card: {access_card_id}, Input PIN: {pin}, Scan Fingerprint: {fingerprint_id}, Room Area: {division}\n"
        user_log.append(log_entry)
        i += 1
        
        if (i > 9):
            i = 1
            t += 1
    
    return user_log

# Generate user log for 100 entries
user_log = generate_user_log(employee_data, 100)

# Save the user log data to a text file
filename = 'user_logs.txt'
with open(filename, 'w') as file:
    for entry in user_log:
        file.write(entry)

print(f"User logs saved to {filename}.")