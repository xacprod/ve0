#To allow URL references to be resolved 
#using Django's STATIC_URL and MEDIA_URL settings, 
#xhtml2pdf allows users to specify a link_callback paramter 
#to point to a function that converts relative URLs to absolute system paths.

import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

# Convert HTML URIs to absolute system paths 
# so xhtml2pdf can access those resources
def link_callback(uri, rel):
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

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                    'media URI must start with %s or %s' % \
                    (sUrl, mUrl))
    return path

def generate_pdf(request, type):
    # Prepare context
    data = {}
    data['today'] = datetime.date.today()
    data['farmer'] = 'Old MacDonald'
    data['animals'] = [('Cow', 'Moo'), ('Goat', 'Baa'), ('Pig', 'Oink')]

    # Render html content through html template with context
    template = get_template('lyrics/oldmacdonald.html')
    html  = template.render(Context(data))

    # Write PDF to file
    file = open(os.join(settings.MEDIA_ROOT, 'test.pdf'), "w+b")
    pisaStatus = pisa.CreatePDF(html, dest=file,
            link_callback = link_callback)

    # Return PDF document through a Django HTTP response
    file.seek(0)
    pdf = file.read()
    file.close()            # Don't forget to close the file handle
    return HttpResponse(pdf, mimetype='application/pdf')