from django.core.files.storage import FileSystemStorage
from skimage.io import imread
import pickle
from skimage.transform import resize
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes


model = pickle.load(open('./models/model.h5', 'rb'))

@parser_classes((MultiPartParser, ))
class PredictImage(APIView):
    def post(self,request,format=None):
        fileObj = request.FILES['image']
        fs = FileSystemStorage()
        filePathName = fs.save(fileObj.name,fileObj)
        filePathName = fs.url(filePathName)
        testimage = '.'+filePathName

        img = imread(testimage)
        img_resize=[resize(img,(150,150,3)).flatten()]
        Categories =['Healthy', 'LeafBlast', 'Hispa', 'BrownSpot']
        probability=model.predict_proba(img_resize)
        for ind,val in enumerate(Categories):
            print(f'{val} = {probability[0][ind]*100}%')
        print("The predicted image is : "+Categories[model.predict(img_resize)[0]])

        context = {'filePathName':filePathName,'predictedLabel':Categories[model.predict(img_resize)[0]]}

        return JsonResponse(context)

    def get(request):
        data={"Name":"Roshan"}
        return JsonResponse(data)


