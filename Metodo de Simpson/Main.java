import java.util.function.Function;

public class Main {

    public static double f(double x) {
        return 1.0 / (1.0 + x);
    }

    public static double s(double a, double b, int n) {
            if (n % 2 !=0) {
                throw new IllegalArgumentException("par");
            }
        double h = (b - a) / n;
        double sum1 = 0.0;
        double sum2 = 0.0;

        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            if (i % 2 == 0) {
                sum2 += f(x);
            } else {
                sum1 += f(x);
            }
        }

        return (h / 3.0) * (f(a) + f(b) + 4.0 * sum1 + 2.0 * sum2);
    }

    public static void main(String[] args) {
        double a = 0.6;
        double b = 0.0;
        int n = 1000;

        try {
            double i = s(a, b, n);
            System.out.println("valor da integral " + i);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}
