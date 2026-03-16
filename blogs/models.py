from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length=80)
    blog_body = models.CharField(max_length=130)

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    comment = models.CharField(max_length=180)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return self.comment




