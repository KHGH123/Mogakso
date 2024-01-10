import java.util.function.*;

public class s2 {
    public static void main(String[] args) {
        String ss = "Hello";
        Predicate<String> isEmpty = s -> s.length() == 0;

        if(!isEmpty.test(ss))   System.out.println("Not Empty!");
    }
}


