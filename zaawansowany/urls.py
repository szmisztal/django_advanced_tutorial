from django.contrib import admin
from django.urls import path, include
from library.views import home, send_email, new_form
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home),
    path('email', send_email),
    path('password_reset', PasswordResetView.as_view()),
    path('password_reset_done', PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name = 'password_reset_confirm'),
    path('password_reset_complete', PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    path('new_form', new_form, name = 'new_form')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
