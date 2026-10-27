from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse


def get_cars(request):
    car_models = [
        {"CarModel": "Pathfinder", "CarMake": "NISSAN"},
        {"CarModel": "Qashqai", "CarMake": "NISSAN"},
        {"CarModel": "XTRAIL", "CarMake": "NISSAN"},
        {"CarModel": "A-Class", "CarMake": "Mercedes"},
        {"CarModel": "C-Class", "CarMake": "Mercedes"},
        {"CarModel": "E-Class", "CarMake": "Mercedes"},
        {"CarModel": "A4", "CarMake": "Audi"},
        {"CarModel": "A5", "CarMake": "Audi"},
        {"CarModel": "A6", "CarMake": "Audi"},
        {"CarModel": "Sorrento", "CarMake": "Kia"},
        {"CarModel": "Carnival", "CarMake": "Kia"},
        {"CarModel": "Cerato", "CarMake": "Kia"},
        {"CarModel": "Corolla", "CarMake": "Toyota"},
        {"CarModel": "Camry", "CarMake": "Toyota"},
        {"CarModel": "Kluger", "CarMake": "Toyota"},
    ]

    return JsonResponse({"CarModels": car_models})
