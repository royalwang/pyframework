from rest_framework import ISO_8601

REST_FRAMEWORK = {
    # Base API policies
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'app.http.middlewares.Authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),

    # Exception handling
    'EXCEPTION_HANDLER': 'app.exceptions.ExceptionHandler.exception_handler',

    # Generic view behavior
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': (),

    # Pagination
    'PAGE_SIZE': 20,

    # Input and output formats
    'DATE_FORMAT': ISO_8601,
    'DATE_INPUT_FORMATS': (ISO_8601,),

    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DATETIME_INPUT_FORMATS': ('%Y-%m-%d %H:%M:%S',),

    'TIME_FORMAT': ISO_8601,
    'TIME_INPUT_FORMATS': (ISO_8601,),
}
