from django.db import models

class Content(models.Model):
    title = models.TextField()
    email = models.EmailField()
    phone = models.TextField(blank = True)
    category = models.IntegerField(default = 0)
    location = models.TextField(blank = True)
    content = models.TextField(null = True, blank = True)

    # def baby_boomer_status(self):
    #     "Returns the person's baby-boomer status."
    #     import datetime
    #     if self.birth_date < datetime.date(1945, 8, 1):
    #         return "Pre-boomer"
    #     elif self.birth_date < datetime.date(1965, 1, 1):
    #         return "Baby boomer"
    #     else:
    #         return "Post-boomer"

    # @property
    def __str__(self):
        return self.title