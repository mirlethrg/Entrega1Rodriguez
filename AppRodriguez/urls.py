"""Entrega1Olivar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from AppRodriguez import views
from AppRodriguez.views import About , Contact , Pricing , Faq , PortFolioItem , formulario_proyecto , formulario_experiencia , formulario_cursos
urlpatterns = [
    path('', views.Inicio, name="AppInicio"),
    path('about', About, name="AppRodriguezAbout"),
    path('contact', Contact, name="AppRodriguezContact"),
    path('pricing', Pricing, name="AppRodriguezPricing"),
    path('faq', Faq, name="AppRodriguezFaq"),
    path('bloghome', formulario_proyecto, name="AppRodriguezBlogHome"),
    path('blogpost', formulario_experiencia, name="AppRodriguezBlogPost"),
    path('portfoliooverview', formulario_cursos, name="AppRodriguezPortFolioOverview"),
    path('portfolioitem', PortFolioItem, name="AppRodriguezPortFolioItem"),
]
