from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class HomeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        currency = request.GET.get("currency")
        return Response({"coinData": currency}, status=status.HTTP_200_OK)
