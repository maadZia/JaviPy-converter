//second parsetree code

public class ExampleClass {
    private int variable1 = 10;
    private String variable2 = "Hello";

    public void printGlobalVariables() {
        int a = 5;
        System.out.println("wartosc zmiennej 1: " + variable1);
        System.out.println("wartosc zmiennej 2: " + variable2);
        System.out.println("wartosc zmiennej a: " + a);
    }

    public static void main(String[] args) {
        ExampleClass example = new ExampleClass();
        example.printGlobalVariables();
    }
}
