# forms.py
from django import forms
from .models import CodesModel , GenerateModel
from dal import autocomplete
from django.utils.html import format_html
from django.shortcuts import resolve_url, reverse
from django.urls import reverse_lazy

# class CodesAutocomplete(autocomplete.Select2QuerySetView):
#     def get_result_label(self, result):
#         return format_html('<img src="flags/{}.png"> {}', result.name, result.name)


class PersonForm(forms.ModelForm):
    class Meta:
        model = CodesModel
        fields = ('__all__')
        widgets = {
            'mytest': autocomplete.ModelSelect2(
                url='code-json-url-autocomplete',
                attrs={'data-html': True}
            )
        }

class createForm(forms.ModelForm):
    code = forms.CharField(label='Code',widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Code ','for':'id_code'}))
    class Meta:
        model = CodesModel
        fields =  "__all__"
        widgets = {
            'endesc': forms.TextInput(attrs={'class': 'form-control','placeholder': 'English Desc.'}),
            'remarks': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Remarks ',}),
            'ardesc': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Arabic Desc.'}),
            'category': forms.Select(attrs={'class': 'form-control','placeholder': 'Select Category'}),
         }
        labels = {
            "endesc": "",
            'remarks': '',
            'ardesc': '',
            'category': '',
        }
        requireds ={ "remarks":False}

class generateForm(forms.ModelForm):

    class Meta:
        model = GenerateModel
        fields = "__all__"
        widgets = {
            'datepart':  forms.TextInput(attrs={'class': 'form-control','placeholder': 'Select the Date.','data-datepicker':'', 'autocomplete':"off"}),
            'thetype': autocomplete.ModelSelect2(url='code-json-url-autocomplete-Entity', attrs={'data-html': True,'class': 'form-control','placeholder': 'Select the Type'}),
            'relatedIssues1': autocomplete.ModelSelect2(url='code-json-url-autocomplete-Doctype', attrs={'data-html': True}),
            'relatedIssues2': autocomplete.ModelSelect2(url='code-json-url-autocomplete-Government', attrs={'data-html': True}),
            'relatedIssues3': autocomplete.ModelSelect2(url='code-json-url-autocomplete-Corporate', attrs={'data-html': True}),
            'project': autocomplete.ModelSelect2(url='code-json-url-autocomplete-Project', attrs={'data-html': True}),
            'status': autocomplete.ModelSelect2(url='code-json-url-autocomplete-Status', attrs={'data-html': True}),
        }
    
 
# Date
# Type
# RelatedIssues1
# RelatedIssues2
# RelatedIssues3
# Project
# Remarks
# Status
