from django.db import models


class Key_word(models.Model):
    id = models.BigAutoField(primary_key=True)
    key_word = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} {self.key_word}'


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_title = models.CharField(max_length=100)
    post_annotation = models.CharField(max_length=200)
    post_text = models.TextField()
    key_words = models.ManyToManyField(Key_word, blank=True)
    post_image = models.ImageField(upload_to="static/images", verbose_name='photo', blank=True)

    def __str__(self):
        return f'{self.id} {self.post_title}'


