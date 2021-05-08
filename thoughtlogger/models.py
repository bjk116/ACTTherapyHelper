from django.db import models

# DAYS_OF_WEEK = (
#     (0, 'Monday'),
#     (1, 'Tuesday'),
#     (2, 'Wednesday'),
#     (3, 'Thursday'),
#     (4, 'Friday'),
#     (5, 'Saturday'),
#     (6, 'Sunday'),
# )

# class Days(models.Model):
#     day = models.CharField(max_length=8, choices=DAYS_OF_WEEK)

# DAY_OF_THE_WEEK = {
#     0 : ('Monday'),
#     1 : ('Tuesday'),
#     2 : ('Wednesday'),
#     3 : ('Thursday'),
#     4 : ('Friday'),
#     5 : ('Saturday'), 
#     6 : ('Sunday'),
# }

# class DayOfTheWeekField(models.CharField):
#     def __init__(self, *args, **kwargs):
#         kwargs['choices']=tuple(sorted(DAY_OF_THE_WEEK.items()))
#         kwargs['max_length']=1 
#         super(DayOfTheWeekField,self).__init__(*args, **kwargs)

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
        thought = f"{self.thought_text[:100]}..."
        # TODO: figure out way to display first couple of thought categories selected
        return f"{dt}: {thought}"

class Errands(models.Model):
    errand_text = models.CharField(max_length=200)
    description = models.TextField(null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    due_date = models.DateTimeField()
    # next_attempt_date will be used for notification/alarms
    # and what will be reset if the user doesn't do it
    next_attempt_date = models.DateTimeField(null=True)
    complete_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.errand_text

class Value(models.Model):
    value_text = models.CharField(max_length=200)

# milestones in values that you've reached
# kind of like proof that 
class Milestone(models.Model):
    # so we can say hey you have munachieved milestones in this model
    value = models.ForeignKey(Value, on_delete=models.PROTECT)
    milestone_text = models.CharField(max_length=300)
    complete_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.value.value_text}: {slef.milestone_text}"

class Routines(models.Model):
    routine_text = models.CharField(max_length=200)
    description = models.TextField()
#    days = models.ManyToManyField(DayOfTheWeekField)
    milestone = models.ForeignKey(Milestone, null=True, on_delete=models.PROTECT)

class SelectedValue(models.Model):
    value = models.ForeignKey(Value, on_delete=models.PROTECT)
    importance = models.TextField()
    routines = models.ForeignKey(Routines, on_delete=models.PROTECT)
