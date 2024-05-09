from rest_framework import serializers
from home.models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendor_name']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    team = PurchaseOrder()
    team_info = serializers.SerializerMethodField()

    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        depth = 1

class HistoricalperformanceSerializer(serializers.ModelSerializer):
    team = HistoricalPerformance()
    team_info = serializers.SerializerMethodField()

    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
        depth = 1