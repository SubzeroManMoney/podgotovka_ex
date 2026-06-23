from django.shortcuts import render, redirect
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
