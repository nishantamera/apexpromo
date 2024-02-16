from datetime import datetime
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.http.response import JsonResponse

from django.contrib.auth.models import User
from dbconnect import get_db_handle, get_collection_handle

dbName = get_db_handle("apex-azure-promo")
promoCollection = get_collection_handle(dbName, "promotions")


@api_view(['GET'])
@permission_classes([AllowAny])
def get_credit_card_promo(request):
    details = get_promo("Credit-Card")
    return JsonResponse({"success": "Successfully retrieved credit card promo.", "details": details}, status=200, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_home_loan_promo(request):
    details = get_promo("Home-Loan")
    return JsonResponse({"success": "Successfully retrieved home loan promo.", "details": details}, status=200, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_insurance_promo(request):
    details = get_promo("Insurance")
    return JsonResponse({"success": "Successfully retrieved insurance promo.", "details": details}, status=200, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_car_loan_promo(request):
    details = get_promo("Car-Loan")
    return JsonResponse({"success": "Successfully retrieved car loan promo.", "details": details}, status=200, safe=False)

def get_promo(type):
    item = promoCollection.find_one({"type": type}, {"_id": 0, "type": 0})
    details = {
        "promo": item["url"]
    }
    return(details)
