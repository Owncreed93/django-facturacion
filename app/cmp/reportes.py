import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.utils import timezone
from xhtml2pdf import pisa

from .models import ComprasEnc, ComprasDet 

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path

def reporte_compras(request):
    template_path = 'cmp/compras_print_all.html'
    today = timezone.now()

    compras = ComprasEnc.objects.all()

    contexto = {
        'obj': compras,
        'today' : today,
        'request' : request
    }

    response = HttpResponse( content_type = 'application/pdf' )
    # * inline --> SETS THE PDF AS A HTML PAGE
    response['Content-Disposition'] = 'inline; filename="todas_compras.pdf"'
    template = get_template(template_path)
    html = template.render(contexto)

    # * CREATE A PDF
    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback
    )

    # * IF ERROR THEN SHOW SOME FUNY VIEW
    if pisaStatus.err:
        return HttpResponse(f'We had some errors <pre> {html} </pre>')
    
    return response

def imprimir_compra(request, compra_id):
    template_path = 'cmp/compras_print_one.html'
    today = timezone.now()

    enc = ComprasEnc.objects.filter(id=compra_id).first()

    if enc:
        detalle = ComprasDet.objects.filter(compra__id=compra_id)
    else:
        datalle = {}

    context = {
        'detalle': detalle,
        'encabezado': enc,
        'today': today,
        'request': request
    }

    response = HttpResponse( content_type = 'application/pdf' )
    # * attachment --> DOWNLOADS THE PDF
    response['Content-Disposition'] = 'attachment; filename="one_compras.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # * CREATE A PDF
    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback
    )

    # * IF ERROR THEN SHOW SOME FUNY VIEW
    if pisaStatus.err:
        return HttpResponse(f'We had some errors <pre> {html} </pre>')
    
    return response

