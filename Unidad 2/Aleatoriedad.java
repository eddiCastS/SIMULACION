import java.util.Random;
public class Aleatoriedad {
    public static void main(String[] args) {
        Random rand = new Random();
        int[] binario = new int[100];
        for (int i = 0; i < 100; i++) binario[i] = rand.nextDouble() > 0.5 ? 1 : 0;
        int runs = 1;
        for (int i = 1; i < binario.length; i++) if (binario[i] != binario[i-1]) runs++;
        System.out.println("Número de runs: " + runs);
    }
}
