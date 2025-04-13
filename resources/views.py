from django.shortcuts import render
# Import APIView, the base class for creating API views in Django REST Framework (DRF)
from rest_framework.views import APIView
from rest_framework.response import Response
# Import status to set HTTP status codes (e.g., 200 OK)
from rest_framework import status
# Import the EducationalResource model to query the database
from .models import EducationResource
# Import the serializer to convert model instances to JSON
from .serializers import EducationalResourceSerializer

# Create your views here.

#a class for handling GET requests....
class ResourceListView(APIView):
    #get method to handle http requests
    def get(self, request, format=None):
        #the the disease query parameter from the URL, if no disease query parameter in the url, return none
        disease = request.query_params.get('disease',None)

        #query all EducationResource objects from the database
        resources = EducationResource.objects.all()

        #if a disease parameter is provided, query the resources by that parameter
        if disease:
            resources = resources.filter(disease=disease)

        #serialize into the fetched data from the datase into a json
        # many=True indicates multiple objects
        serializer = EducationalResourceSerializer(resources, many=True)

        # Return the serialized data with HTTP 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)
