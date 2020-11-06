from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
	return render(request,'home.html')

def result(request):
	cls = joblib.load('filename')
	lis=[]
	lis.append(request.GET['age'])
	lis.append(request.GET['gender'])


	ans = cls.predict([lis])

	return render(request,'result.html',{'ans':ans,'lis':lis})