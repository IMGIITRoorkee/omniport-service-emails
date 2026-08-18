import hmac

from rest_framework import permissions

from categories.models import Category


class HasCategoryToken(permissions.BasePermission):
    """
    Allows access only to callers presenting the token of the named category
    """

    def has_permission(self, request, view):
        """
        Check the token in the request against the token on the named category
        :param request: the request being checked for permissions
        :param view: the view to which the request was made
        :return: True if the request is allowed to proceed, False otherwise
        """

        slug = request.data.get('slug')
        token = request.data.get('token')
        if not isinstance(slug, str) or not isinstance(token, str):
            return False

        category = Category.objects.filter(slug=slug).first()
        if category is None:
            return False

        expected_token = (category.meta or {}).get('token')
        if not isinstance(expected_token, str) or not expected_token:
            return False

        if not hmac.compare_digest(
            token.encode('utf-8'),
            expected_token.encode('utf-8'),
        ):
            return False

        request.category = category
        return True
