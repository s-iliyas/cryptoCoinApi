import requests
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class HomeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        currency = request.GET.get("currency")
        response = requests.get(
            f'https://api.coingecko.com/api/v3/coins/markets?vs_currency={currency}')
        coinData = response.json()
        request_data = list(map(lambda x: mapFunction(x), coinData))
        serializer = self.serializer_class(data=request_data, many=True)
        # serialized data validation
        if serializer.is_valid():
            # saving validated serialized data in db using save method
            serializer.save()
            # send 200 ok when success as response
            return Response({"coinData": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
