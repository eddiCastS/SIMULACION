import java.util.Random;

public class Biominal {
    public static void main(String[] args) {
        Random rand = new Random();
        int n = 10, repeticiones = 10;
        double p = 0.5;

        for (int k = 0; k < repeticiones; k++) {
            int exitos = 0;
            for (int i = 0; i < n; i++) {
                if (rand.nextDouble() < p) exitos++;
            }
            System.out.println("Muestra: " + exitos);
        }
    }
}
