public class Main { public static void main(String[] args) {
double[][] x = {{5, 1, 1}, {3, 4, 1}, {3, 3, 6}};
double[] r = {5, 6, 0};
int n = r.length;

for (int i = 0; i < n - 1; i++) {
    int p = i;
    for (int j = i + 1; j < n; j++) {
        if (Math.abs(x[j][i]) > Math.abs(x[p][i])) {
            p = j;
        }
    }

    if (p != i) {
        double[] temp = x[i];
        x[i] = x[p];
        x[p] = temp;

        double tempResult = r[i];
        r[i] = r[p];
        r[p] = tempResult;
    }

    for (int k = i + 1; k < n; k++) {
        double fator = x[k][i] / x[i][i];
        r[k] -= fator * r[i];
        for (int j = i; j < n; j++) {
            x[k][j] -= fator * x[i][j];
        }
    }
}

double[] s = new double[n];
for (int i = n - 1; i >= 0; i--) {
    double a = 0;
    for (int j = i + 1; j < n; j++) {
        a += x[i][j] * s[j];
    }
    s[i] = (r[i] - a) / x[i][i];
}

System.out.println("x1 = " + s[0]);
        System.out.println("x2 = " + s[1]);
     System.out.println("x3 = " + s[2]);
    }
}
