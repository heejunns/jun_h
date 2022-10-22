package Exercise_Object;
class Calculator {
    int value;

    Calculator() {
        this.value = 0;
    }

    void add(int val) {
        this.value += val;
    }

    int getValue() {
        return this.value;
    }
}
class UpradeCalculator extends Calculator{
    void minus(int val){
        this.value -= val;
    }
}

public class exerciseObject_1 {
    public static void main(String[] args) {
        UpradeCalculator upradeCalculator = new UpradeCalculator();
        upradeCalculator.add(10);
        upradeCalculator.minus(3);
        System.out.println(upradeCalculator.getValue());
    }
}
