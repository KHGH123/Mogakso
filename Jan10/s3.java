import java.util.function.*;
import java.util.*;
import java.util.Collections.*;

public class s3 {
    public static void main(String[] args) {
        Supplier<Integer> s = () -> (int)(Math.random()*100)+1;
        Consumer<Integer> c = i -> System.out.print(i+" ");
        Predicate<Integer> p = i -> i%2 == 0;
        Function<Integer, Integer> f = i -> i/10*10;

        List<Integer> list = new ArrayList<>();
        makeRandomList(s, list);
        System.out.println(list);
        printEvenNum(p, c, list);
        List<Integer> newList = doSomething(f, list);
        System.out.println(newList);
        List<Integer> sortedList = sortList(list);
        System.out.println(sortedList);
    }

    static <T>void makeRandomList(Supplier<T> s, List<T> list) {
        for(int i=0; i<10; i++)
            list.add(s.get());
    }

    static <T>void printEvenNum(Predicate<T> p, Consumer<T> c, List<T> list) {
        System.out.print("[");
        for(T i : list) {
            if(p.test(i))
                c.accept(i);
        }
        System.out.println("]");
    }
    
    static <T>List<T> doSomething(Function<T, T>f, List<T> list) {
        List<T> newList = new ArrayList<>();
        for (T i : list)
        {
            newList.add(f.apply(i));
        }
        return newList;
    }

    static <T extends Comparable<T>>List<T> sortList(List<T> list) {
        Collections.sort(list);
        return list;
    }
}
