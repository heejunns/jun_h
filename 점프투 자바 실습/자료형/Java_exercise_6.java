import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Iterator;

public class Java_exercise_6 {
    public static void main(String[] args) {
        ArrayList<Integer> arrayList = new ArrayList<>(Arrays.asList(1,3,5,4,2));
        System.out.println(arrayList); // 기존 그대로 출력
        arrayList.sort(Comparator.reverseOrder());
        System.out.println(arrayList);
    }
}
