package Exercise_control;

public class ExerciseControl_2 {
    public static void main(String[] args) {
        int total = 0;
        int i = 0;
        while (i <=1000) {
            if (i%3 ==0){
                total+=i;
            }
            i++;
        }
        System.out.printf("0부터 1000까지의 3의 배수의 합은 %d 입니다.",total);
    }

}
