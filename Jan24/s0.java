import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class s0 {
    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(1,2,3,4,5);
        Stream<Integer> intStream = list.stream(); 

        intStream.forEach(System.out::print); // 최종 연산, 닫힘
        // intStream.forEach(System.out::print); // 에러, 이미 닫힘
        
        String[] strArr = new String[]{"a","b","c"};
        Stream<String> strStream = Stream.of("a", "b", "c");
        Stream<String> strStream2 = Arrays.stream(strArr);
        strStream.forEach(System.out::println);

        int[] intArr = {1,2,3,4,5};
        IntStream intStream2 = Arrays.stream(intArr);
        //intStream2.forEach(System.out::println); // 최종연산
        System.out.println("sum="+intStream2.sum());

        Integer[] intArr2 = {1,2,3,4,5};
        Stream<Integer> intStream3 = Arrays.stream(intArr2);
        System.out.println("count="+intStream3.count()); // sum() 없음
    }
}
