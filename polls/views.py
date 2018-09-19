from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from polls.models import Snippet,User
from polls.serializers import SnippetSerializer,UserregistrationSerializer,LoginSerializer,UserUpdateSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@api_view(['GET', 'POST'])
def snippet_list(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserLogin(APIView):


    def post(self,request):
        
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            kwargs = {
            "username":request.data['username'],"password":request.data['password']
            }
            
            try:
                user_obj = User.objects.get(username=kwargs['username'])
                print user_obj,"user_obj"
                if not user_obj.is_superuser:
                    if user_obj.check_password(kwargs['password']):
                        user_data={
                        "username":user_obj.username,
                        "id":user_obj.id,
                        "age":user_obj.age,
                        "mobile_number":user_obj.mobile_number,
                        "first_name":user_obj.first_name,
                        "last_name":user_obj.last_name,
                        "department":user_obj.department.name
                        }
                        return Response({"msg":"You are logged in successfully","data":user_data,"success":True})
                    else:
                        return Response({"msg":"Password Wrong"})
                else:
                    if user_obj.check_password(kwargs['password']):

                        user_data={
                            "username":user_obj.username,
                            "id":user_obj.id,
                         
                            "department":"None"
                            }
                        return Response({"msg":"You are logged in successfully","data":user_data,"success":True})
                    

                # else:
                # 	return Response(serializer.errors)

            except Exception as e:
                print (e)
                return Response({"msg":"No matching username"})
            else:
                return Response(serializer.errors,"sdfgfgsfdg",status=400)
    def get(self,request):
    	serializer=LoginSerializer()
    	return Response(serializer.data)




class UserRegistration(APIView):
    @method_decorator(login_required)
    def get(self,request):
        serializer = UserregistrationSerializer()
        return Response(serializer.data)
    def post(self,request):
        serializer = UserregistrationSerializer(data =request.data)
        
        if serializer.is_valid():
            try:
                user_form_data= {

                    "username":request.data['username'],
                    "first_name":request.data['first_name'],
                    "last_name":request.data['last_name'],
                    "mobile_number":request.data['mobile_number'],
                    "age":request.data['age'],
                    "password":request.data['password']
                }
                
                try:
                    user_obj = User.objects.get(mobile_number=user_form_data['mobile_number'])
                    user_obj.first_name=request.data['first_name']
                    user_obj.last_name=request.data['last_name']
                    user_obj.username=request.data['username']
                    user_obj.age=request.data['age']
                    user_obj.password=request.data['password']
                    user_obj.set_password(request.data['password'])
                    user_obj.save()

                    return Response({"msg":"You're details updated successfully"})
                	# user_obj.save()
                	# return Response({"msg":"you're details are updated successfully"})
                except Exception as e:

                	user_obj = User.objects.create(**user_form_data)
                
	                user_obj.set_password(request.data['password'])
	                print user_obj,"************************"
	                user_obj.save()

                	return Response({"msg":"you are registration is successful"})
            except Exception as e:
                
                return Response({serializer.errors},status=400)
        else:
            
            return Response(serializer.errors,"dfgsdfgsdfgdfsgdsgdsgds")

class GetAllUsers(APIView):
	def get(self,request):
		user_obj=User.objects.all().values('first_name','last_name','mobile_number','id','age','username').exclude(username='root')
		return Response(user_obj,status=200)	


class GetUsers_by_loginUser(APIView):

    def post(self,request):
        if request.data['department'] != 'None':
            user_obj = User.objects.filter(department__name=request.data['department']).values('first_name','last_name','mobile_number','id','age','username','department__name')
        else:
            user_obj = User.objects.all().values('first_name','last_name','mobile_number','id','age','username','department__name')
        return Response(user_obj,status=200)

