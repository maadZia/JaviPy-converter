//third parsetree code

import java.util.Random;

enum Day {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
}


public class MyClass {
 
    private int myNumber;

    public MyClass(int number) {
        this.myNumber = number;
    }

    public void printNumber() {
        System.out.println("My number is: " + myNumber);
    }

    public static void main(String[] args) {
        MyClass myObject = new MyClass(42);
        myObject.printNumber();
        Day today = Day.MONDAY;
        System.out.println("Today is: " + today);
    }
}
