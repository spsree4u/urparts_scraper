from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from scraper.models import PartsDetails
from scraper.serializers import PartsDetailsSerializer

# Create your views here.


@api_view(['GET'])
def company_parts(request, format=None):
    try:
        filter_params = {}

        company_name = request.query_params.get('manufacturer')
        if company_name:
            filter_params['company_name'] = company_name
        category_name = request.query_params.get('category')
        if category_name:
            filter_params['category_name'] = category_name
        model_name = request.query_params.get('model')
        if model_name:
            filter_params['model_name'] = model_name

        print(filter_params)
        parts_details = PartsDetails.objects.filter(**filter_params).values(
            'company_name', 'category_name', 'model_name', 'part_name')

        print(parts_details)
        if not parts_details:
            return Response(
                "No resource found, please check the query parameters "
                "and values in URL!", status=HTTP_404_NOT_FOUND)
    except PartsDetails.DoesNotExist:
        print("error")
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        parts_details_serializer = PartsDetailsSerializer(parts_details,
                                                          many=True)
        return Response(parts_details_serializer.data)
