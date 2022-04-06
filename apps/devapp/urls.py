
from django.urls import  include, path, re_path as url
from django.views.generic.base import View
from django.views.generic import TemplateView
from rest_framework import routers
from .forms import PersonForm
from .views import AboutView, CategoriesCountView, CategoryCounterRedirectView, CodesAutocomplete, CodesAutocompleteApi,  CodesListApiView, HomePageView, MyView, PersonView, createView , generateView
from dal import autocomplete
from .models import CodesModel
from django.views.generic.base import RedirectView
from . import views
router = routers.DefaultRouter()
router.register(r'codes', views.CodesViewSet)


#app_name = 'devapp'
urlpatterns = [
       path('create', views.CreateView.as_view(), name='create'),
       path('', include(router.urls)),
       path('api/', CodesListApiView.as_view()),
       path('api/<cat>/', CodesListApiView.as_view()),
       path('create-codes/', createView.as_view(), name="create-codes"),
       path('generate/', generateView.as_view(), name="generate-codes"),

       # path('get_all_codes/api/Entity', CodesAutocomplete.as_view(), name='code-json-url-autocomplete-Entity',kwargs={'cat':'Entity'}),
       # #path('get_all_codes/', CodesAutocompleteEntity.as_view(), name='code-json-url-autocomplete-Person',kwargs={'cat':'Person'}),
       # path('api/Doctype', CodesAutocomplete.as_view(), name='code-json-url-autocomplete-Doctype',kwargs={'cat':'Doctype'}),
       # path('get_all_codes/Government', CodesAutocomplete.as_view(), name='code-json-url-autocomplete-Government',kwargs={'cat':'Government'}),
       # path('get_all_codes/Corporate', CodesAutocomplete.as_view(), name='code-json-url-autocomplete-Corporate',kwargs={'cat':'Corporate'}),
       # path('get_all_codes/project', CodesAutocomplete.as_view(), name='code-json-url-autocomplete-Project',kwargs={'cat':'Project'}),
       # path('get_all_codes/status', CodesAutocomplete.as_view(), name='code-json-url-autocomplete-Status',kwargs={'cat':'Status'}),

       path('get_all_codes/Entity', CodesAutocomplete.as_view(), name='code-json-url-autocomplete-Entity',kwargs={'cat':'Entity'}),
       #path('get_all_codes/', CodesAutocompleteEntity.as_view(), name='code-json-url-autocomplete-Person',kwargs={'cat':'Person'}),
       path('get_all_codes/Doctype', CodesAutocomplete.as_view(), name='code-json-url-autocomplete-Doctype',kwargs={'cat':'Doctype'}),
       path('get_all_codes/Government', CodesAutocomplete.as_view(), name='code-json-url-autocomplete-Government',kwargs={'cat':'Government'}),
       path('get_all_codes/Corporate', CodesAutocomplete.as_view(), name='code-json-url-autocomplete-Corporate',kwargs={'cat':'Corporate'}),
       path('get_all_codes/project', CodesAutocomplete.as_view(), name='code-json-url-autocomplete-Project',kwargs={'cat':'Project'}),
       path('get_all_codes/status', CodesAutocomplete.as_view(), name='code-json-url-autocomplete-Status',kwargs={'cat':'Status'}),



       #path('get_all_codes/<cat>', CodesAutocomplete.as_view(), name='code-json-url-autocomplete',),
       #url (r'^get_all_codes/(?P<cat_q>)$', CodesAutocomplete.as_view(), name='code-json-url-autocomplete',kwargs={'devapp':'cat_q'}),
       #path('get_all_codes/<str:cat_q>', MyView.as_view(), name='code-omar-url-autocomplete',),
       url(r'^codes/$', PersonView.as_view(), name='code-autocomplete',),
       #path('about/', TemplateView.as_view(template_name="dev/Appabout.html")),
       path('about/', AboutView.as_view()),
       path('mine/', MyView.as_view(), name='my-view'),
       path('count/', CategoriesCountView.as_view(), name='Categories-Count-View'),
       path('new_context', HomePageView.as_view(), name='Home-Page-View'),

       # path('counter/<int:pk>/', CategoryCounterRedirectView.as_view(), name='article-counter'),
       #path('details/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
       # path('go-to-django/', RedirectView.as_view(url='https://www.djangoproject.com/'), name='go-to-django'),

]
