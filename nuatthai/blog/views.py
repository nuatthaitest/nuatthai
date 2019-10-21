from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
    }
    return render(request, 'blog/home.html', context)



def reservation_home(request):
    context = {
        'service': 'service'
    }
    return render(request, 'blog/reservation_home.html', context)

def login(request):
    return render(request, 'users/login.html')

def _05ReservationSearchPage(request):
    return render(request, 'blog/_05ReservationSearchPage.html')

    

def _08SummaryPage(request):
    return render(request, 'blog/_08SummaryPage.html')

def _09CompletedPage(request):
    return render(request, 'blog/_09CompletedPage.html')

def _11AdminStaffHomePage(request):
    return render(request, 'blog/_11AdminStaffHomePage.html')

def _12StaffHomePage(request):
    return render(request, 'blog/_12StaffHomePage.html')




class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

