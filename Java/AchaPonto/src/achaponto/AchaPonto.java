package achaponto;

import java.util.Scanner;
import achaponto.ListaPonto;

public class AchaPonto {
    
    static Scanner sc = new Scanner(System.in);
    
    public static void main(String[] args) {
        ListaPonto lp = new ListaPonto(5);
        int escolha = verificaEscolha(lp);
        
        while (escolha > 0 && escolha < 7) {
            
            //code
            verificaEscolha(lp);
        }
    }
    
    static void imprimeLista(){
        
    }

    static void imprimeEscolha() {
        System.out.println("Escolha uma opção:");
        System.out.println("1 - Adicionar um elemento no final da coleção");
        System.out.println("2 - Adicionar um elemento em uma posição da coleção");
        System.out.println("3 - Retornar o índice da primeira ocorrência de um elemento especificado na coleção");
        System.out.println("4 - Remover um elemento em uma posição na coleção");
        System.out.println("5 - Calcular a distância dos dois pontos mais distantes na coleção");
        System.out.println("6 - Retornar uma coleção de pontos contido em uma circunferência");
        System.out.println("0 - Sair");
        System.out.print("Opção: ");
    }

    static int verificaEscolha(ListaPonto lp) {
        imprimeEscolha();
        int escolha = sc.nextInt();
        switch (escolha) {
            case 0:
                System.exit(0);
                break;
            case 1:
                System.out.println("Forneça as Coordenadas:");
                System.out.print("X: ");
                int x = sc.nextInt();
                System.out.print("Y: ");
                int y = sc.nextInt();
                Ponto p = new Ponto(x,y);
                lp.adicionarAoFinal(p);
                System.out.println(lp.toString());//tirar no fim
                break;
            case 2:
                break;
            case 3:
                break;
            case 4:
                break;
            case 5:
                break;
            case 6:
                break;
            default:
                System.out.println("Escolha uma opção valida");
                break;
        }
        return escolha;
    }

}
