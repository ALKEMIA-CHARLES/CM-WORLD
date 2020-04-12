from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from worldwatch.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from worldwatch.forms import UserUpdateForm
from worldwatch.forms import CommentForm
# Create your views here.


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "main/signup.html", context={'form': form})


class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "main/index.html"
    context_object_name = "posts"
    ordering =['-post_date']

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "main/detail.html"

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "main/postform.html"
    fields = ['title', 'message', 'image']

    def form_valid(self, form):
        form.instance.masterpost = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = "main/updateform.html"
    fields = ['image','title','message']


    def form_valid(self, form):
        form.instance.masterpost = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.masterpost:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'main/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.masterpost:
            return True
        return False

    
@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user.profile)
    return render(request, "main/profile.html", context={"form":form})

def post_comments(request, postid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        print(postid)
        if form.is_valid():
            c_form=form.save(commit=False)
            c_form.post = get_object_or_404(Post,id=postid)
            c_form.user=request.user
            print(c_form)
            c_form.save()
            return redirect('index')
    else:
        form = CommentForm()
    return render(request, "main/commentform.html", context={"form":form, })