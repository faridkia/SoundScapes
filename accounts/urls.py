from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm, CustomSetPasswordForm

app_name = 'accounts'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('password-reset/', auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm,success_url='done'), name='password-reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('password-reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(form_class=CustomSetPasswordForm,success_url='/accounts/password-reset/complete'), name='password-reset-confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password-reset-complete')
]