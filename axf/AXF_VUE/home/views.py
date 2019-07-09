from time import sleep

from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework_extensions.cache.decorators import cache_response

from home.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow
from home.serializers import MainWheelSerializer, MainNavSerializer, MainMustBuySerializer, MainShopSerializer, \
    MainShowSerializer


class HomeView(GenericAPIView):

    # @cache_response(timeout=300)
    def get(self, request, *args, **kwargs):

        result = cache.get("homeview1")

        if result:
            return Response(result)

        mainwheels = MainWheel.objects.all()

        main_wheels_serializer = MainWheelSerializer(mainwheels, many=True)

        mainnavs = MainNav.objects.all()

        main_navs_serializer = MainNavSerializer(mainnavs, many=True)

        mainmustbuys = MainMustBuy.objects.all()

        main_must_buys_serializer = MainMustBuySerializer(mainmustbuys, many=True)

        mainshops = MainShop.objects.all()

        main_shops_serializer = MainShopSerializer(mainshops, many=True)

        mainshows = MainShow.objects.all()

        main_shows_serializer = MainShowSerializer(mainshows, many=True)

        # sleep(5)

        data = {
            "status": HTTP_200_OK,
            "msg": "ok",
            "data": {
                "main_wheels": main_wheels_serializer.data,
                "main_navs": main_navs_serializer.data,
                "main_must_buys": main_must_buys_serializer.data,
                "main_shops": main_shops_serializer.data,
                "main_shows": main_shows_serializer.data
            }
        }

        cache.set("homeview1", data, timeout=300)

        return Response(data)
