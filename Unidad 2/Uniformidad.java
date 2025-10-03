import java.util.Random;
public class Uniformidad {
    public static void main(String[] args) {
        Random rand = new Random();
        int[] histograma = new int[10];
        for (int i = 0; i < 1000; i++) histograma[(int)(rand.nextDouble()*10)]++;
        for (int i = 0; i < 10; i++) System.out.println("Rango " + i + ": " + histograma[i]);
    }
}
