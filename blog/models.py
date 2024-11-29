from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    dislikes = models.ManyToManyField(User, related_name="disliked_posts", blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Get the canonical URL for the post.
        """
        try:
            return reverse("post-detail", kwargs={"pk": self.pk})
        except Exception as e:
            print(f"Error generating URL for post {self.pk}: {e}")
            return "/"
    
    def total_likes(self):
        return self.likes.count()
    
    def total_dislikes(self):
        return self.dislikes.count()
