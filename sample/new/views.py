from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):

    return render(request,"home.html")

def register(request):
    if request.method == 'POST':
        # Extract form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        aadhar_number=request.POST.get('aadhar_number')

        # Check if passwords match
        if password != confirm_password:
            return redirect('register')

        # Create user
        user = User.objects.create_user(
            username=phone_number,  # Use phone number as username
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        # Create UserProfile
        UserProfile.objects.create(
            address=address,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            gender=gender,
            aadhar_number=aadhar_number
        )
        return redirect('user_login')

    return render(request,'register.html')


# views.py


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/schems')  # Redirect to home page after successful login
        else:
            return redirect('/user_login')
            # Display error message if authentication fails

    # Render login page for GET requests and POST requests with errors
    return render(request, 'login.html')


def welcome(request):
        return render(request,'login.html')

def help(request):
    if request.method == 'POST':
        name_of_scheme = request.POST.get('name_of_scheme')
        report_problem = request.POST.get('report_problem')

        # Create Help object
        help_instance = Help.objects.create(
            name_of_scheme=name_of_scheme,
            report_problem=report_problem
        )

        # Redirect to the homepage
        return redirect('/')
    return render(request, 'help.html')


from django.shortcuts import render, redirect
from .models import Feedback

def feedback(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        suggested = request.POST.get('suggested')

        # Create Feedback object
        feedback = Feedback.objects.create(
            rating=rating,
            suggested=suggested
        )

        # Redirect to the homepage
        return redirect('/')  # Replace '/' with the URL of your homepage if needed

    return render(request, 'feedback.html')


def schems(request):
    return render(request,'schems.html')
