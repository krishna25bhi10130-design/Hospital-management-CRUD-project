# Simple Hospital Management CRUD (All in one file)

patients = []   # List to store patient records
patient_id = 1  # Auto-increment ID

while True:
    print("\n===== HOSPITAL MANAGEMENT (CRUD) =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Update Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter choice: ")

    # CREATE
    if choice == "1":
        global patient_id
        name = input("Enter name: ")
        age = input("Enter age: ")
        disease = input("Enter disease: ")

        patient = {
            "id": patient_id,
            "name": name,
            "age": age,
            "disease": disease
        }
        patients.append(patient)
        print("Patient Added with ID:", patient_id)
        patient_id += 1
     # READ
    elif choice == "2":
        if not patients:
            print("No patients found!")
        else:
            for p in patients:
                print(f"\nID: {p['id']}")
                print(f"Name: {p['name']}")
                print(f"Age: {p['age']}")
                print(f"Disease: {p['disease']}")
                print("-------------------")

     # UPDATE
    elif choice == "3":
        update_id = int(input("Enter patient ID to update: "))
        found = False
        for p in patients:
            if p["id"] == update_id:
                p["name"] = input("New name: ")
                p["age"] = input("New age: ")
                p["disease"] = input("New disease: ")
                print("Patient Updated!")
                found = True
        if not found:
            print("Patient ID not found!")

    # DELETE
      elif choice == "4":
        delete_id = int(input("Enter patient ID to delete: "))
        found = False
        for p in patients:
            if p["id"] == delete_id:
                patients.remove(p)
                print("Patient Deleted!")
                found = True
        if not found:
            print("Patient ID not found!")

    # EXIT
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Enter 1 to 5.")