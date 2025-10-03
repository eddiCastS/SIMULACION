import java.util.Random;

public class Inversa {
    public static void main(String[] args) {
        Random rand = new Random();
        int n = 20;
        for (int i = 0; i < n; i++) {
            double u = rand.nextDouble();
            double x = -Math.log(1 - u); // Exponencial(1)
            System.out.println(x);
        }
    }
}
