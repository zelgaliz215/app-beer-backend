# app-beer-backend 

# Backen en python usando flask y bluprints

## Estructura de la app
my-beer-app/
├── app-beer-backend /
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── run.py
│   └── modules/
│       ├── __init__.py
│       ├── users/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   ├── routes.py
│       │   └── ...
│       ├── inventory/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   ├── routes.py
│       │   └── ...
│       ├── transactions/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   ├── routes.py
│       │   └── ...
│       ├── orders/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   ├── routes.py
│       │   └── ...
└── frontend/
    ├── package.json
    ├── next.config.js
    ├── tailwind.config.js
    ├── pages/
    │   ├── _app.js
    │   ├── index.js
    │   ├── users.js
    │   ├── inventory.js
    │   ├── transactions.js
    │   ├── orders.js
    │   └── ...
    └── components/
        ├── Navbar.js
        ├── Layout.js
        └── ...

## Ejecutar la instalacion de dependencias

- Usar el script desde la raiz del backend:

```bash
source scripts/install_dependencies.sh
```

##