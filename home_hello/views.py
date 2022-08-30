from django.shortcuts import render


def home(request):
	name = request.GET.get('name')
	message = request.GET.get('message')
	return render(request, 'home_hello/home.html', {'name': name, 'msg': message})
