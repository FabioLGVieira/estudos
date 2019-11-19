package achaponto;

import java.util.Arrays;
import sun.misc.GC;

public class ListaPonto {

    private Ponto pontos[];
    private int validos;

    public ListaPonto(int N) {
        this.pontos = new Ponto[N];
        this.validos = 0;
    }

    public Ponto[] adicionarAoFinal(Ponto p) {
        if (validos < pontos.length) {
            this.pontos[validos] = p;
            this.validos++;
        } else {
            System.out.println("Lista Completa, Ponto nao adicionado");
        }
        return this.pontos;
    }

    public int adicionarNaPosicao() {
        return 0;
    }

    public int retornaIndice() {
        return 0;
    }

    public int removeElemento() {
        return 0;
    }

    public int CalculaDistancia() {
        return 0;
    }

    public int retornaPontosEmCircunferencia() {
        return 0;
    }

    @Override
    public String toString() {
        String vetor ="";
        for (int i = 0; i < this.validos; i++) {
            vetor += String.valueOf(pontos[i].toString())+" ";
        }
        return vetor;
    }
}
