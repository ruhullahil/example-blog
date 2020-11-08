from django.shortcuts import render
import requests

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# POSTS VIEW ENDPOINT
def posts(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code ==200 :
        print(response.json())
        _posts = response.json()

        page = request.GET.get('page', 1)

        paginator = Paginator(_posts, 10)
        try:
            _post = paginator.page(page)
        except PageNotAnInteger:
            _post = paginator.page(1)
        except EmptyPage:
            _post = paginator.page(paginator.num_pages)
  
        return render(request, 'blog-listing.html',{"posts":_post})
    


# POST DETAILS VIEW ENDPOINT
def post_details(request):
    return render(request, 'blog-post.html')