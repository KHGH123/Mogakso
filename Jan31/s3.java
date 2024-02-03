import java.util.*;
import java.util.stream.*;

public class s3 {
    public static void main(String[] args) {
        Optional<String> optStr = Optional.of("abcde");
        Optional<Integer> optInt = optStr.map(String::length);
        System.out.println("optStr = "+optStr.orElse(""));
        System.out.println("optInt = "+optInt.get());

        int result1 = Optional.of("123")
            .filter(x->x.length() > 0)
            .map(Integer::parseInt).get();

        int result2 = Optional.of("")
            .filter(x->x.length() > 0)
            .map(Integer::parseInt).orElse(-1);

        System.out.println("result1 = "+result1);
        System.out.println("result2 = "+result2);

        Optional.of("456").map(Integer::parseInt).ifPresent(x->System.out.printf("result3 = %d\n",x));

        OptionalInt optInt1 = OptionalInt.of(0);
        OptionalInt optInt2 = OptionalInt.empty();

        System.out.println(optInt1.isPresent());
        System.out.println(optInt2.isPresent());

        System.out.println(optInt1.getAsInt());
        // System.out.println(optInt2.getAsInt()); // NoSuchElementException
        
        System.out.println(optInt1);
        System.out.println(optInt2);

        Optional<String> opt1 = Optional.ofNullable(null);
        Optional<String> opt2 = Optional.empty();
        
        System.out.println("opt1="+opt1);
        System.out.println("opt2="+opt2);

        int result3 = optStrToInt(Optional.of("123"), 0);
        int result4 = optStrToInt(Optional.of(""), 0);

        System.out.println("result3="+result3);
        System.out.println("result4="+result4);
    }
    static int optStrToInt(Optional<String> optStr, int defaultValue) {
        try {
            return optStr.map(Integer::parseInt).get();
        } catch (Exception e) {
            return defaultValue;
        }
    }
}
