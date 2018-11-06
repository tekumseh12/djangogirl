from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import formular
from . import model_kal
def kalkulacka(request):
    return render(request,"kal.html", {})

def post(request):
    post = Post.objects.all()
    return render(request, 'post.html', {'posts':post})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'posts':post})
def Formular(request):
    if request.method == "POST":
        form = formular(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
            
    else:
        form = formular()
        return render(request, 'formular.html', {'form':form})

def kal_py(request):
    vysledok = None
    msg_error = None
    if request.method == "POST":
        try:
            a = float(request.POST["a"])
            b = float(request.POST["b"])
        except:
            msg_error = "A alebo B neni cislo"
            return render(request,"kal_py.html", {"err_msg":msg_error})
        if request.POST["operator"] == "+":
                  vysledok=model_kal.secti(a,b)
        if request.POST["operator"] == "*":
                  vysledok=model_kal.vynasob(a,b)
        if request.POST["operator"] == "-":
                  vysledok=model_kal.odcitaj(a,b)
        if request.POST["operator"] == "/" and b == 0:
                msg_error = "delit nulou sa neda"
                return render(request,"kal_py.html", {"err_msg":msg_error})
        if request.POST["operator"] == "/":
                 vysledok=model_kal.vydel(a,b)
        return render(request,"kal_py.html", {"vysledok":vysledok})          
                  
    else:
         return render(request,"kal_py.html", {})
