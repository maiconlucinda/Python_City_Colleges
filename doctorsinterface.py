
from datetime import datetime
import patient_data

patients = patient_data.patients


while True:

    # Getting the ID from user
    patient_id = input("Please, Enter the Patient ID: ")
    if patient_id == "Exit":
        exit()

    # Testing if the ID exists
    while patients.get(patient_id) == None:   
        print("This ID does not exist, try again")
        patient_id = input("Please, Enter the Patient ID: ")
        if patient_id == "Exit":
            exit()

    patient_data = patients.get(patient_id)




    #Patients name, age and gender.
    #The patient's diagnosis.
    #Medications and allergies and the number of Medications and number of allergies.
    patient_name = patient_data["name"]
    patient_age = patient_data["age"]
    patient_gender = patient_data["gender"]
    patient_diagnosis = patient_data["diagnosis"]
    patient_allergies = patient_data["allergies"]
    number_of_medications = len(patient_data["medications"])
    number_of_allergies = len(patient_data["allergies"])

    print(f"The Patient's name: {patient_name}")
    print(f"The Patient's age: {patient_age}")
    print(f"The Patient's gender: {patient_gender}")
    print(f"The Patient's diagnosis: {patient_diagnosis}")
    print(f"The Patient's allergies: {patient_allergies}")
    print(f"Patient's number of medications: {number_of_medications}")
    print(f"Patient's number of allergies: {number_of_allergies}")




    #The patients average blood pressure.
    systolic = 0
    diastolic = 0
    index = 0
    for values in patient_data["blood_pressure_checks"]:
        index += 1
        systolic += values[0]
        diastolic += values[1]

    systolic = systolic / index
    diastolic = diastolic / index
    patient_average_blood_pressure = f"{systolic}/{diastolic}"



    # Whether the patients average blood pressure is High, Normal or Low
    blood_pressure_category = "None"
    if systolic > 125 or diastolic > 85:
        blood_pressure_category = "High"
    elif systolic > 115 or diastolic > 75:
        blood_pressure_category = "Normal"
    elif systolic < 115 and diastolic < 75:
        blood_pressure_category = "Low"
    else:
        print("There might be something wrong with the data")

    print(f"The patient's average blood pressure is: {blood_pressure_category}")   




    # The time difference between the patients last checkup and next appointment.
    if patient_data["next_appointment_date"] == "No-Date":
        print(f"The Patient {patient_id} doesn't have an upcoming appointment.")
    else:
        date1 = datetime.strptime(patient_data['last_checkup_date'], '%Y-%m-%d')
        date2 = datetime.strptime(patient_data['next_appointment_date'],'%Y-%m-%d')
        time_difference = (date2-date1).days
        print(f"Patient {patient_id}: There are {time_difference} days from the last appointment to the next appointment")




    # Ask the doctor for a medication and then add medication to the patient's medication list.
    medication_to_add = input("Please, enter the medication's name, if there is no medication to be prescribed, enter 'None': ")  
   
    for allergies in patient_data["allergies"]:

        if allergies == medication_to_add:
            print(f"The Patient {patient_id} is allergic to {medication_to_add}.")
        else:
            medication_exists = False
            if medication_to_add == "None":
                medication_exists = None
            else:
                for medication in patient_data["medications"]:
                    if medication == medication_to_add:
                        medication_exists = True

            if medication_exists == False:
                patient_data["medications"].append(medication_to_add)




    # Ask the doctor for a medication and then remove medication from the patient's medication list.
    medication_remove = input("Please, enter the medication to be remeved from the patient's medication list: ")

    medication_exists_remove = None
    index = -1
    for medication in patient_data["medications"]:
        index += 1
        if medication == medication_remove:
            patient_data["medications"].pop(index)