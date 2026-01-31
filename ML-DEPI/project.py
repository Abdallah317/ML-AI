import os

# global file location
my_csv = "employees.csv"

class EmployeeManager:
    def __init__(self):
        # self.data will be the dict
        self.data = {}
        
        # if file is not there, create it with header
        if not os.path.exists(my_csv):
            f = open(my_csv, "w")
            f.write("ID,Name,Position,Salary,Email\n")
            f.close()
        else:
            # load it manually
            f = open(my_csv, "r")
            lines = f.readlines()
            f.close()
            # skip first line (header)
            for i in range(1, len(lines)):
                row = lines[i].strip().split(",")
                if len(row) == 5:
                    eid = row[0]
                    self.data[eid] = {
                        "id": row[0], "name": row[1], 
                        "pos": row[2], "sal": int(row[3]), "email": row[4]
                    }

    def save_all(self):
        # rewrite everything manually
        f = open(my_csv, "w")
        f.write("ID,Name,Position,Salary,Email\n")
        for k in self.data:
            d = self.data[k]
            # building string line by line
            line = str(d['id']) + "," + d['name'] + "," + d['pos'] + "," + str(d['sal']) + "," + d['email'] + "\n"
            f.write(line)
        f.close()

    def add_emp(self):
        print("\n--- NEW EMP ---")
        num = input("ID: ")
        if num in self.data:
            print("Already exists!")
            return
            
        nm = input("Name: ")
        job = input("Job: ")
        s_raw = input("Salary (like 5k or 5000): ").lower()
        
        # manual conversion
        if "k" in s_raw:
            val = int(s_raw.replace("k", "")) * 1000
        else:
            val = int(s_raw)
            
        mail = input("Email: ")
        
        # store it
        self.data[num] = {"id": num, "name": nm, "pos": job, "sal": val, "email": mail}
        self.save_all()
        print("Saved.")

    def list_all(self):
        print("\nList of People:")
        for k in self.data:
            e = self.data[k]
            # very basic print
            print(e['id'] + " | " + e['name'] + " | " + e['pos'] + " | " + str(e['sal']))

    def update_emp(self):
        target = input("ID to edit: ")
        if target in self.data:
            obj = self.data[target]
            
            # asking one by one
            print("Editing " + obj['name'])
            
            x1 = input("New Name (enter to skip): ")
            if x1 != "": obj["name"] = x1
            
            x2 = input("New Job (enter to skip): ")
            if x2 != "": obj["pos"] = x2
                
            x3 = input("New Salary (like 10k): ")
            if x3 != "":
                if "k" in x3.lower():
                    obj["sal"] = int(x3.lower().replace("k","")) * 1000
                else:
                    obj["sal"] = int(x3)

            x4 = input("New Email: ")
            if x4 != "": obj["email"] = x4
            
            self.save_all()
            print("Updated.")
        else:
            print("Not found.")

    def delete_emp(self):
        did = input("ID to remove: ")
        if did in self.data:
            # using pop to delete
            self.data.pop(did)
            self.save_all()
            print("Deleted.")
        else:
            print("No ID match.")

    def search_emp(self):
        sid = input("Search ID: ")
        if sid in self.data:
            print("Result: " + str(self.data[sid]))
        else:
            print("Nothing.")

if __name__ == "__main__":
    # making the object
    run = EmployeeManager()
    
    while True:
        print("\n1.Add 2.Show 3.Edit 4.Delete 5.Search 6.Exit")
        c = input("Choice: ")
        
        if c == '1': run.add_emp()
        elif c == '2': run.list_all()
        elif c == '3': run.update_emp()
        elif c == '4': run.delete_emp()
        elif c == '5': run.search_emp()
        elif c == '6': break