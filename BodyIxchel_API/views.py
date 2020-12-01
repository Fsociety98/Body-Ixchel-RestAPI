# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
#import io
from rest_framework.parsers import JSONParser
# Serializers
from BodyIxchel_API.serializers import UsuarioLoginSerializer, UsuarioSerializer, UsuarioRegistroSerializer, UsuarioModificarDatosSerializer, UsuarioInactivoSerializer, RecoverPasswordLogSerializer, NewPasswordSerializer, RecoverPasswordLogUpdateSerializer, MastografiaSerializer, MastografiaUpdateSerializer

# Models
from BodyIxchel_API.models import Usuario, RecoverPasswordLog, Mastografia
#---- Email
from BodyIxchel_API.email import SecretCode, getAlternativeText, getHTMLBase, EmailHandled
from datetime import date

#---- IA 
from BodyIxchel_API.MastografiaAnomaliaDetector import MastografiaAnomaliaDetector
import os
from PIL import Image
import base64

#------------ Errors Headler ---------------

def ErrorMessage(message, statusCode):
    return Response({'statusCode': statusCode, 'message' : message}, status=statusCode)

def ErrorArrayToString(errorArray):

    _listErrors = []

    for error in errorArray:
        _listErrors.append(str(error[0]))

    return _listErrors

#------------ Errors Headler ---------------


#------------ Authentication ---------------

class AuthenticationViewSet(viewsets.GenericViewSet):

    queryset = Usuario.objects.filter(is_active=True)
    serializer_class = UsuarioSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post.

    #/api/authentication/login/
    #BODY: {"email": "", "password": ""}

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UsuarioLoginSerializer(data=request.data)
        #if serializer.is_valid(raise_exception=True):
        if serializer.is_valid():

            usuario, token = serializer.save()
            data = {
                'usuario': UsuarioSerializer(usuario).data,
                'access_token': token
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else :
            return ErrorMessage(ErrorArrayToString(serializer.errors.values()), status.HTTP_400_BAD_REQUEST)

    
    #/api/authentication/create_account/
    #BODY : {"nombre": "", "apellidoPaterno": "", "apellidoMaterno": "", "fechaNacimiento": "YYYY-MM-DD",
    #"email": "", "password": "", "password_confirmation" : "" }

    @action(detail=False, methods=['post'])
    def create_account(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        #if serializer.is_valid(raise_exception=True):
        if serializer.is_valid():
            usuario = serializer.save()
            data = UsuarioSerializer(usuario).data
            return Response(data, status=status.HTTP_201_CREATED)
        else :
            return ErrorMessage(ErrorArrayToString(serializer.errors.values()), status.HTTP_400_BAD_REQUEST)

    #/api/authentication/logout/
    #HEADERS: [KEY : Authorization, VALUE : Token {token}]

    @action(detail=False, methods=['get'])
    def logout(self, request, format=None):
        queryset = self.get_queryset()
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


#------------ Authentication ---------------

# --------Recuperar Contraseña-------

#/api/recover-password
#BODY : {"email": ""}

@api_view(["POST"])
def recoverPassword(request):
    queryset = Usuario.objects.filter(email=request.data['email'])

    validator = queryset.exists()

    if validator == True :
        oSecretCode = SecretCode()
        oSecretCode.generate()

        today = date.today()

        usuario_serializer = UsuarioSerializer(queryset, many=True)
        recoverPasswordLog_serializer = RecoverPasswordLogSerializer(data= {"codigo": str(oSecretCode.getAllCadena()), "fechaSolicitud": today, "usuario": usuario_serializer.data[0]['usuarioId']})

        if recoverPasswordLog_serializer.is_valid():
            
            oEmailHandled = EmailHandled("soporte.bodyixchel@gmail.com", str(usuario_serializer.data[0]['email']), "Ixchel123@", "Recuperar Contraseña", getHTMLBase(oSecretCode.getNumber1(), oSecretCode.getNumber2(), oSecretCode.getNumber3(), oSecretCode.getNumber4()), getAlternativeText(str(oSecretCode.getAllCadena())))
            oEmailHandled.sendHTMLEmail()

            recoverPasswordLog = recoverPasswordLog_serializer.save()
            data = RecoverPasswordLogSerializer(recoverPasswordLog).data
            return Response(data, status=status.HTTP_200_OK)
        else :
            #print(recoverPasswordLog_serializer.errors.values())
            return ErrorMessage(ErrorArrayToString(recoverPasswordLog_serializer.errors.values()), status.HTTP_400_BAD_REQUEST)
    else :
        return ErrorMessage('Usuario no registrado y/o inactivo.', status.HTTP_404_NOT_FOUND)


#/api/check-password
#BODY : {"code": "" }

@api_view(["POST"])
def checkCode(request):
    
    today = date.today()
    queryset = RecoverPasswordLog.objects.filter(codigo=request.data['code'], fechaSolicitud = today, validado = False)

    validator = queryset.exists()

    if validator == True :

        return ErrorMessage('Validado', status.HTTP_200_OK)
    else:
        return ErrorMessage('Solicitud expirada, por favor, intente de nuevo.', status.HTTP_404_NOT_FOUND)

#/api/change-password
#BODY : {"code": "", "password": "", "password_confirmation" : "" }

@api_view(["POST"])
def changePassword(request):
    today = date.today()
    queryset = RecoverPasswordLog.objects.filter(codigo=request.data['code'], fechaSolicitud = today, validado = False)

    validator = queryset.exists()

    if validator == True :
        recoverPasswordLog_serializer = RecoverPasswordLogSerializer(queryset, many=True)
        querysetUsuario = Usuario.objects.filter(is_active=True, usuarioId=recoverPasswordLog_serializer.data[0]['usuario'])
        usuario_serializer = UsuarioSerializer(querysetUsuario, many=True)

        newPassword_serializer = NewPasswordSerializer(data={'password': request.data['password'], 'password_confirmation' : request.data['password_confirmation']})
        
        if newPassword_serializer.is_valid():
            u = Usuario.objects.get( usuarioId=recoverPasswordLog_serializer.data[0]['usuario'])
            u.set_password(request.data['password'])
            u.save()

            q = RecoverPasswordLog.objects.get(recoverPasswordLogId=recoverPasswordLog_serializer.data[0]['recoverPasswordLogId'])
            recoverPasswordLogUpdate_serializer = RecoverPasswordLogUpdateSerializer(q, data={'validado': 'True'})

            if recoverPasswordLogUpdate_serializer.is_valid():
                recoverPasswordLogUpdate_serializer.save()

                return ErrorMessage('Contraseña actualizada con éxito.', status.HTTP_201_CREATED)
            else:
                return ErrorMessage(ErrorArrayToString(recoverPasswordLogUpdate_serializer.errors.values()), status.HTTP_400_BAD_REQUEST)

        else :

            return ErrorMessage(ErrorArrayToString(newPassword_serializer.errors.values()), status.HTTP_400_BAD_REQUEST)

    else:
        return ErrorMessage('Solicitud expirada, por favor, intente de nuevo.', status.HTTP_404_NOT_FOUND)

#-- APARTIR DE AQUI TODOS :: HEADERS: [KEY : Authorization, VALUE : Token {token}]

#------------ Usuario ---------------

#/api/users/all
@api_view(["GET"])
@permission_classes([IsAuthenticated])  
def getUsers(request):
    queryset = Usuario.objects.filter(is_active=True)
    serializer = UsuarioSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#/api/users/detail/{user_id}
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUser(request, user_id):

    queryset = Usuario.objects.filter(is_active=True, usuarioId=user_id)
    validator = queryset.exists()

    if validator == True :
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else :
        #return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        return ErrorMessage('Usuario no encontrado.', status.HTTP_404_NOT_FOUND)
  

#/api/users/update/{user_id}
#BODY : {"nombre": "", "apellidoPaterno": "", "apellidoMaterno": "", "fechaNacimiento": "YYYY-MM-DD",
#"email": "" }

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateUser(request, user_id, format=None):

    try:
        print(request.data)
        queryset = Usuario.objects.get(usuarioId=user_id)
        serializer = UsuarioModificarDatosSerializer(queryset, data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except ObjectDoesNotExist:
        return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

 #/api/users/delete/{user_id}
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteUser(request, user_id, format=None):

    try:
        
        queryset = Usuario.objects.get(usuarioId=user_id)
        serializer = UsuarioInactivoSerializer(queryset, data= {"is_active": "false"})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except ObjectDoesNotExist:
        return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)


#------------ Usuario ---------------

# -----------Mastografia---------------
#/api/mastografias/analyze
@api_view(["POST"])
#@permission_classes([IsAuthenticated])
def analyzeMastografia(request):
    today = date.today()

    serializer = MastografiaSerializer(data={'imagen': request.FILES['mastografia'], 'fechaEscaneo': today, 'usuario': request.data['usuarioId']})

    if serializer.is_valid():
        mastografia = serializer.save()
        data = MastografiaSerializer(mastografia).data
        
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        print(data['imagen'])
        oMastografiaAnomaliaDetector = MastografiaAnomaliaDetector('{0}/AnomaliaModelDetector.xml'.format(BASE_DIR),'{0}{1}'.format(BASE_DIR,data['imagen']),'Anomalia')

        oSecretCode = SecretCode()
        oSecretCode.generate()

        NAME_IMG_RESULTADO = 'MastografiaResultado_User_{0}_{1}_{2}.jpg'.format(data['usuario'],today, oSecretCode.getAllCadena())

        oMastografiaAnomaliaDetector.saveImage(oMastografiaAnomaliaDetector.analize(),'{0}{1}'.format(MEDIA_ROOT,'/mastografias/resultados/{0}'.format(NAME_IMG_RESULTADO)))

        RUTA_IMG_RESULTADO = 'mastografias/resultados/' + NAME_IMG_RESULTADO
        #oMastografiaAnomaliaDetector.saveImage(oMastografiaAnomaliaDetector.analize(),RUTA_IMG_RESULTADO)
     
        queryset = Mastografia.objects.get(mastografiaId=data['mastografiaId'])
        resultSerializer = MastografiaUpdateSerializer(queryset, data={'rutaImagenResultado': RUTA_IMG_RESULTADO, 'check':'true', 'anomaliasEncontradas': oMastografiaAnomaliaDetector.getNumberFoundOfAnomalias()})

        if resultSerializer.is_valid():
            resultMastografia = resultSerializer.save()
            resultData = MastografiaSerializer(resultMastografia).data

            return Response(resultData, status=status.HTTP_201_CREATED)
        
        else:
            return ErrorMessage(ErrorArrayToString(resultSerializer.errors.values()), status.HTTP_400_BAD_REQUEST)

    else :
        return ErrorMessage(ErrorArrayToString(serializer.errors.values()), status.HTTP_400_BAD_REQUEST)


#/api/mastografias/result/{mastografia_id}
@api_view(["GET"])
#@permission_classes([IsAuthenticated])
def getMastografia(request, mastografia_id):

    queryset = Mastografia.objects.filter(check=True, mastografiaId=mastografia_id)

    validator = queryset.exists()

    if validator == True :
        serializer = MastografiaSerializer(queryset, many=True)

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

        RUTA_IMG_RESULTADO ='{0}/{1}'.format(MEDIA_ROOT, serializer.data[0]['rutaImagenResultado'])

        STR_IMG_BASE_64 = ""

        with open(RUTA_IMG_RESULTADO, "rb") as imageFile:
            STR_IMG_BASE_64 = base64.b64encode(imageFile.read())

        return Response(STR_IMG_BASE_64, status=status.HTTP_200_OK)
    else :

        return ErrorMessage('Mastografia no encontrada.', status.HTTP_404_NOT_FOUND)


#/api/mastografias/list/{usuario_id}
@api_view(["GET"])
#@permission_classes([IsAuthenticated])
def getMastografias(request, usuario_id):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    queryset = Mastografia.objects.filter(check=True, usuario=usuario_id)

    MastografiaList = []

    for mastografia in queryset:
        RUTA_IMG ='{0}/{1}'.format(MEDIA_ROOT, str(mastografia.imagen))  
        STR_IMG_BASE_64 = ""

        with open(RUTA_IMG, "rb") as imageFile:
            STR_IMG_BASE_64 = base64.b64encode(imageFile.read())


        RUTA_IMG_RESULTADO ='{0}/{1}'.format(MEDIA_ROOT, mastografia.rutaImagenResultado)
        STR_IMG_RESULTADO_BASE_64 = ""

        with open(RUTA_IMG_RESULTADO, "rb") as imageFile:
            STR_IMG_RESULTADO_BASE_64 = base64.b64encode(imageFile.read())
        

        MastografiaList.append({'mastografiaId': mastografia.mastografiaId, 'fechaEscaneo': str(mastografia.fechaEscaneo), 'anomaliasEncontradas': mastografia.anomaliasEncontradas, 'usuario': mastografia.usuario.usuarioId, 'check': mastografia.check, 'imagen': STR_IMG_BASE_64, 'rutaImagenResultado': STR_IMG_RESULTADO_BASE_64})

    return Response(MastografiaList, status=status.HTTP_200_OK)

