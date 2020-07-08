from .base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'remote':{

            'ENGINE': 'sql_server.pyodbc',
            'NAME': 'INEI_BDIPC_LIMA',
            'USER': 'Administrador',
            'PASSWORD': 'Pa$$w0rd2020',
            'HOST': 'azureipc2020.database.windows.net',
            'PORT': '1433',

            'OPTIONS': {
                'driver': 'ODBC Driver 13 for SQL Server',
            },

    }
}
DATABASE_ROUTERS = ['core.dbrouters.RemoteRouter']