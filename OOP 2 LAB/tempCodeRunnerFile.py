class Person:
    total_people = 0

    def __init__(self, name="Unknown", age=0, contact="N/A"):
        self.name = name
        self.age = age
        self.contact = contact
        Person.total_people += 1

    @classmethod
    def from_default(cls):
        return cls()

    @classmethod
    def from_details(cls, name, age, contact):
        return cls(name, age, contact)

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Contact: {self.contact}"


class Patient(Person):
    def __init__(self, name="Unknown", age=0, contact="N/A"):
        super().__init__(name, age, contact)
        self.appointments = []

    def add_appointment(self, doctor_name, date, time):
        self.appointments.append((doctor_name, date, time))

    def display(self):
        details = super().display()
        details += "\nAppointments:\n"
        for appointment in self.appointments:
            details += f"  - Doctor: {appointment[0]}, Date: {appointment[1]}, Time: {appointment[2]}\n"
        return details


class Doctor(Person):
    def __init__(self, name="Unknown", age=0, contact="N/A", specialization="General"):
        super().__init__(name, age, contact)
        self.specialization = specialization
        self.assigned_patients = []

    def assign_patient(self, patient_name):
        self.assigned_patients.append(patient_name)

    def display(self):
        details = super().display()
        details += f"\nSpecialization: {self.specialization}\nAssigned Patients:\n"
        for patient in self.assigned_patients:
            details += f"  - {patient}\n"
        return details


if __name__ == "__main__":
    patient1 = Patient.from_details("Tausif", 22, "123-456-7890")
    patient2 = Patient.from_details("Ritu", 21, "987-654-3210")

    patient1.add_appointment("Dr. Rafi", "2024-11-23", "10:00 AM")
    patient1.add_appointment("Dr. Mursalin", "2024-11-24", "2:00 PM")
    patient2.add_appointment("Dr. Rafi", "2024-11-23", "11:00 AM")

    doctor1 = Doctor.from_details("Dr. Rafi", 45, "555-123-4567", "Cardiologist")
    doctor2 = Doctor.from_details("Dr. Mursalin", 50, "555-987-6543", "Neurologist")

    doctor1.assign_patient(patient1.name)
    doctor1.assign_patient(patient2.name)
    doctor2.assign_patient(patient1.name)

    print("Patient Information:")
    print(patient1.display())
    print(patient2.display())

    print("\nDoctor Information:")
    print(doctor1.display())
    print(doctor2.display())

    print(f"\nTotal People in the System: {Person.total_people}")
