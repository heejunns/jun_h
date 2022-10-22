package Exercise_control;

public class ExerciseControl_5 {
    public static void main(String[] args) {
        int[] marks = {70,60,55,75,95,90,80,80,85,100};
        int total = 0;
        for (int mark: marks){
            total+=mark;
       }
        System.out.printf("A 학급의 평균 점수는 %d 입니다.",total/marks.length);
    }

}
