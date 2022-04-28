from msilib.schema import ListView
from django.shortcuts import render, get_list_or_404, get_object_or_404
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from .models import Customer

class CustomerListView(ListView):
    # models = Customer
    queryset = Customer.objects.all()
    template_name = 'customers/main.html'

def customer_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    customer = get_object_or_404(Customer, pk=pk)

    template_path = 'customers/pdf2.html' # the template we want to render <----
    context = {'customer': customer} # the context we want to pass to the template <----
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # For Download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # For Display only
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Create your views here.
def render_pdf_view(request):
    template_path = 'customers/pdf1.html' # the template we want to render <----
    context = {'myvar': 'this is your template context'} # the context we want to pass to the template <----
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # For Download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # For Display only
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response