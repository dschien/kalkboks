import json

from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render_to_response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from kalkboks import math


def home(request):
    return render_to_response('index.html')


@api_view(['POST'])
@permission_classes((AllowAny,))
def cagr(request):
    """
    calculate growth rate
    """
    # This view expects an access_token GET parameter
    try:
        i_0 = float(request.DATA['base'])
        rate = float(request.DATA['rate'])
        years = int(request.DATA['years'])
    except ValueError:
        return HttpResponse(json.dumps({"result": "Input should be numbers"}),
                            content_type="application/json",
                            status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse(json.dumps({"result": math.cagr(i_0, rate, years)}),
                        content_type="application/json",
                        status=status.HTTP_200_OK)
