from django.urls import path,include
from users.views import user_details,login_form,register,index, user_delete,activate,featured_projects,user_edit,user_donations
urlpatterns = [
    path('register/', register, name="user.register"),
    path('edit/<int:id>', user_edit, name="user.edit"),
    path('', index, name="index"),
    path('login/', login_form, name="user.login"),
    path('details/<int:id>',user_details , name="user.details"),
    path('delete/<int:id>',user_delete , name="user.delete"),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('featured/', featured_projects , name="featured"),
    # path('add_to_featured/<int:id>',add_to_featured , name="add_to_featured"),
    path('donations/<int:id>', user_donations , name="user.donations"),

]