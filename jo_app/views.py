from django.shortcuts import render, redirect, get_object_or_404
from jo_app.models import Clients, Users

# Create your views here.
login = ""
password = ""
def index(request):
    global login, password
    login = request.GET.get('login', '')
    password = request.GET.get('password', '')
    print("user's login: " + login)
    print("user's pass: " + password)
    user = Users.objects.filter(login=login).first()
    print(request.resolver_match.url_name)
    if user is not None:
        print("user exists")
        if user.pass_field == password:
            print("password match")
            request.session['user_id'] = user.id
            return redirect('tables')
        else:
            print("password " + password + " not match")
    else:
        print("user " + login + " does not exist")
    return render(request, 'login.html')

def tables(request):
    if request.GET.get('back') == "true":
        return redirect('login')
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    if request.GET.get('edit') is not None:
        request.session['edit_id'] = request.GET.get('edit')
        return redirect('edit')

    search = request.GET.get('search', '')
    tabless = Clients.objects.all()
    if search != '':
        tabless = tabless.filter(secondname__icontains=search)

    user = Users.objects.get(id=user_id)
    context = {
        'isadmin': user.isadmin,
        'clients': tabless,
        'serach': search,
    }
    return render(request, 'tables.html', context)

def edit(request):
    edit_id = request.session.get('edit_id')
    client = get_object_or_404(Clients, id=edit_id)
    context = {
        'edit': edit_id,
        'client': client,
    }
    if request.method == 'POST':
        client.secondname = request.POST.get('secondname')
        client.firstname = request.POST.get('firstname')
        client.phone = request.POST.get('phone')
        client.bday = request.POST.get('bday')
        client.gender = request.POST.get('gender')
        client.category = request.POST.get('category')
        client.save()
        return redirect('tables')

    return render(request, 'edit.html', context)