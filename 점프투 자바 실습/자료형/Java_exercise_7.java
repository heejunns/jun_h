import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class Java_exercise_7 {
    public static void main(String[] args) {
        ArrayList<String> myList = new ArrayList<>(Arrays.asList("Life", "is", "too", "short"));
        System.out.println(myList); // [Life, is, too, short] 출력
        String str = String.join(" ",myList);
        System.out.println(str);

    }
}
