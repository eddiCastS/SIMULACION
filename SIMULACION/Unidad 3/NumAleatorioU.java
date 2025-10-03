import java.util.Random;

public class NumAleatorioU {
    public static void main(String[] args) {
        Random rand = new Random();
        for (int i = 0; i < 5; i++) {
            System.out.println(rand.nextDouble());
        }
    }
}
