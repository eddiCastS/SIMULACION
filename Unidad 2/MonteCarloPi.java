import java.util.Random;
public class MonteCarloPi {
    public static void main(String[] args) {
        int n = 100000;
        int dentro = 0;
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            double x = rand.nextDouble();
            double y = rand.nextDouble();
            if (x*x + y*y <= 1) dentro++;
        }
        double pi_aprox = 4.0 * dentro / n;
        System.out.println("Estimación de π: " + pi_aprox);
    }
}
