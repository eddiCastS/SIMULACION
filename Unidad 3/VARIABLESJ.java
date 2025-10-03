import java.util.Arrays;
import java.util.Random;

public class VARIABLESJ {
    public static void main(String[] args) {
        Random rand = new Random();

        
        int[] discreta = new int[10];
        for(int i=0; i<10; i++){
            int exito = 0;
            for(int j=0; j<10; j++){
                if(rand.nextDouble() < 0.5) exito++;
            }
            discreta[i] = exito;
        }
        System.out.println("Variable discreta (Binomial): " + Arrays.toString(discreta));

        
        double lambda = 1.5;
        double[] continua = new double[10];
        for(int i=0; i<10; i++){
            double U = rand.nextDouble();
            continua[i] = -Math.log(U)/lambda;
        }
        System.out.println("Variable continua (Exponencial): " + Arrays.toString(continua));

        
        int max = Arrays.stream(discreta).max().getAsInt();
        int[] frecuencia = new int[max+1];
        for(int val : discreta){
            frecuencia[val]++;
        }
        System.out.println("Frecuencia de valores discretos: " + Arrays.toString(frecuencia));
    }
}
