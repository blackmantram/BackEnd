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
    url(r'^usuariosredes/(?P<pk>[0-9]+)', views.UsuarioRedesDetail.as_view()),
    url(r'^usuariosredes', views.UsuarioRedesListCreate.as_view()),
        url(r'^usuarios/(?P<usuario>[0-9]+)/problemas_soluciones/(?P<pk>[0-9]+)', views.ProblemaSolucionDetail.as_view()),
    url(r'^usuarios/(?P<usuario>[0-9]+)/problemas_soluciones', views.ProblemaSolucionListCreate.as_view()), 
    url(r'^buscar/$', views.ProblemaSolucionListCreate.as_view()), 
    url(r'^usuarios/(?P<pk>[0-9]+)/redes', views.UsuarioRedesList.as_view()),  
    url(r'^usuarios/(?P<pk>[0-9]+)', views.UsuarioDetail.as_view()),
    url(r'^usuarios', views.UsuarioListCreate.as_view()), 
    url(r'^redes/(?P<pk>[0-9]+)', views.RedSocialDetail.as_view()),
    url(r'^redes', views.RedSocialListCreate.as_view()),
    url(r'^categorias/(?P<pk>[0-9]+)', views.CategoriaDetail.as_view()),
    url(r'^categorias', views.CategoriaListCreate.as_view()), 
    url(r'^problemas_soluciones/(?P<pk>[0-9]+)', views.ProblemaSolucionDetail.as_view()), 
  #  url(r'^usuarios/(?P<pk>[0-9]+)/$/redes/', views.UsuarioRedesDetail.as_view()),  
   # url(r'^detalles/(?P<pk>[0-9]+)/$', 'views.VistaUsuario.as_view()'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^', include('landing_page.urls')),
    # url(r'^admin/', include(admin.site.urls)),
  #  url(r'^$', views.usuario_list),
  
   
)
urlpatterns = format_suffix_patterns(urlpatterns)