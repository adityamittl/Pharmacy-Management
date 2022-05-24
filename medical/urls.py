from django.contrib import admin
from django.urls import path,include
from inventory.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', updateInventory),
    path('billing', billing),
    path('getComposition', getComposition),
    path('findAlternative', findAlternative),
    path('findMedicine', findMedicine),
    path("api/medicine/<str:name>", getprice),
    path("api/bill",generateBill),
    path('bill/<str:name>', fetchBill),
    path("analyse",analysis),
    path('inventory',StockItems),
    path("checkQuantity",checkQuantity),
    path("setup",setup),
    path('',include("authentication.urls")),
    path('oldstock',oldInventory),
    path('backup',backupdb),
    path('findMedicineByComposition',findMedicineByComposition)
]
