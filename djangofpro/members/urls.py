from django.urls import path
from . views import UserEditView
from django.contrib.auth import views as auth_views
from .import views
from .views import UsDelete,UsUpdate,UsView,PasswordsChangeView



urlpatterns=[
	#path('register/',userregister.as_view(),name='register'),
	path('',views.registerform,name='register'),
	path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
	path('login/',views.loginpage,name='login'),
	path('logout/',views.logoutpage,name='logout'),
	path('uslis/',UsView.as_view(),name='uslis'),
	path('usdp/<int:id>',views.userpg,name='userpag'),
	path('usdetail/<int:id>',views.Usdetails_page,name='usdetail'),
	path('usupd/<int:pk>',UsUpdate.as_view(),name='userupd'),
	path('usdel/<int:pk>',UsDelete.as_view(),name='userdel'),
	path('userbase',views.ubase,name='userbase'),

	path('reset_password/',auth_views.PasswordResetView.as_view(template_name="Passwordreset/password_reset.html"),name="reset_password"),
	path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="Passwordreset/password_reset_sent.html"),name="password_reset_done"),
	path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="Passwordreset/password_reset_form.html"),name="password_reset_confirm"),
	path('reset_password-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="Passwordreset/password_reset_done.html"),name="password_reset_complete"),
	#path('password/',auth_views.PasswordChangeView.as_view(template_name="Passwordreset/password_change.html")),
	path('password/',PasswordsChangeView.as_view(template_name="Passwordreset/password_change.html")),
	path('password_success',views.password_success,name='password_success'),
]