import logging

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger()


class CommonMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        logger.exception('process error')

    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
