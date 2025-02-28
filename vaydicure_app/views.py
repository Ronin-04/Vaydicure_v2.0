from django.shortcuts import render
from .models import Doctor
from django.http import JsonResponse


# Create your views here.
from django.http import HttpResponse
def mainpage(request):
    return render(request,"Mainpage.html")
def medicinepage(extracted_text):
    medicines = []

    if "paracetamol" in extracted_text:
        medicines.append("Paracetamol 500mg - Take 1 tablet twice daily after meals.")
    
    # Condition for Cough Syrup
    if "cough" in extracted_text:
        medicines.append("Corex Cough Syrup - 5ml twice daily.")

    # Condition for antibiotics (e.g., Amoxicillin)
    if "amoxicillin" in extracted_text or "antibiotic" in extracted_text:
        medicines.append("Amoxicillin 500mg - Take 1 capsule every 8 hours for 7 days.")

    # Condition for pain relief (e.g., Ibuprofen)
    if "ibuprofen" in extracted_text or "pain" in extracted_text:
        medicines.append("Ibuprofen 400mg - Take 1 tablet every 6-8 hours as needed for pain.")

    # Condition for fever (e.g., Acetaminophen)
    if "fever" in extracted_text or "acetaminophen" in extracted_text:
        medicines.append("Acetaminophen 500mg - Take 1 tablet every 4-6 hours for fever.")

    # Condition for diabetes (e.g., Metformin)
    if "diabetes" in extracted_text or "metformin" in extracted_text:
        medicines.append("Metformin 500mg - Take 1 tablet twice daily with meals.")

    # Condition for hypertension (e.g., Amlodipine)
    if "blood pressure" in extracted_text or "hypertension" in extracted_text or "amlodipine" in extracted_text:
        medicines.append("Amlodipine 5mg - Take 1 tablet daily for blood pressure control.")

    # Condition for cholesterol (e.g., Atorvastatin)
    if "cholesterol" in extracted_text or "atorvastatin" in extracted_text:
        medicines.append("Atorvastatin 10mg - Take 1 tablet daily to lower cholesterol levels.")

    # Condition for allergies (e.g., Cetirizine)
    if "allergy" in extracted_text or "cetirizine" in extracted_text:
        medicines.append("Cetirizine 10mg - Take 1 tablet once daily for allergy relief.")

    # Condition for acid reflux (e.g., Omeprazole)
    if "acid reflux" in extracted_text or "omeprazole" in extracted_text:
        medicines.append("Omeprazole 20mg - Take 1 tablet daily before meals for acid reflux.")

    # Condition for anxiety (e.g., Alprazolam)
    if "anxiety" in extracted_text or "alprazolam" in extracted_text:
        medicines.append("Alprazolam 0.25mg - Take 1 tablet as needed for anxiety.")

    # Condition for Asthma (e.g., Salbutamol)
    if "asthma" in extracted_text or "salbutamol" in extracted_text:
        medicines.append("Salbutamol Inhaler - 2 puffs every 4-6 hours as needed.")

    # Condition for Gastrointestinal Issues (e.g., Pantoprazole)
    if "gastritis" in extracted_text or "pantoprazole" in extracted_text:
        medicines.append("Pantoprazole 40mg - Take 1 tablet daily before breakfast.")

    # Condition for Insomnia (e.g., Zolpidem)
    if "insomnia" in extracted_text or "zolpidem" in extracted_text:
        medicines.append("Zolpidem 10mg - Take 1 tablet before bedtime for sleep.")

    # Condition for Depression (e.g., Sertraline)
    if "depression" in extracted_text or "sertraline" in extracted_text:
        medicines.append("Sertraline 50mg - Take 1 tablet daily for mood stabilization.")

    # Condition for Viral Infections (e.g., Oseltamivir for flu)
    if "influenza" in extracted_text or "oseltamivir" in extracted_text or "flu" in extracted_text:
        medicines.append("Oseltamivir 75mg - Take 1 capsule twice daily for 5 days for flu.")

    # Condition for Skin Infections (e.g., Clotrimazole for fungal infections)
    if "fungal infection" in extracted_text or "clotrimazole" in extracted_text:
        medicines.append("Clotrimazole Cream - Apply twice daily to the affected area for fungal infections.")

    # Condition for Heart Disease (e.g., Aspirin)
    if "heart disease" in extracted_text or "aspirin" in extracted_text or "blood thinner" in extracted_text:
        medicines.append("Aspirin 81mg - Take 1 tablet daily as a blood thinner for heart disease.")

    # Condition for Migraine (e.g., Sumatriptan)
    if "migraine" in extracted_text or "sumatriptan" in extracted_text:
        medicines.append("Sumatriptan 50mg - Take 1 tablet at the onset of migraine symptoms.")

    # Condition for Diarrhea (e.g., Loperamide)
    if "diarrhea" in extracted_text or "loperamide" in extracted_text:
        medicines.append("Loperamide 2mg - Take 1 tablet after each loose stool, up to 4 tablets per day.")

    # Condition for Constipation (e.g., Lactulose)
    if "constipation" in extracted_text or "lactulose" in extracted_text:
        medicines.append("Lactulose 10ml - Take 10ml once or twice daily to relieve constipation.")

    if "Oral Rehydration Salts" in extracted_text or "ORS" in extracted_text:
        medicines.append("Dissolve 1 sachet of ORS in 1 liter of clean water. Drink small sips frequently throughout the day. Duration: As needed to prevent dehydration.")
    

    # Default message if no specific recommendation found
    if not medicines:
        medicines.append("No specific medicine recommendation found.")

    return render(extracted_text,"Medicine.html")



def appointmentpage(request):
    return render(request,"Appointment.html")
    return redirect('/appointment/')


def urgentcarepage(request):
    return render(request,"Urgentcare.html")

def chatbot(request):
    return render(request,"Chatbotpage.html")
def doctorlist(request):
    doctors = Doctor.objects.all()
    return render(request, 'Doctors_list.html', {'doctors': doctors})

def get_doctors(request):
    # Check if there are doctors in the database
    doctors = Doctor.objects.all()

    # If no doctors are found, add the predefined ones
    if not doctors:
        doctor_data = [
            {
                "name": "Dr. John Doe",
                "specialization": "Cardiologist",
                "location": "New York",
                "contact_number": "1234567890",
                "available_days": "Mon-Fri",
                "available_time": "10 AM - 5 PM",
                "url": ""
            },
            {
                "name": "Dr. Jane Smith",
                "specialization": "Dermatologist",
                "location": "Los Angeles",
                "contact_number": "0987654321",
                "available_days": "Mon-Sat",
                "available_time": "9 AM - 4 PM",
                "url": ""
            },
            {
                "name": "Dr. Alice Brown",
                "specialization": "Neurologist",
                "location": "Chicago",
                "contact_number": "1122334455",
                "available_days": "Tue-Fri",
                "available_time": "11 AM - 6 PM",
                "url": ""
            }
        ]

        for data in doctor_data:
            Doctor.objects.update_or_create(
                name=data["name"],
                specialization=data["specialization"],
                location=data["location"],
                contact_number=data["contact_number"],
                available_days=data["available_days"],
                available_time=data["available_time"],
                url=data["url"]
            )

        # Fetch doctors again after inserting
        doctors = Doctor.objects.all()

    # Prepare data for JSON response
    doctor_list = [
        {
            "name": doctor.name,
            "specialization": doctor.specialization,
            "location": doctor.location,
            "contact_number": doctor.contact_number,
            "available_days": doctor.available_days,
            "available_time": doctor.available_time,
            "url": doctor.url
        } for doctor in doctors
    ]

    return JsonResponse({"doctors": doctor_list})