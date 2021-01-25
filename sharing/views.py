from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.views import View

from sharing.models import ShareableFile


class FileView(View):
    def get(self, request, file_hash):
        try:
            obj = ShareableFile.objects.get(hash=file_hash)
        except ShareableFile.DoesNotExist:
            return HttpResponse(status=404)
        if obj.user != request.user and not obj.public:
            return HttpResponse(status=401)
        response = HttpResponse(content=obj.file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(obj.name)
        response['X-Sendfile'] = smart_str(obj.file.path)
        return response
