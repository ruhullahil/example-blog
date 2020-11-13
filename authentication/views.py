from django.http import Http404
from django.shortcuts import render,redirect
from .register_form import Registerform


# LOGIN VIEW ENDPOINT

def register(request):
    if request.method =='POST': 
        regestr = Registerform(request.POST)


        if regestr.is_valid():
            post = regestr.save(commit = False)
            post.set_password(post.password) 
            post.save()
            return redirect('all-posts')
        else:
            return render(request, "registration.html", {'form':regestr}) 
    else :
        form = Registerform(data= None)    
        return render(request, 'registration.html',{'form': form})