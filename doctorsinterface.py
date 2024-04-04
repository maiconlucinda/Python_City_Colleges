
import patient_data
patients = patient_data.patients

patient_id = input("Please, Enter the Patient ID: ")
#print(patient_id[0])


if patients.get(patient_id) == None:
    print("This ID does not exist, try again")
    exit()


patient_data = patients.get(patient_id)
#print(patient_data)

patient_name = patient_data["name"]
patient_age = patient_data["age"]
patient_gender = patient_data["gender"]
patient_diagnosis = patient_data["diagnosis"]
patient_allergies = patient_data["allergies"]
number_of_medications = len(patient_data["medications"])
number_of_allergies = len(patient_data["allergies"])

print(patient_name, patient_age, patient_gender, patient_diagnosis, patient_allergies, number_of_medications, number_of_allergies)