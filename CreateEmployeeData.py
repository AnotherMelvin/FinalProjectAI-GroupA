import random
import hashlib

def generate_employee_data(num_employees):
    divisions = ['Sales', 'Manager', 'Marketing', 'Manufacturer', 'Maintenance']
    worktimes = {
        'Sales': [[8,12], [14,18]],
        'Manager': [[10,14], [16,20]],
        'Marketing': [[8,12], [14,18]],
        'Manufacturer': [[10,14], [16,20]],
        'Maintenance': [[18,20]]
    }
    employee_data = []
    i = 1

    for _ in range(num_employees):
        employee_id = i
        pin = generate_pin()
        access_card_id = generate_access_card_id()
        fingerprint_id = generate_fingerprint_id(employee_id)
        division = random.choice(divisions)
        work_time = random.choice(worktimes[division])
        employee_data.append({'ID': employee_id, 'PIN': pin, 'Access Card ID': access_card_id, 'Fingerprint ID': fingerprint_id, 'Division': division, 'Start Time': work_time[0], 'Finish Time': work_time[1]})
        i += 1

    return employee_data

def generate_pin():
    return random.randint(1000, 9999)

def generate_access_card_id():
    return random.randint(100000, 999999)

def generate_fingerprint_id(employee_id):
    hash_object = hashlib.sha256(str(employee_id).encode())
    return hash_object.hexdigest()

# Generate employee data
employees = generate_employee_data(50)

# Save the employee data to a text file
filename = 'employee_data.txt'
with open(filename, 'w') as file:
    for employee in employees:
        file.write(f"ID: {employee['ID']}, PIN: {employee['PIN']}, Access Card ID: {employee['Access Card ID']}, Fingerprint ID: {employee['Fingerprint ID']}, Division: {employee['Division']}, Start Time: {employee['Start Time']}, Finish Time: {employee['Finish Time']}\n")

print(f"Employee data saved to {filename}.")