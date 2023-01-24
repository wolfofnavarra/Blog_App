from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def PostList(request):
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(object_list, 3) #replace paginate_by = 3
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # if not integer, we deliver fisrt page
        post_list = paginator.page(1)
    except EmptyPage:
        # if page is out of range, we return last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'index.html',
                  {'page': page,
                  'post_list': post_list})

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug = slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False) #create comment object but dont save to database yet.
            new_comment.post = post # assign current post to comment
            new_comment.save() # save the comment to the database

    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

