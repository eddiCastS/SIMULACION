import java.util.Random;

public class DistribucionNormal {
    public static void main(String[] args) {
        Random rand = new Random();
        for (int i = 0; i < 10; i++) {
            double u1 = rand.nextDouble();
            double u2 = rand.nextDouble();
            double z = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2); 
            System.out.println(z); // Normal(0,1)
        }
    }
}
