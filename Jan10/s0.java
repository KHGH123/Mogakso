import java.util.*;

public class s0 {
    public static void main(String[] args) {
        MyFunction f1 = new MyFunction() {
            public int max(int a, int b) {
                return a>b ? a : b;
            }
        };
        MyFunction f2 = (a, b) -> a>b ? a : b;
        List<String> list = Arrays.asList("abc", "aaa", "bbb");
        Collections.sort(list, (s1, s2)->s1.compareTo(s2));

        System.out.println(f1.max(3, 5) + " " + f2.max(3, 5));
        System.out.println(list);
    }   
    
    @FunctionalInterface
    interface MyFunction {
        public abstract int max(int a, int b);
    }
}
