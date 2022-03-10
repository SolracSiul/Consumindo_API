from django.http import Http404, HttpRequest
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.http import JsonResponse
from django.conf import settings 
import requests
from ConsultaAPI.models import IpsPublicados

@api_view(['GET'])
def getLocationByIP(request,ip):
    url = 'http://ip-api.com/json/'
    print(ip)
    try:
        response = requests.get(url + ip).json()

        ipPlubicado = IpsPublicados(ip_query = response['query'],
            ip_status = response['status'],
            ip_country = response['country'],
            ip_countryCode = response['countryCode'],
            ip_region = response['region'],
            ip_regionName= response['regionName'],
            ip_city=response['city'],
            ip_zip= response['zip'],
            ip_lat=response['lat'],
            ip_lon=response['lon'],
            ip_timezone=response['timezone'],
            ip_isp=response['isp'],
            ip_org=response['org'],
            ip_as=response['as'])
        ipPlubicado.save()
        ## salvar response no BD
        return JsonResponse(response, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getHistorico(request):
    try:
        ipspublicados = IpsPublicados.objects.all().values()
        return JsonResponse(list(ipspublicados), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

