from registration.signals import user_activated
from django.contrib.auth.models import Group
from django.core.mail import mail_admins

def create(sender, user, request, **kwarg):
    g = Group.objects.get(name="Editor") 
    g.user_set.add(user)
    user.is_staff = True
    user.save()

    msg = "%s %s" % (user.username, user.email) 
    mail_admins(subject="Helphelp2: new registration", message=msg)

user_activated.connect(create)
