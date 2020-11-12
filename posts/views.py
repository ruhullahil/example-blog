from django.shortcuts import render
from django.http import HttpResponseNotFound  

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .service import service



# POSTS VIEW ENDPOINT
serve = service(root_url= 'https://jsonplaceholder.typicode.com')
def posts(request):
   
    response = serve.get('posts')
    if response !=404:   
        _posts = response

        page = request.GET.get('page', 1)

        paginator = Paginator(_posts, 10)
        try:
            _post = paginator.page(page)
        except PageNotAnInteger:
            _post = paginator.page(1)
        except EmptyPage:
            _post = paginator.page(paginator.num_pages)
  
        return render(request, 'blog-listing.html',{"posts":_post})

    return HttpResponseNotFound('<h1>Faild to request</h1>') 

    
    


# POST DETAILS VIEW ENDPOINT
def post_details(request):
    return render(request, 'blog-post.html')