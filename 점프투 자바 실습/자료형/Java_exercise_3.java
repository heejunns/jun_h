public class Java_exercise_3 {
    public static void main(String[] args) {
        String secretnum = "881120-1068234";
        System.out.printf("홍길동씨의 연월일은:%s 입니다.\n",secretnum.substring(0,6));
        System.out.printf("홍길동씨의 주민등록번호 뒷자리는:%s 입니다.",secretnum.substring(7));

    }
}
