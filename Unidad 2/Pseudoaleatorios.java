import java.util.Random;
public class Pseudoaleatorios {
    public static void main(String[] args) {
        Random rand = new Random(123);
        for (int i = 0; i < 10; i++) System.out.println(rand.nextDouble());
    }
}
