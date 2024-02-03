import java.util.*;
import java.util.stream.*;

public class s0 {
    public static void main(String[] args) {
        Stream<Student> studentStream = Stream.of(
            new Student("a", 3, 300),
            new Student("b", 1, 200),
            new Student("c", 2, 100),
            new Student("d", 2, 150),
            new Student("e", 1, 200),
            new Student("f", 3, 290),
            new Student("g", 3, 180)
        );

        studentStream.sorted(Comparator.comparing(Student::getBan)
        .thenComparing(Comparator.naturalOrder()).reversed())
        .forEach(System.out::println);
    }
}

class Student implements Comparable<Student> {
    String name;
    int ban;
    int totalScore;

    public String getName() {
        return this.name;
    }

    public int getBan() {
        return this.ban;
    }

    public int getTotalScore() {
        return this.totalScore;
    }

    Student(String name, int ban, int totalScore) {
        this.name = name;
        this.ban = ban;
        this.totalScore = totalScore;
    }

    @Override
    public String toString() {
        return name+" : "+ban+" : "+totalScore;
    }
    
    @Override
    public int compareTo(Student s) {
        return s.totalScore - this.totalScore;
    }
}
