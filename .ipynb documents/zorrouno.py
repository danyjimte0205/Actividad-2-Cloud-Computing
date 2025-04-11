import pandas as pd

class processor:
    @staticmethod
    def embbed(d):
        """
        Procesamiento para datos de bancarrota:
        1. Elimina columnas no numéricas/innecesarias
        2. Conserva todas las features financieras
        """
        try:
            # Eliminar solo columnas no relevantes para el modelo
            cols_to_drop = ['Bankrupt?']  # Conservamos esta para el target
            if 'RowNumber' in d.columns:
                cols_to_drop.append('RowNumber')
                
            d = d.drop(cols_to_drop, axis=1, errors='ignore')
            
            # Convertir nombres de columnas al formato esperado
            d.columns = ['_' + col.replace(' ', '_').replace('-', '_').replace('(', '').replace(')', '').replace('%', 'percent') 
                        for col in d.columns]
            
        except Exception as e:
            print(f"Error en procesamiento: {str(e)}")
        return d