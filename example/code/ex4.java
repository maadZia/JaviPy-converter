// fourth parsetree code

public class Example {
    private static int privateVariable = 10;

    public static void main(String[] args) {
        int i = 0;

        while (i < 5) {
            if (i % 2 == 0) {
                System.out.println("Liczba parzysta: " + i);
            } else {
                System.out.println("Liczba nieparzysta: " + i);
            }
            i++;
        }

        try {
            int result = divide(10, 0);
            System.out.println("Wynik dzielenia: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Nie można dzielić przez zero!");
        }
    }

    private static int divide(int a, int b) {
        return a / b;
    }
}
