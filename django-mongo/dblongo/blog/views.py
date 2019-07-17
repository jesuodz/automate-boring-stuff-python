# from django.shortcuts import render, get_object_or_404
# from rest_framework.response import Response
# from rest_framework import status

# # from .models import Post

# def get_post_REQ(request):
#     doc = {
#         'title': 'Hello',
#         'content': 'World',
#         'author': 'jesuodz'
#     }

#     post = Post(doc)
#     post.save()
    
#     if request.method == 'GET':
#         print("\nWE HAVE A GET!\n")

#     return Response(status=status.HTTP_404_NOT_FOUND)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

@api_view(['GET', 'POST'])
def get_post_REQ(request):
    # get all posts
    if request.method == 'GET':
        return Response({})
    # insert a new record for a post
    elif request.method == 'POST':
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'author': request.data.get('author')
        }

        post = Post(title=data['title'])
        post.save()

        # serializer = PostSerializer(data=data)
        # print(serializer.Meta.print_data())
        # print(serializer)
        # if serializer.is_valid(): print("OK")

        return Response({})
        # if serializer.is_valid():
        #     # serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors)

