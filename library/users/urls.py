from django.urls import path
from django.contrib.auth import views as auth_views
from .views import logout,register,profile,createsuperuser
from .forms import CreateSuperUserForm
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="users-login"),
    path('logout/', logout, name="users-logout"),
    path('register/', register, name="users-register"),
    path('profile/',profile, name='users-update'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name="users/password_reset.html"
         ),
         name='password-reset'),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(
             template_name="users/password_reset_done.html"
             ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="users/password_reset_confirm.html",
             ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
     auth_views.PasswordResetCompleteView.as_view(
         template_name="users/password_reset_complete.html"
     ),
     name='password_reset_complete'),
    path("create-librarian/", createsuperuser, name="create-librarian")
]