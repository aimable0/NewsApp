from django.shortcuts import render
from .models import AirtimePayments


# Create your views here.
def index(request):
    return render(request, "momo/index.html")


def airtime(request):
    return render(
        request, "momo/airtime.html", {"airtime": AirtimePayments.objects.all()}
    )
