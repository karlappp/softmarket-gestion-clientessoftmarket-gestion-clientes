# softmarket-gestion-clientes

Proyecto de gestión de clientes para SoftMarket S.A., aplicando principios SOLID y buenas prácticas de desarrollo con Git y GitHub.

Trabajo de la asignatura **Buenas Prácticas de Desarrollo de Software** (Presencial 24072).

## Integrantes
- Karla Gutiérrez Villero
- José Manuel Quintero Meléndez

## Objetivo y funcionalidades
- Modelar productos (`Producto`) validando que el precio no sea negativo.
- Registrar y consultar productos (`gestion_productos.py`).

## Requisitos
- Python 3.8 o superior. No requiere librerías externas.

## Instalación y uso
```bash
git clone https://github.com/karlappp/softmarket-gestion-clientessoftmarket-gestion-clientes.git
cd softmarket-gestion-clientessoftmarket-gestion-clientes
python main.py                 # prueba inicial de la clase Producto
python gestion_productos.py    # demo de registro y consulta
python -m unittest -v          # pruebas unitarias
```

## Estructura de archivos
| Archivo | Descripción |
|---|---|
| `productos.py` | Clase `Producto` (nombre y precio, con validación). |
| `gestion_productos.py` | Funciones `registrar_producto`, `consultar_productos` y `mostrar_productos`. |
| `test_gestion_productos.py` | Pruebas unitarias (`unittest`). |
| `main.py` | Prueba inicial de la clase `Producto`. |

## Modelo de ramas (Git Flow adaptado)
- `main`: versión estable, revisada y aprobada.
- `develop`: integración de funcionalidades en desarrollo.
- `feature/*`: una rama por funcionalidad, creada desde `develop` (por ejemplo `feature/productos`, `feature/gestion-productos`).
- `hotfix/*`: correcciones urgentes creadas desde `main`, que luego se integran en `main` y en `develop`.

Los cambios entran siempre mediante Pull Request revisado por otro integrante.

## Convención de commits
`feat:` nueva funcionalidad · `fix:` corrección · `docs:` documentación · `refactor:` reorganización · `test:` pruebas · `chore:` tareas de mantenimiento.
