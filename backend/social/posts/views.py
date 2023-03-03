from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse,reverse_lazy
from django.views import generic
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .pagination import PostSetPagination
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import (
                                        HTMLFormRenderer, 
                                        JSONRenderer, 
                                        BrowsableAPIRenderer,
                                    )

response_schema_dictposts = {
    "200": openapi.Response(
        description="Successful Operation",
        examples={
            "application/json": {
    "results": [
        {
            "type": "post",
            "title": "Funny post",
            "id": "5ad63a2b-4890-47b8-bc24-979a96941863",
            "description": "This is a funny joke. Laugh.",
            "contentType": "text/plain",
            "content": "I tried to catch fog the other day, I Mist.",
            "author": {
                "type": "author",
                "id": "866ff975-bb49-4c75-8cc8-10e2a6af44a0",
                "displayName": "Fahad",
                "url": "",
                "profileImage": ""
            },
            "categories": [
                "Funny"
            ],
            "comments": "/comments/",
            "published": "2023-03-03T14:45:41.208691-07:00",
            "visibility": "PUBLIC"
        },
        {
            "type": "post",
            "title": "Sad post",
            "id": "3e227dbd-986f-4f3b-9872-2f81d9c6335f",
            "description": "Sad post,Cry",
            "contentType": "text/plain",
            "content": "Hi this is very sad :(",
            "author": {
                "type": "author",
                "id": "866ff975-bb49-4c75-8cc8-10e2a6af44a0",
                "displayName": "Fahad",
                "url": "",
                "profileImage": ""
            },
            "categories": [
                "Sad"
            ],
            "comments": "/comments/",
            "published": "2023-03-03T14:47:10.782792-07:00",
            "visibility": "PUBLIC"
        }
    ]
}
        }
        
    )}

response_schema_dictpost = {
    "200": openapi.Response(
        description="Successful Operation",
        examples={
            "application/json": {
    "type": "post",
    "title": "Sad post",
    "id": "3e227dbd-986f-4f3b-9872-2f81d9c6335f",
    "description": "Sad post,Cry",
    "contentType": "text/plain",
    "content": "Hi this is very sad :(",
    "author": {
        "type": "author",
        "id": "866ff975-bb49-4c75-8cc8-10e2a6af44a0",
        "displayName": "Fahad",
        "url": "",
        "profileImage": ""
    },
    "categories": [
        "Sad"
    ],
    "comments": "/comments/",
    "published": "2023-03-03T14:47:10.782792-07:00",
    "visibility": "PUBLIC"
}
        }
        
    )}

response_schema_dictdelete = {
    
    "204":openapi.Response(description="Successful Deletion",)}


response_schema_dictComments = {
    "200": openapi.Response(
        description="Successful Operation",
        examples={
            "application/json": [
    {
        "type": "comment",
        "author": {
            "type": "author",
            "id": "866ff975-bb49-4c75-8cc8-10e2a6af44a0",
            "displayName": "Fahad",
            "url": "",
            "profileImage": ""
        },
        "comment": "Wow haha funny dude!",
        "contentType": "text/plain",
        "published": "2023-03-03T15:03:31.309896-07:00",
        "id": "412be771-19bf-4452-9e84-549a52916951"
    }
]
        }
    )}

class post_list(APIView, PageNumberPagination):
    serializer_class = PostSerializer
    pagination_class = PostSetPagination
    @swagger_auto_schema(responses=response_schema_dictposts,operation_summary="List of Posts for an Author")
    def get(self, request, pk_a):
        """
        Get the list of posts on our website
        """
        author = Author.objects.get(id=pk_a)
        posts = Post.objects.filter(author=author)
        posts = self.paginate_queryset(posts, request) 
        serializer = PostSerializer(posts, many=True)
        return  self.get_paginated_response(serializer.data)

    @swagger_auto_schema(responses=response_schema_dictposts,operation_summary="Create a new Post for an Author")

    def post(self, request, pk_a):
        """
        New post for an Author
        """
        pk = str(uuid.uuid4())
        
        try:
            author = Author.objects.get(pk=pk_a)
        except Author.DoesNotExist:
            error_msg = "Author id not found"
            return Response(error_msg, status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(data=request.data, context={'author_id': pk_a})
        if serializer.is_valid():
            serializer.validated_data.pop("author")
            post = Post.objects.create(**serializer.validated_data, author=author, id = pk)
            post.update_fields_with_request(request)

            serializer = PostSerializer(post, many=False)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class post_detail(APIView, PageNumberPagination):
    serializer_class = PostSerializer
    pagination_class = PostSetPagination

    @swagger_auto_schema(responses=response_schema_dictpost,operation_summary="Get a particular post of an author")
    def get(self, request, pk_a, pk):
        """
        Get a particular post of an author
        """
        try: 
            author = Author.objects.get(id=pk_a)
            post = Post.objects.get(author=author, id = pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist: 
            return self.put(request, pk_a, pk)
    @swagger_auto_schema(responses=response_schema_dictpost,operation_summary="Create a particular post of an author") 
    def post(self, request, pk_a, pk):       
        
        try:
            _ = Author.objects.get(pk=pk_a)
        except Author.DoesNotExist:
            error_msg = "Author id not found"
            return Response(error_msg, status=status.HTTP_404_NOT_FOUND)
        
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            error_msg = "Post id not found"
            return Response(error_msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            post = serializer.save()
            post.update_fields_with_request(request)           
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses=response_schema_dictdelete,operation_summary="Delete a particular post of an author") 
    def delete(self, request, pk_a, pk):
        """
        Deletes the post given by the particular authorid and postid
        """

        # TODO: check permissions 

        try: 
            post = Post.objects.get(id=pk)
            post.delete()
            post.save()
            print(post.title)
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response("Post does not exist",status=status.HTTP_404_NOT_FOUND)
      

    @swagger_auto_schema(responses=response_schema_dictpost,operation_summary="Update a particular post of an author") 
    def put(self, request, pk_a, pk):
        """
        Updates the post given by the particular authorid and postid
        """

        try:
            author = Author.objects.get(id=pk_a)
            try:
                _ = Post.objects.get(id=pk)
                return Response("Post already exists", status=status.HTTP_400_NOT_FOUND)
            except Post.DoesNotExist:
                pass
        except Author.DoesNotExist:
            author = Author.objects.get(id=pk_a)
            Response("Author does not exist", status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(data=request.data, context={'author_id': pk_a})
        if serializer.is_valid():
            serializer.validated_data.pop("author")
            post = Post.objects.create(**serializer.validated_data, author=author, id=pk)
            post.update_fields_with_request(request)

            serializer = PostSerializer(post, many=False)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@swagger_auto_schema( method='get',responses=response_schema_dictComments,operation_summary="Get the comments on a post")
@api_view(['GET'])
def get_comments(request, pk_a, pk):
    """
    Get the list of comments on our website
    """
    author = Author.objects.get(id=pk_a)
    post = Post.objects.get(author=author, id=pk)
    comments = Comment.objects.filter(author=author,post=post)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@swagger_auto_schema( method='get',responses=response_schema_dictpost,operation_summary="Get a partdsfdidsf of an author")
@api_view(['GET'])
def get_likes(request, pk_a, pk):
    """
    Get the list of comments on our website
    """
    post = Post.objects.get(id=pk)
    likes = Like.objects.filter(object=post.id)
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by('title')[:5]

class DetailView(generic.DetailView):
    model = Post
    context_object_name = 'postt'
    template_name = 'posts/detail.html'
    