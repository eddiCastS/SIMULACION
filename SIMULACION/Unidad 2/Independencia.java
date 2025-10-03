import java.util.Random;
public class Independencia {
    public static void main(String[] args) {
        Random rand = new Random();
        double[] numeros = new double[100];
        for (int i = 0; i < 100; i++) numeros[i] = rand.nextDouble();
        double sumProd = 0, sum1 = 0, sum2 = 0;
        for (int i = 0; i < numeros.length - 1; i++) {
            sumProd += numeros[i] * numeros[i+1];
            sum1 += numeros[i];
            sum2 += numeros[i+1];
        }
        double corr = (sumProd - (sum1*sum2/(numeros.length-1))) / (numeros.length-1);
        System.out.println("Autocorrelación aproximada: " + corr);
    }
}
