from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.forms import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Posts

posts = Posts.objects.all()


class PostListView(ListView):
    """
    View to display paginated list of all blog posts.
    """

    model = Posts
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5


class UserPostListView(ListView):
    """
    View to display posts by a specific user.
    """

    model = Posts
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        """
        Retrieve posts for a specific user.
        """
        try:
            user = get_object_or_404(User, username=self.kwargs.get("username"))
            return Posts.objects.filter(author=user).order_by("-date_posted")
        except Exception as e:
            messages.error(self.request, f"Error retrieving user posts: {str(e)}")
            return Posts.objects.none()


class LatestPostListView(ListView):
    """
    View to display the 3 most recent blog posts.
    """

    model = Posts
    template_name = "blog/latest_posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        try:
            return Posts.objects.all().order_by("-date_posted")[:3]
        except Exception as e:
            messages.error(self.request, f"Error retrieving latest posts: {str(e)}")
            return Posts.objects.none()


class PostDetailView(DetailView):
    """
    View to display details of a specific blog post.
    """

    model = Posts


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View to create a new blog post.
    """

    model = Posts
    fields = ["title", "content"]

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """
        Validate and save the post form.
        """
        try:
            form.instance.author = self.request.user
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"Error creating post: {str(e)}")
            return self.form_invalid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View to update an existing blog post.
    """

    model = Posts
    fields = ["title", "content"]

    def test_func(self) -> bool | None:
        """
        Check if the current user is the post author.
        """

        try:
            post = self.get_object()

            return self.request.user == post.author
        except Exception as e:
            messages.error(self.request, f"Error checking post permissions: {str(e)}")
            return False

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """
        Validate and save the updated post form.
        """
        try:
            form.instance.author = self.request.user
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"Error updating post: {str(e)}")
            return self.form_invalid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View to delete a blog post.
    """

    model = Posts
    success_url = "/"

    def test_func(self) -> bool | None:
        """
        Check if the current user is the post author.
        """
        try:
            post = self.get_object()

            return self.request.user == post.author
        except Exception as e:
            messages.error(self.request, f"Error checking post permissions: {str(e)}")
            return False


def about(request):
    """
    Render the about page.
    """
    try:
        return render(request, "blog/about.html", {"title": "About"})
    except Exception as e:
        messages.error(request, f"Error rendering about page: {str(e)}")
        return redirect("blog-home")


@login_required
def like_post(request, pk):
    """
    Allows logged-in users to like or unlike a post,
    automatically removing any existing dislike.

    """
    try:
        post = get_object_or_404(Posts, pk=pk)
        uList = post.likes.all()

        if request.user in uList:
            post.likes.remove(request.user)

        else:
            post.likes.add(request.user)
            post.dislikes.remove(request.user)

        return JsonResponse(
            {
                "likes": post.total_likes(),
                "dislikes": post.total_dislikes(),
                "liked": request.user in uList,
                "disliked": request.user in uList,
            }
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e),
                "likes": 0,
                "dislikes": 0,
                "liked": False,
                "disliked": False,
            },
            status=400,
        )


@login_required
def dislike_post(request, pk):
    """
    Allows logged-in users to dislike or undislike a post,
    automatically removing any existing like.
    """
    try:
        post = get_object_or_404(Posts, pk=pk)
        uList = post.dislikes.all()

        if request.user in uList:
            post.dislikes.remove(request.user)

        else:
            post.dislikes.add(request.user)
            post.likes.remove(request.user)

        return JsonResponse(
            {
                "likes": post.total_likes(),
                "dislikes": post.total_dislikes(),
                "liked": request.user in uList,
                "disliked": request.user in uList,
            }
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e),
                "likes": 0,
                "dislikes": 0,
                "liked": False,
                "disliked": False,
            },
            status=400,
        )
