//third parsetree code

public class Fibonacci {
    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        } else {
            int a = fibonacci(n - 1);
            int b = fibonacci(n - 2);
            return a+b;
        }
    }

    public static void main(String[] args) {
        int n = 10;
        int f = fibonacci(n);
        System.out.println("dla n = " + n);
        System.out.println("liczba Fibonacciego to: " + f);
    }
}
