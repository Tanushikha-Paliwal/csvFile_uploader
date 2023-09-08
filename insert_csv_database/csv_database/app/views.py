from django.shortcuts import render
from . models import *
import io
import csv

# Create your views here.

def insert_data(request):
    if request.method == "POST":
        csv_file = request.FILES['csv_file']
        decode_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decode_file)
        next(io_string)
        for row in csv.reader(io_string , delimiter=','):
            date = row[0]
            open_price = float(row[1])
            high_price = float(row[2])
            low_price = float(row[3])
            close_price = float(row[4])
            adj_close_price = float(row[5])
            volume = int(row[6])
            Stock.objects.create(date = date , open = open_price , high = high_price , low = low_price , close = close_price ,
                                 adj_close = adj_close_price , volume = volume)
        return render(request , "success.html")
    return render(request , "insert.html")
    
def show_data(request):
    data = Stock.objects.all()
    return render(request , "table.html" , {"data":data})
    
