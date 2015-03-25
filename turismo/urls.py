from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from plataforma import views
# from landing_page import views

urlpatterns = patterns('',
    # Examples:   //
    # url(r'^$', 'views.index'),
    # url(r'^$', landing_page.views.VistaUsuario.as_view()),
    url(r'^roles/(?P<pk>[0-9]+)/$', views.RolDetail.as_view()),  
    url(r'^roles/', views.RolListCreate.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view()),  
    url(r'^usuarios/', views.UsuarioListCreate.as_view()),
    
   # url(r'^detalles/(?P<pk>[0-9]+)/$', 'views.VistaUsuario.as_view()'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^', include('landing_page.urls')),
    # url(r'^admin/', include(admin.site.urls)),
  #  url(r'^$', views.usuario_list),
  
   
)
urlpatterns = format_suffix_patterns(urlpatterns)