package Exercise_Object;

import javax.crypto.spec.PSource;

class Calculator_3 {
    int value;

    Calculator_3() {
        this.value = 0;
    }

    void add(int val) {
        this.value += val;
    }

    int getValue() {
        return this.value;
    }
}
class IsoddCalculator extends Calculator_3{
    boolean isodd(int val){
        if (val%2 == 1){
            return true;
        } else{
           return false;
        }

    }

}

public class exerciseObject_3 {
    public static void main(String[] args) {

      IsoddCalculator isoddCalculator = new IsoddCalculator();
        System.out.println(isoddCalculator.isodd(17));
    }
}
