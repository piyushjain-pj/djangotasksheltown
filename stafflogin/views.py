from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from stafflogin.forms import UserRegisterForm, PropertyOwnerForm
from stafflogin.models import UserRegistered, PropertyOwner

# Create your views here.
# Create your views here.


def index(request):
    print(request.user)
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    return render(request, 'sheltownstafflogin/staffHome.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/stafflogin")
        else:
            # No backend authenticated the credentials
            if user == None:
                msg = "Invalid Username! and Password!"
            return render(request, 'sheltownstafflogin/login.html', {'msg': msg})
    return render(request, 'sheltownstafflogin/login.html')


def logout_request(request):
    logout(request)
    return redirect("/stafflogin")


#Function to Display all User Registerd in Sheltown
@login_required
def user(request):
        # add the dictionary during initialization
        user = UserRegistered.objects.all()
        return render(request, 'sheltownstafflogin/userRegister.html', {'user': user})


#Function to Display all Property Ownes in Sheltown

@login_required
def owner(request):
    context={}
    context['data'] = PropertyOwner.objects.all()
    print(context['data'])
    return render(request, 'sheltownstafflogin/rentalpropertiesowner.html', context)

#Function to Display all Listed Properties in Sheltown


@login_required
def listing(request):
    return render(request, 'sheltownstafflogin/rentalpropertieslisted.html')

#To Add NEW USER


@login_required
def adduser(request):
    context = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/stafflogin/')
    else:
        form = UserRegisterForm()
        context['form'] = form
        return render(request, 'sheltownstafflogin/AddUser.html', context)

#To Add NEW Property Owner
@login_required
def addpropertyowner(request):
    context = {}
    if request.method == 'POST':
        form = PropertyOwnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/stafflogin/staff/user')
    else:
        form = PropertyOwnerForm()
        context['form'] = form
        return render(request, 'sheltownstafflogin/AddPropertyOwner.html', context)

#To Add New Property
@login_required
def addproperty(request):
    return render(request, 'sheltownstafflogin/AddProperty.html')


@login_required
def edituser(request, id):
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(UserRegistered, id=id)

    # pass the object as instance in form
    form = UserRegisterForm(request.POST or None, instance=obj)

    # save the data from the form and
    if form.is_valid():
        form.save()
        messages.success(request, 'User Record has been Updated Succefully.')
        return HttpResponseRedirect("/stafflogin/staff/user")

    # add form dictionary to context
    context["form"] = form
    return render(request, "sheltownstafflogin/EditUser.html", context)


@login_required
def editpropertyowner(request):
    return render(request, 'sheltownstafflogin/EditPropertyOwner.html')


@login_required
def editproperty(request):
    return render(request, 'sheltownstafflogin/EditProperty.html')


def deleteuser(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(UserRegistered, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        messages.success(request, 'User Record has been Deleted Succefully.')
        return HttpResponseRedirect("/stafflogin/staff/user")

    return render(request, "sheltownstafflogin/deleteuser.html", context)
