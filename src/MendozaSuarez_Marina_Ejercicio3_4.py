
from MendozaSuarez_Marina_Ejercicio2 import Gen

'''La clase tRNA ya tiene el metodo longitud heredado de Gen'''
class tRNA(Gen):
    def __init__(self, nombre, secuencia, especie=None, anticodon=None, aminoacido=None):
        super().__init__(nombre, secuencia, especie)
        self.anticodon = anticodon
        self.aminoacido = aminoacido
        # Si se proporciona un aminoacido, ARNt ya esta cargado
        self.carga = True if aminoacido else False

    def validar_anticodon(self):
        bases_validas = {'A', 'U', 'G', 'C'}
        if self.anticodon and (len(self.anticodon) == 3) and all(b in bases_validas for b in self.anticodon):
            return True
        else:
            raise ValueError("Anticodon invalido.")
    
    def codon_complementario(self):
        pares = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}
        return ''.join(pares[b] for b in self.anticodon[::-1])
    
    def cargar_aminoacido(self, aminoacido):
        self.aminoacido = aminoacido
        self.carga = True
    
    def descargar(self):
        self.aminoacido = None
        self.carga = False
    
    def resumen(self):
        base = super().resumen()
        extra = f" Anticodon: {self.anticodon}, Aminoacido: {self.aminoacido if self.aminoacido else 'no cargado'}."
        return base + extra
        
class ncRNA(Gen):
    def __init__(self, nombre, secuencia, especie=None, tipo=None, objetivo=None):
        super().__init__(nombre, secuencia, especie)
        self.tipo = tipo
        self.objetivo = objetivo
        self.estructura_secundaria = None

    def predecir_estructura(self, estructura):
        """Asigna una estructura secundaria (string o notación dot-bracket)."""
        self.estructura_secundaria = estructura

    def apuntar_gen(self, gen_objetivo):
        """Define el gen objetivo para un ncRNA regulador."""
        self.objetivo = gen_objetivo

    def resumen(self):
        base = super().resumen()
        tipo_str = f" Tipo: {self.tipo}" if self.tipo else ""
        objetivo_str = f", Objetivo: {self.objetivo}" if self.objetivo else ""
        return base + tipo_str + objetivo_str


class Proteina(tRNA):
    def __init__(self, nombre, secuencia, especie=None, anticodon=None, aminoacido=None, secuencia_aminoacidos=None):
        super().__init__(nombre, secuencia, especie, anticodon, aminoacido)
        self.secuencia_aminoacidos = secuencia_aminoacidos or ""
    
    def agregar_aminoacido(self, aa):
        """Agrega un aminoacido a la secuencia de la proteina."""
        self.secuencia_aminoacidos += aa

    def longitud_proteina(self):
        """Devuelve el numero de aminoacidos."""
        return len(self.secuencia_aminoacidos)

    def resumen(self):
        base = super().resumen()
        prot_info = f" Secuencia proteina: {self.secuencia_aminoacidos} ({self.longitud_proteina()} aa)"
        return base + prot_info


# Crear un tRNA cargado con Metionina
trna1 = tRNA(nombre="tRNA-Met", secuencia="ATGCGTACG", especie="Homo sapiens",
             anticodon="AUG", aminoacido="Met")

print(trna1.resumen())  # Resumen completo
print("Codon complementario:", trna1.codon_complementario())

# Descargar el aminoacido
trna1.descargar()
print(trna1.resumen())


# Crear un ncRNA regulador tipo miRNA
mirna1 = ncRNA(nombre="miR-21", secuencia="TTGACAGTT", especie="Homo sapiens",
               tipo="miRNA", objetivo="PTEN")

# Asignar estructura secundaria
mirna1.predecir_estructura("(((...)))")

print(mirna1.resumen())
print("Estructura secundaria:", mirna1.estructura_secundaria)

# Crear una proteina usando un tRNA como base
prot1 = Proteina(nombre="ProteinaX", secuencia="ATGCGTACG", especie="Homo sapiens",
                anticodon="AUG", aminoacido="Met")

# Agregar aminoacidos
prot1.agregar_aminoacido("M")  # Metionina
prot1.agregar_aminoacido("A")  # Alanina
prot1.agregar_aminoacido("G")  # Glicina

print(prot1.resumen())
print("Longitud proteina:", prot1.longitud_proteina())
