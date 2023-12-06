from django.shortcuts import render,redirect
from .forms import CSVUploadForm
from .models import DynamicModel , DynamicData
from django.db import models
import csv
import io

def upload_csv(request):
    if request.method =='POST':
        form = CSVUploadForm(request.POST,request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']

            text_csv_file =io.TextIOWrapper(csv_file,encoding='utf8')
            reader = csv.DictReader(text_csv_file)
            
            dynamic_model_instance = DynamicModel()
            dynamic_model_instance.save()

            # dynamically create columns in the model from those method 
            for row in reader:
                
                for column_name ,value in row.items():
                    dynamic_data_instance= DynamicData(
                        dynamic_model = dynamic_model_instance,
                        column_name=column_name,
                        column_value=value
                    )
                    dynamic_data_instance.save()

            return redirect('upload_success')
    else:
        form = CSVUploadForm()
    return render(request,'upload_csv.html',{'form':form})


def upload_success(request):
    return render(request,'upload_success.html')

def show_csv(request):
    data = DynamicData.objects.filter(dynamic_model__isnull=False)

    data_dict = {}
    for item in data:
        model_id = item.dynamic_model.id
        column_name = item.column_name
        column_value = item.column_value

        if model_id not in data_dict:
            data_dict[model_id] = {'id': model_id, 'columns': {}}

        data_dict[model_id]['columns'][column_name] = column_value

    # Convert the dictionary to a list for easier iteration in the template
    data_list = list(data_dict.values())

    # get unique column name 
    unique_column = set()
    for item in data_list:
        unique_column.update(item['columns'].keys())


    return render(request, 'show_csv.html', {'data': data_list,'unique_columns':unique_column})