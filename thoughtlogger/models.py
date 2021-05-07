from django.db import models



# Create your models here.
class Activity(models.Model):
    activity_text = models.CharField(max_length=200)
    create_date = models.DateTimeField('create date')

    def __str__(self):
        return self.activity_text

class ThoughtCategory(models.Model):
    thought_category_text = models.CharField(max_length=200)

    def __str__(self):
        return self.thought_category_text

class Thought(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    thought_text = models.TextField()
    thought_categories = models.ManyToManyField(ThoughtCategory)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        dt = self.create_date.strftime("%Y-%m-%d %H:%M")
        return f"{dt}: {self.thought_text[:100]}"