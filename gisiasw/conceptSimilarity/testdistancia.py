
from Graph import distancia_key_entity as dke_recursiva
from simpleGraphGenerator import dke as dke_acumulativa
from simpleGraphGenerator import get_entities_by_level_sin_acumular

key = "Python_(programming_language)"
entity = "Artificial_intelligence"

print get_entities_by_level_sin_acumular(key,6)

# print dke_acumulativa(key,entity)
# print  len (dke_recursiva(key,entity)) - 1


