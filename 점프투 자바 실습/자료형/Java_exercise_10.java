import java.util.HashMap;

public class Java_exercise_10 { //
    enum coffeeMenu {
        AMERRICANO,
        ICEAMERICANO,
        CAFELATTTE
    };
   static void printCoffeePrice(coffeeMenu type) {
        HashMap<coffeeMenu, Integer> priceMap = new HashMap<>();
        priceMap.put(coffeeMenu.AMERRICANO, 3000);  // 1: 아메리카노
        priceMap.put(coffeeMenu.ICEAMERICANO, 4000);  // 2: 아이스 아메리카노
        priceMap.put(coffeeMenu.CAFELATTTE, 5000);  // 3: 카페라떼
        int price = priceMap.get(type);
        System.out.printf("가격은 %d원 입니다.", price);
    }

    public static void main(String[] args) {
        printCoffeePrice(coffeeMenu.AMERRICANO);
    }
}

