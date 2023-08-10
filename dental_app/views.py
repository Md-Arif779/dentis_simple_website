from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request, 'home.html')

    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # send an email
        send_mail(
            subject,
            f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}",
            email,
            ['arifmahmudovi997@gmail.com'],  # Replace with the recipient email address(es)
        )

        # Return a response or redirect to a success page
        
        return render(request, 'contact.html', {'name': name, 'email': email, 'subject': subject, 'phone': phone, 'message': message })  # Optionally, pass a variable to display success message
    else:
        return render(request, 'contact.html')
    

from django.shortcuts import render

from django.shortcuts import render

def apointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_email = request.POST['your-email']
        your_days = request.POST['your-days']
        your_phone = request.POST['your-phone']
        your_address = request.POST['your-address']
        your_scheldule = request.POST['your-scheldule']
        message = request.POST['message']

        appointment = "Name: " + your_name + "Email: " + your_email + "Phone: " + your_phone + "Days: " + your_days + "Adress: " + your_address + "Scheldule: " + your_scheldule + "Meassage: " + message

        send_mail(
            'Appointment Request',
            appointment,
            your_email,
            ['arifmahmudovi997@gmail.com'],         
        )

        return render(request, 'apointment_sure.html', {'your_name': your_name, 'your_email': your_email, 'your_days': your_days, 'your_phone': your_phone, 'your_address': your_address, 'your_scheldule': your_scheldule, 'message': message })
    else:
        return render(request, 'apointment.html')

def apointment_sure(request):
    # This view can be left empty for now or you can add some content to display
    return render(request, 'apointment_sure.html')


        


    
def about(request):
    return render(request, 'about.html')



def services(request):
    return render(request, 'services.html')    
