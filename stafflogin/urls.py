from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from stafflogin import views as s
urlpatterns = [
    path("", s.index, name="index"),
    path("login", s.loginUser, name="loginUser"),
    path("logout", s.logout_request, name="logout_request"),
    path("staff/user", s.user, name="user"),
    path("staff/listing", s.listing, name="listing"),
    path("staff/owner", s.owner, name="owner"),
    path("staff/adduser", s.adduser, name="adduser"),
    path("staff/addproperty", s.addproperty, name="addproperty"),
    path("staff/addpropertyowner", s.addpropertyowner, name="addpropertyowner"),
    path("staff/<id>/edituser/", s.edituser, name="edituser"),
    path("staff/editproperty", s.editproperty, name="editproperty"),
    path("staff/<id>/editowner",s.editpropertyowner, name="addpropertyowner"),
    path("staff/<id>/deleteuser", s.deleteuser, name="deleteuser")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
