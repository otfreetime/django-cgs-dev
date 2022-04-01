
from ast import arg
from unicodedata import category
from urllib.request import Request
from xml.parsers.expat import model
from dal import autocomplete
from django.shortcuts import render
from django.utils.html import format_html
from django.views.generic import CreateView, TemplateView, ListView

from apps.devapp.serializers import CodesSerializer
from .forms import  PersonForm, createForm , generateForm
from .models import  CodesModel , GenerateModel, CategoriesModel
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse

from .serializers import CodesSerializer
from rest_framework import viewsets

#*******************************************************************************
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import CodesModel
from .serializers import CodesSerializer

#*************************************************************************************

class CodesViewSet(viewsets.ModelViewSet):
    queryset = CodesModel.objects.all().order_by('code')
    serializer_class = CodesSerializer

class CodesListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]
    #  def get_object(self, todo_id, user_id):
    # Codes.objects.filter(category__categoryname="Entity") 
    def get_serializer_context(self):
        return {'request': self.request}

    def get(self, request, *args, **kwargs):
    
        try:
            query =self.kwargs['cat']
        except:
           # codes = CodesModel.objects.all()
            return None
        else:
            codes = CodesModel.objects.filter(category__categoryname=query)
            serializer = CodesSerializer(codes,many=True,context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
       
       

#***************************************************
from django.http import HttpResponse
from django.views import View

from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView

class CategoryCounterRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'article-detail'
    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(CategoriesModel, pk=kwargs['pk'])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)

class MyView(ListView):
    def get(self, request, *args, **kwargs):
        methods = kwargs.get('cat_q') #View.http_method_names
        return HttpResponse(methods)

class CategoriesCountView(ListView):
    model = CategoriesModel
    template_name = "devapp/category.html"
    context_object_name = 'Categories'
    def head(self, *args, **kwargs):
        #last_book = self.get_queryset().latest('publication_date')
        CategoriesCount = 55 #self.get_queryset().all().count
        response = HttpResponse(headers={'Categories-Count': CategoriesCount},)
        return response

class HomePageView(TemplateView):
    template_name = "devapp/category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_context'] = CategoriesModel.objects.all()[:2]
        return context
#***************************************************

class AboutView(TemplateView):
    template_name = "devapp/about.html"


#@login_required(login_url="/login/")
class createView(CreateView):
    model=CodesModel
    form_class=createForm
    template_name = 'devapp/createPage.html'

   
class PersonView(CreateView):
    model=CodesModel
    form_class=PersonForm
    template_name = 'devapp/PersonPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['js_script'] = """
                                $('#id_mytest').on('change', function () {
                                    var selected = $('#id_mytest').val();
                                    var cSelect = document.getElementById("mySelect2");
                                    cSelect.innerHTML = $('#id_mytest  option:selected').text()
                                });
                                """
        return context

class generateView(CreateView):
    model=GenerateModel
    form_class=generateForm
    template_name = 'devapp/generatePage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['js_script'] = """
                                $('#id_thetype').on('change', function () {
                                    var selected = $('#id_thetype').val();
                                    var cSelect = document.getElementById("mySelect2");
                                    cSelect.innerHTML = $('#id_thetype  option:selected').text()
                                });
                                """
        return context
    # 2. Create
    # def post(self, request, *args, **kwargs):
    #     '''
    #     Create the Todo with given todo data
    #     '''
    #     data = {
    #         'task': request.data.get('task'), 
    #         'completed': request.data.get('completed'), 
    #         'user': request.user.id
    #     }
    #     serializer = CodesSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#*******************************************************************************
class CodesAutocomplete(autocomplete.Select2QuerySetView):
    # def get_result_label(self, result):
    #     return format_html('{}', result.code)
    
    def get_queryset(self, *args, **kwargs):
        # query =self.kwargs['cat']
        try:
            query =self.kwargs['cat']
        except:
            qs = CodesModel.objects.all()
        else:
            qs = CodesModel.objects.filter(category__categoryname=query)
        
        if self.q:
            qs = qs.filter(Q(code__icontains=self.q) | Q(endesc__icontains=self.q)  | Q(ardesc__icontains=self.q))

        return qs





#*******************************************************************************
class CodesAutocompleteApi(autocomplete.Select2QuerySetView):
    # def get_result_label(self, result):
    #     return format_html('{}', result.code)

    def get_queryset(self, *args, **kwargs):
        qs = CodesModel.objects.filter(category__categoryname='Entity') 
        if self.q:
            qs = qs.filter(Q(code__icontains=self.q) | Q(endesc__icontains=self.q)  | Q(ardesc__icontains=self.q))
        return qs 


# #*******************************************************************************
# class CodesAutocompleteEntity(autocomplete.Select2QuerySetView):
#     # def get_result_label(self, result):
#     #     return format_html('{}', result.code)

#     def get_queryset(self, *args, **kwargs):
#         qs = CodesModel.objects.filter(category__categoryname='Entity') 
#         if self.q:
#             qs = qs.filter(Q(code__icontains=self.q) | Q(endesc__icontains=self.q)  | Q(ardesc__icontains=self.q))
#         return qs 


# class CodesAutocompleteEntity(autocomplete.Select2QuerySetView):
#     # def get_result_label(self, result):
#     #     return format_html('{}', result.code)

#     def get_queryset(self, *args, **kwargs):
#         qs = CodesModel.objects.filter(category__categoryname='Entity') 
#         if self.q:
#             qs = qs.filter(Q(code__icontains=self.q) | Q(endesc__icontains=self.q)  | Q(ardesc__icontains=self.q))
#         return qs 



# class CodesAutocompletePerson(autocomplete.Select2QuerySetView):
#     # def get_result_label(self, result):
#     #     return format_html('{}', result.code)

#     def get_queryset(self, *args, **kwargs):
#         qs = CodesModel.objects.filter(category__categoryname='Person') 
#         if self.q:
#             qs = qs.filter(Q(code__icontains=self.q) | Q(endesc__icontains=self.q)  | Q(ardesc__icontains=self.q))
#         return qs 

# #**********************************************************************************************************************************
# class CodesAutocompleteCorporate(autocomplete.Select2QuerySetView):
#     # def get_result_label(self, result):
#     #     return format_html('{}', result.code)

#     def get_queryset(self, *args, **kwargs):
#         qs = CodesModel.objects.filter(category__categoryname='Corporate') 
#         if self.q:
#             qs = qs.filter(Q(code__icontains=self.q) | Q(endesc__icontains=self.q)  | Q(ardesc__icontains=self.q))
#         return qs 


# #**********************************************************************************************************************************
# class CodesAutocompleteProject(autocomplete.Select2QuerySetView):
#     # def get_result_label(self, result):
#     #     return format_html('{}', result.code)

#     def get_queryset(self, *args, **kwargs):
#         qs = CodesModel.objects.filter(category__categoryname='Project') 
#         if self.q:
#             qs = qs.filter(Q(code__icontains=self.q) | Q(endesc__icontains=self.q)  | Q(ardesc__icontains=self.q))
#         return qs 


# #**********************************************************************************************************************************
# class CodesAutocompleteGovernment(autocomplete.Select2QuerySetView):
#     # def get_result_label(self, result):
#     #     return format_html('{}', result.code)

#     def get_queryset(self, *args, **kwargs):
#         qs = CodesModel.objects.filter(category__categoryname='Government') 
#         if self.q:
#             qs = qs.filter(Q(code__icontains=self.q) | Q(endesc__icontains=self.q)  | Q(ardesc__icontains=self.q))
#         return qs 


# #**********************************************************************************************************************************
# class CodesAutocompleteDoctype(autocomplete.Select2QuerySetView):
#     # def get_result_label(self, result):
#     #     return format_html('{}', result.code)

#     def get_queryset(self, *args, **kwargs):
#         qs = CodesModel.objects.filter(category__categoryname='Doctype') 
#         if self.q:
#             qs = qs.filter(Q(code__icontains=self.q) | Q(endesc__icontains=self.q)  | Q(ardesc__icontains=self.q))
#         return qs 

# #**********************************************************************************************************************************
# class CodesAutocompleteStatus(autocomplete.Select2QuerySetView):
#     # def get_result_label(self, result):
#     #     return format_html('{}', result.code)

#     def get_queryset(self, *args, **kwargs):
#         qs = CodesModel.objects.filter(category__categoryname='Status') 
#         if self.q:
#             qs = qs.filter(Q(code__icontains=self.q) | Q(endesc__icontains=self.q)  | Q(ardesc__icontains=self.q))
#         return qs 



    