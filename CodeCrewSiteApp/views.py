from django.shortcuts import render
from .forms import ContactForm, ContactingForm


# Create your views here.
# all pages render their respective page

def index(request):
    return render(request, 'CodeCrewSiteApp/index.html')


def AboutUs(request):
    return render(request, 'CodeCrewSiteApp/AboutUs.html', )


def Gallery(request):
    return render(request, 'CodeCrewSiteApp/Gallery.html', )


def Resources(request):
    return render(request, 'CodeCrewSiteApp/Resources.html', )

# sends the form for contacting, for some reason name isn't popping up
def ContactUs(request):
    form = ContactingForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request, 'CodeCrewSiteApp/ContactUs.html', {'form': ContactingForm()})
    return render(request, 'CodeCrewSiteApp/ContactUs.html', {'form': ContactingForm()})

# there is nothing else to look at



































def SecretPage(request):
    contactList = ContactForm.objects.all()
    print(contactList)
    return render(request,'CodeCrewSiteApp/SecretPage.html',{'contactList':contactList})