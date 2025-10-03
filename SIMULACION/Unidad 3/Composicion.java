import java.util.Random;

public class Composicion {
    public static void main(String[] args) {
        Random rand = new Random();
        int n = 11;
        for (int i = 0; i < n; i++) {
            if (rand.nextDouble() < 0.5) {
                // Normal(0,1) con Box-Muller
                double u1 = rand.nextDouble();
                double u2 = rand.nextDouble();
                double z = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
                System.out.println("Normal: " + z);
            } else {
                // Exponencial(1)
                double u = rand.nextDouble();
                double exp = -Math.log(1 - u);
                System.out.println("Exponencial: " + exp);
            }
        }
    }
}
