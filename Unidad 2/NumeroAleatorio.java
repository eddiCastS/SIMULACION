import java.util.Random;


public class NumeroAleatorio {

    public static void main(String[] args) {
        Random random = new Random();
        int numero = random.nextInt(1000);

        System.out.println("numero aleatoriamente generado:" + numero);
    }
}