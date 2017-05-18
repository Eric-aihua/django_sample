from rest_framework.metadata import BaseMetadata

__author__ = 'eric.sun'
class MinimalMetadata(BaseMetadata):
    """
    Don't include field and other information for `OPTIONS` requests.
    Just return the name and description.
    """
    def determine_metadata(self, request, view):
        return {
            'name': view.get_view_name(),
            'description': "this project is a rest_framework test size"
        }
