class Gen:
    
    def __init__(self, nombre, secuencia, especie=None):
        """Constructor y atributos"""
        self.nombre = nombre
        self.secuencia = secuencia
        self.especie = especie
        
        bases_validas = {'A', 'T', 'G', 'C'}
        if not all(base in bases_validas for base in self.secuencia):
            raise ValueError("La secuencia contiene caracteres no validos (solo A, T, G, C permitidos).")
        
    
    def longitud(self):
        """Regresa la longitud de la secuencia en bases"""
        return len(self.secuencia)
    
    def resumen(self):
        """Devuelve un resumen breve con la info del gen"""
        return f"Gen: {self.nombre} ({self.especie if self.especie else 'Especie desconocida'}), {self.longitud()} bases."
    
