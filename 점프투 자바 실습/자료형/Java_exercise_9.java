import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;


public class Java_exercise_9 {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5));
        System.out.println(numbers);  // [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5] 출력
        // 중복 허용 안되는 set 사용
        HashSet<Integer> hashMap = new HashSet<>(numbers);
        ArrayList<Integer> arrayList = new ArrayList<>(hashMap);
        System.out.println(arrayList);

    }
}
