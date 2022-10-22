package Exercise_Object;
class Calculator_2 {
    int value;

    Calculator_2() {
        this.value = 0;
    }

    void add(int val) {
        this.value += val;
    }

    int getValue() {
        return this.value;
    }
}
class MaxLimitCalculator extends Calculator_2{
   @Override
    void add(int val){
       if (value+val > 100){
           this.value = 100;
       } else{
           this.value+=val;
       }
   }
}

public class exerciseObject_2 {
    public static void main(String[] args) {
        MaxLimitCalculator maxLimitCalculator = new MaxLimitCalculator();
        maxLimitCalculator.add(50);
        maxLimitCalculator.add(35);
        System.out.println(maxLimitCalculator.getValue());
    }
}
