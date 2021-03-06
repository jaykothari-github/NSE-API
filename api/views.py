from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date
from nsepy import get_history
from .serializers import *
from .models import *


# Create your views here.

@api_view(['GET'])
def overview(request):
    api_urls = {
        '/' : 'Api Overviews',
        '/get-data/' : 'Get Data'

    }
    return Response(api_urls)

@api_view(['GET','POST'])
def get_data(request):
    if request.method == 'POST':
        print(request.data,'------------------------------------------')
        symbol = request.data['symbol']
        # start = request.data['start'].split('-')
        # end = request.data['end'].split('-')
        # sbin = get_history(symbol=symbol,
        #             start=date(int(start[0]),int(start[1]),int(start[2])),
        #             end=date(int(end[0]),int(end[1]),int(end[2])))

        sbin = get_history(symbol=symbol,
                    start=date(2022,3,1),
                    end=date.today())[::-1]
        d = dict(sbin)
        data = {'Info': {'Symbol' : symbol}, 'Time' : {}}
        for i in range(7):
            try:
                data['Info']['Series'] = d['Series'][date(2022,3,i)]
            except:pass
        l = ['Open','High','Low','Close']
        for k,v in d['Symbol'].items():
            data['Time'].update({str(k):{}})
        for i in l:
            for k,v in d[i].items():
                data['Time'][str(k)].update({i.lower():v})
        return Response(data)
    return Response('GET Method')