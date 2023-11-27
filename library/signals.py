from django.db.models.signals import post_save, pre_save
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from .models import Author
import logging

author_log = logging.getLogger("author_log")
author_log.setLevel(logging.DEBUG)
log_handler = logging.FileHandler('logs/author.log')
log_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)
author_log.addHandler(log_handler)

# our_signal = Signal()

@receiver([post_save], sender = Author)
def author_after_save(sender, instance, **kwargs):
    print("Author saved !")
    print(instance.name, instance.surname)
    author_log.info("some1 created author: " + instance.name + " " + instance.surname )
#
# @receiver([pre_save], sender = Author)
# def author_before_save(sender, instance, **kwargs):
#     print("Author will be saved !")
#     our_author = Author.objects.get(id = instance.id)
#     print(our_author.name, our_author.surname)
#
# @receiver(request_finished)
# def home_load(sender, **kwargs):
#     print("Homepage loaded !")
#
# @receiver(our_signal)
# def given_name(sender, **kwargs):
#     print("Given name", kwargs.get('name'))
