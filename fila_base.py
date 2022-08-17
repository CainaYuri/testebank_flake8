class FilaBase:
    codigo: int = 0
    fila_prioritaria = []
    clientes_atendidos = []
    senha_atual = ''

    def reseta_fila(self)->None:
        if self.codigo >=100:
            self.codigo = 0
        else:
            self.codigo+=1
