filename1 = 'employee_data.txt'
filename2 = 'user_logs.txt'
employee_data = []
user_log = []

# Read the employee data & user log from the text file
with open(filename1, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(', ')
        employee = {}
        for item in data:
            key, value = item.split(': ')
            employee[key.strip()] = value.strip()
        employee_data.append(employee)

with open(filename2, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(', ')
        user = {}
        for item in data:
            key, value = item.split(': ')
            user[key.strip()] = value.strip()
        user_log.append(user)

accepted_0 = 0
accepted_1 = 0
accepted_2 = 0
accepted_3 = 0
accepted_4 = 0
rejected_0 = 0
rejected_1 = 0
rejected_2 = 0
rejected_3 = 0
rejected_4 = 0

divisions = ['Sales', 'Manager', 'Marketing', 'Manufacturer', 'Maintenance']

def access_card(card, room):
    has_access_card = False
    division = "null"
    id = -1
    
    for employee in employee_data:
        if card == employee['Access Card ID'] and room == employee['Division']:
            has_access_card = True
            division = employee['Division']
            id = int(employee['ID'])
            break
    
    return has_access_card, division, id
            
def division(div):
    for divs in divisions:
        if div == divs:
            return True
    return False

def worktime(id, time):
    for employee in employee_data:
        if id == int(employee['ID']):
            if int(time) >= int(employee['Start Time']) and int(time) <= int(employee['Finish Time']):
                return True
    return False

def pin(id, user_pin):
    for employee in employee_data:
        if id == int(employee['ID']):
            if (user_pin == employee['PIN']):
                return True
    return False     

def fingerprint(id, user_finger):
    for employee in employee_data:
        if id == int(employee['ID']):
            if (user_finger == employee['Fingerprint ID']):
                return True
    return False    

def level_one(user):
    access_card = False
    granted = False
    
    for employee in employee_data:
        if user['Scan Access Card'] == employee['Access Card ID']:
            access_card = True
    
    if access_card: granted = True
    
    # AccessCard => Granted
    if access_card and not granted:
        return False
    else:
        return True and granted

def level_two(user):
    granted = False
    has_access_card, div, id = access_card(user['Scan Access Card'], user['Room Area'])
    
    if has_access_card and division(div): granted = True
    
    # ∀x∃y AccessCard(x,y) ^ Division(y) => Granted(x)
    if not(has_access_card and division(div)) or granted:
        return True and granted
    else:
        return False

def level_three(user):
    granted = False
    has_access_card, div, id = access_card(user['Scan Access Card'], user['Room Area'])
    
    if has_access_card and division(div) and worktime(id, user['Time']): granted = True
    
    # ∀x∃y AccessCard(x,y) ^ Division(y) ^ Worktime(x) => Granted(x)
    if not(has_access_card and division(div) and worktime(id, user['Time'])) or granted:
        return True and granted
    else:
        return False
    
def level_four(user):
    granted = False
    has_access_card, div, id = access_card(user['Scan Access Card'], user['Room Area'])
    
    if has_access_card and division(div) and worktime(id, user['Time']) and pin(id, user['Input PIN']): granted = True
    
    # ∀x∃y AccessCard(x,y) ^ Division(y) ^ Worktime(x) ^ PIN(x) => Granted(x)
    if not(has_access_card and division(div) and worktime(id, user['Time']) and pin(id, user['Input PIN'])) or granted:
        return True and granted
    else:
        return False
    
def level_five(user):
    granted = False
    has_access_card, div, id = access_card(user['Scan Access Card'], user['Room Area'])
    
    if has_access_card and division(div) and worktime(id, user['Time']) and pin(id, user['Input PIN']) and fingerprint(id, user['Scan Fingerprint']): granted = True
    
    # ∀x∃y AccessCard(x,y) ^ Division(y) ^ Worktime(x) ^ PIN(x) ^ Fingerprint(x) => Granted(x)
    if not(has_access_card and division(div) and worktime(id, user['Time']) and pin(id, user['Input PIN']) and fingerprint(id, user['Scan Fingerprint'])) or granted:
        return True and granted
    else:
        return False

for user in user_log:
    if level_one(user):
        accepted_0 += 1
    else:
        rejected_0 += 1
    
    if level_two(user):
        accepted_1 += 1
    else:
        rejected_1 += 1
    
    if level_three(user):
        accepted_2 += 1
    else:
        rejected_2 += 1
    
    if level_four(user):
        accepted_3 += 1
    else:
        rejected_3 += 1
    
    if level_five(user):
        accepted_4 += 1
    else:
        rejected_4 += 1

print("Level One: (AccessCard => Granted)")
print(f"Accepted: {accepted_0}")
print(f"Rejected: {rejected_0}\n")

print("Level Two: (∀x∃y AccessCard(x,y) ^ Division(y) => Granted(x))")
print(f"Accepted: {accepted_1}")
print(f"Rejected: {rejected_1}\n")

print("Level Three: (∀x∃y AccessCard(x,y) ^ Division(y) ^ Worktime(x) => Granted(x))")
print(f"Accepted: {accepted_2}")
print(f"Rejected: {rejected_2}\n")

print("Level Four: (∀x∃y AccessCard(x,y) ^ Division(y) ^ Worktime(x) ^ PIN(x) => Granted(x))")
print(f"Accepted: {accepted_3}")
print(f"Rejected: {rejected_3}\n")

print("Level Five: (∀x∃y AccessCard(x,y) ^ Division(y) ^ Worktime(x) ^ PIN(x) ^ Fingerprint(x) => Granted(x))")
print(f"Accepted: {accepted_4}")
print(f"Rejected: {rejected_4}")