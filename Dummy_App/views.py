from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.template.response import TemplateResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from . import models, serializers, utils, constants
from rest_framework.response import Response
from django.conf import settings
import requests
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

# Create your views here.

class Login(APIView):
	"""
	User Login API
	:param request: {'username': 'XYZ_987', 'password': '123456'}
	An internal call to /api/token/ is sent to get access token which is then returned as response
	response: access token of JWT auth with user basic information
	"""
	def post(self, request):
			
		username = request.data.get('username')
		password = request.data.get('password')
		try:
			user = models.User.objects.get(username__iexact=username)
		except models.User.DoesNotExist:
			return Response({"error": constants.LOGIN_ERROR, "message": constants.USER_DOES_NOT_EXIST,
				"error_code":constants.USERNAME_ERROR}, status.HTTP_400_BAD_REQUEST)		
		serializer = serializers.UserLoginSerializer(user)
		if serializer.is_valid:
			if user.is_active:
				if user.check_password(password):						
					data = {"username":username,"password":password, 'email': username}
					response = requests.post(settings.BASE_URL + '/api/token/', data=data)
					access_token = response.json()
					bearer_token = access_token['access']
					headers = {"Authorization": "Bearer " + bearer_token}
					
					return utils.response({"user": serializer.data,
											   "tokens": access_token},
												headers=headers)
				return utils.response({"error": constants.LOGIN_ERROR, "message":constants.ENTER_CORRECT_PASSWORD,
					"error_code":constants.PASSWORD_ERROR}, status.HTTP_400_BAD_REQUEST)
		else:
			return utils.response({"message": "error"},
									  status.HTTP_400_BAD_REQUEST, utils.generate_error_message(serializer.errors))

