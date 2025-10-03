import java.util.Random;

public class ChiCuadrada {
    public static void main(String[] args) {
        Random rand = new Random();
        int n = 100;
        int k = 10;
        int[] conteos = new int[k];

        for (int i = 0; i < n; i++) {
            double u = rand.nextDouble();
            int intervalo = (int)(u * k);
            conteos[intervalo]++;
        }

        double esperado = n / (double)k;
        double chi2 = 0;
        for (int c : conteos) {
            chi2 += Math.pow(c - esperado, 2) / esperado;
        }

        System.out.println("Chi-cuadrada aproximada: " + chi2);
    }
}
