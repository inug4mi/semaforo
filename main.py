import datetime
import random

DIA_SEMANA = "Jueves"
TIEMPO_SEMAFORO_ROJO = 0
TIEMPO_SEMAFORO_VERDE = 0

GANANCIAS_POR_HORA=[0,0,0,0,0,0,0,0,0,0]
GANANCIA_INSTANTE = {"ganancia":0,"hora":datetime.time()}

inversion_dia = 0
ganancia_dia = 0

inventario = {
    "dulces": {"precio": random.randint(200, 800), "stock": 100},
    "cigarrillos": {
        "starlite": {"precio": 700, "stock": 10},
        "boston": {"precio": 800, "stock": 10},
        "lucky-verde": {"precio": 1000, "stock": 10},
        "lucky-azul": {"precio": 1000, "stock": 10},
        "lucky-rojo": {"precio": 1000, "stock": 10},
        "malboro rojo": {"precio": 1000, "stock": 10},
        "malboro fuxion": {"precio": 1000, "stock": 10}
    }
}

frase_de_entrada = (
    "caballero/dama "
    "mentas, cigarrillos, dulces, tamarindos, con mucho gusto, a la orden "
    "dios lo bendiga"
)



