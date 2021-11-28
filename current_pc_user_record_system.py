def Get_event_date(events):
    return events.dates
def current_user(events):
    events.sort(key = Get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        if event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines
def generate_report(machines):
    for machine,users in machines.items():
        if len(users) > 0:
            user_list = " , ".join(users)
            print(f"{machine}: {user_list}")
            with open("user_data.txt", "a+") as f:
                f.write(f"{machine}: {user_list}\n")
    print("Report file created.")

class Event:
    def __init__(self,event_date,event_type,machine_name,user):
        self.dates = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'Ayan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'Supriya'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'Supriya'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'Ayan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'Sachin'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'Rahul'),
]

users = current_user(events)
print(users)
generate_report(users)

