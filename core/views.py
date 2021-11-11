from django.shortcuts import render, redirect
from .models import RegisterStudent
from .forms import RegisterForm, RegiserFormCustom


# Create your views here.

def createRegister(request):
    if request.method == 'POST':
        form = RegiserFormCustom(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                RegisterStudent.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')

    else:
        form = RegiserFormCustom()
    return render(request, 'core/index.html', {'form': form})

# def createRegister(request):
#     if request.method == "POST":
#         form = RegiserFormCustom(request.POST)
#         if form.is_valid():
#             try:
#                 RegisterStudent.objects.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#     return render(request, 'core/index.html', {"form":form})
