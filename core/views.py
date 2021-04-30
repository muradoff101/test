from django.db.models import Sum, Max, Count
from core.models import Deals
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import generics
from core.models import *
from core.serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import csv
from deals.settings import BASE_DIR
# Create your views here.


class MainPageView(ListView):
    template_name = "index.html"
    model = Deals

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


class UploadCSVFilesView(generics.CreateAPIView):
    # serializer_class = CSVFileSerializer
    # parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        files_serializer = CSVFileSerializer(data=request.data)
        if files_serializer.is_valid():
            files_serializer.save()

            with open(str(BASE_DIR) + files_serializer.data['csv_file'], 'r',  encoding='utf_8') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if i == 0:
                        pass
                    else:
                        Deals.objects.create(
                            customer=row[0],
                            item=row[1],
                            total=row[2],
                            quantity=row[3],
                            date=row[4]
                        )

            return Response('ok', status=status.HTTP_201_CREATED)
        return Response(files_serializer.errors, status=status.HTTP_424_FAILED_DEPENDENCY)


class CustomersView(generics.ListAPIView):
    serializer_class = CustomersSerializer
    # queryset = Deals.objects.all().annotate(dcount=Sum('total')).order_by(
    #     "-total").distinct()[:5]

    # queryset = Deals.objects.all().values(
    #     "customer", "total", "item").distinct('customer').annotate(total_p=Sum("total")).order_by("-total")[:5]

    queryset = Deals.objects.values(
        'customer', 'item', 'total'
    ).annotate(
        total_sales=Sum('total')
    ).order_by('-total')[:5]
