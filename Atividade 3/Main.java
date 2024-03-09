import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double e = Math.E;
                double x0 = 0;
        double x1 = 0.5;
        double x2 = 1;
                double y0 = Math.exp(2 * x0);
        double y1 = Math.exp(2 * x1);
        double y2 = Math.exp(2 * x2);
                double a = y0;
        double b = (y1 - y0) / (x1 - x0);
        double c = ((y2 - y0) / (x2 - x0) - b) / (x2 - x1);
        
        System.out.printf("P(x) = %.4f + %.4fx + %.4fx^2\n", a, b, c);  }
}
