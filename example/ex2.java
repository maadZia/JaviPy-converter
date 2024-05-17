//second parsetree code

public class ExampleClass {
    // Zmienne globalne
    private int variable1 = 10;
    private String variable2 = "Hello";

    // Funkcja 1
    public void printGlobalVariables() {
        System.out.println("wartosc zmiennej 1: " + variable1);
        System.out.println("wartosc zmiennej 2: " + variable2);
    }

    // metoda main
    public static void main(String[] args) {
        ExampleClass example = new ExampleClass();

        // wywołanie funkcji 
        example.printGlobalVariables();
    }
}
