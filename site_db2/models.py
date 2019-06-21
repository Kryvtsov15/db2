from django.db import models


class Message(models.Model):
    email = models.EmailField(max_length=254, verbose_name= "Email")
    text_message = models.CharField(max_length= 100, verbose_name= "Message")
    create_date = models.DateField(auto_now_add=True, verbose_name= "Create date")
    update_date = models.DateField(auto_now=True, verbose_name= "Update_date")