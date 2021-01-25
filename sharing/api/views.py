from django.contrib.auth import logout, authenticate, login
from django.db.models import Q
from django.http import JsonResponse
from django.views import View
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    CreateAPIView
from rest_framework.permissions import IsAuthenticated

from sharing.api.permissions import IsShareableFileOwner, CanDownloadFile
from sharing.api.serializers import ShareableFileListSerializer, ShareableFileDetailSerializer, \
    ShareableFileCreateSerializer
from sharing.models import ShareableFile


class ShareableFileListView(ListAPIView):
    """
    File list of logged in user.
    """
    queryset = ShareableFile.objects.all()
    serializer_class = ShareableFileListSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = 'hash'
    lookup_url_kwarg = 'hash'

    def get_queryset(self):
        queryset = super(ShareableFileListView, self).get_queryset()
        return queryset.filter(
            Q(user=self.request.user.id)
        )


class ShareableFileDetailView(RetrieveAPIView):
    """
    Get file of logged in user.
    """
    queryset = ShareableFile.objects.all()
    serializer_class = ShareableFileDetailSerializer
    permission_classes = [
        CanDownloadFile,
    ]
    lookup_field = 'hash'
    lookup_url_kwarg = 'hash'


class ShareableFileUpdateView(RetrieveUpdateAPIView):
    """
    Update file of logged in user.
    """
    queryset = ShareableFile.objects.all()
    serializer_class = ShareableFileDetailSerializer
    permission_classes = [
        IsShareableFileOwner,
    ]
    lookup_field = 'hash'
    lookup_url_kwarg = 'hash'


class ShareableFileDeleteView(RetrieveDestroyAPIView):
    """
    Delete file of logged in user.
    """
    queryset = ShareableFile.objects.all()
    serializer_class = ShareableFileDetailSerializer
    permission_classes = [
        IsShareableFileOwner,
    ]
    lookup_field = 'hash'
    lookup_url_kwarg = 'hash'


class ShareableFileCreateView(CreateAPIView):
    """
    Delete file of logged in user.
    """
    queryset = ShareableFile.objects.all()
    serializer_class = ShareableFileCreateSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = 'hash'
    lookup_url_kwarg = 'hash'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LoginView(View):
    def post(self, request):
        logout(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not (username and password):
            return JsonResponse(data={
                'status': 'username and password parameters are required',
            }, status=400)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse(data={
                'status': 'ok',
            }, status=200)
        else:
            return JsonResponse(data={
                'status': 'wrong authentication data',
            }, status=403)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return JsonResponse({'status': 'ok'})
