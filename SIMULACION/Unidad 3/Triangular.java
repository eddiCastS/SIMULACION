import java.util.Random;

public class Triangular {
    public static void main(String[] args) {
        Random rand = new Random();
        int n = 5;
        double a = 0, b = 10, c = 5;

        for (int i = 0; i < n; i++) {
            double u = rand.nextDouble();
            double f = (c - a) / (b - a);
            double x;
            if (u < f) {
                x = a + Math.sqrt(u * (b - a) * (c - a));
            } else {
                x = b - Math.sqrt((1 - u) * (b - a) * (b - c));
            }
            System.out.println(x);
        }
    }
}
