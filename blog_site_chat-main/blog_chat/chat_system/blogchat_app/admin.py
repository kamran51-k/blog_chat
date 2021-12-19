from django.contrib import admin

from blogchat_app.models import AboutModel, Comment, ContactModel, LogoModel, NavbarModel, PostModel, ContactModel2

# Register your models here.
admin.site.register(NavbarModel)
admin.site.register(PostModel)
admin.site.register(LogoModel)
admin.site.register(AboutModel)
admin.site.register(ContactModel2)
admin.site.register(ContactModel)
admin.site.register(Comment)
