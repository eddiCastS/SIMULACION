import java.util.Random;

public class Convolucion {
    public static void main(String[] args) {
        Random rand = new Random();
        int lambda = 4;
        int muestras = 32;

        for (int j = 0; j < muestras; j++) {
            double L = Math.exp(-lambda);
            int k = 0;
            double p = 1.0;
            while (p > L) {
                k++;
                p *= rand.nextDouble();
            }
            System.out.println(k - 1);
        }
    }
}
