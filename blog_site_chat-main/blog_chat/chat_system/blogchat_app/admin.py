from django.contrib import admin

from blogchat_app.models import AboutModel, CategoryModel, Comment, ContactModel, LogoModel, NavbarModel, PostModel, ContactModel2, ProfileModel

# Register your models here.
admin.site.register(NavbarModel)
admin.site.register(PostModel)
admin.site.register(LogoModel)
admin.site.register(AboutModel)
admin.site.register(ContactModel2)
admin.site.register(ContactModel)
admin.site.register(Comment)
admin.site.register(CategoryModel)
admin.site.register(ProfileModel)
