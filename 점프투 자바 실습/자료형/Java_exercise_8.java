import java.util.HashMap;

public class Java_exercise_8 {
    public static void main(String[] args) {
        HashMap<String, Integer> grade = new HashMap<>();
        grade.put("A", 90);
        grade.put("B", 80);
        grade.put("C", 70);

        System.out.println(grade.remove("B"));
        System.out.println(grade.keySet()); // B 를 grade 맵에서 삭제 하였는지 확인
        System.out.println(grade);

    }
}
