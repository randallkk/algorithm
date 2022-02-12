import java.util.ArrayList;
import java.util.Scanner;

public class example {
    public example(){
        System.out.println("hello");
    }
        
    private static void inOut() {
        Scanner scan = new Scanner(System.in);
        String a = scan.next();	// white space를 기준으로 한 단어를 받아옴: String
        int b = scan.nextInt();	// int
        double c = scan.nextDouble();	// double
        String d = scan.nextLine();	// 개행문자("\n")를 기준으로 한 줄을 받아옴.
        String e = scan.nextLine();
        scan.close();
        
        System.out.println(d.equals("\n"));
        System.out.println(d.equals(""));
        System.out.println(a + b + c + d + e);
    }

    private static void isEqual(){
        String a = "Anna";
        String b = "Anna";
        String c = a;
        ArrayList<Object> d = new ArrayList<>();
        ArrayList<Object> e = new ArrayList<>();
        ArrayList<Object> f = d;

        System.out.println(System.identityHashCode(a));
        System.out.println(System.identityHashCode(b));
        System.out.println(System.identityHashCode(c));
        System.out.println(System.identityHashCode(d));
        System.out.println(System.identityHashCode(e));
        System.out.println(System.identityHashCode(f));
        
        if(a==b) System.out.println("a와 b는 같은 객체(Object)를 참조합니다.");
        if(b==c) System.out.println("b와 c는 같은 객체(Object)를 참조합니다.");
        if(c==a) System.out.println("c와 a는 같은 객체(Object)를 참조합니다.");
        if(d==e) System.out.println("d와 e는 같은 객체(Object)를 참조합니다.");
        if(e==f) System.out.println("e와 f는 같은 객체(Object)를 참조합니다.");
        if(f==d) System.out.println("f와 d는 같은 객체(Object)를 참조합니다.");
        if(a.equals(b)) System.out.println("a와 b는 같은 값(value)을 가집니다.");
        if(b.equals(c)) System.out.println("b와 c는 같은 값(value)을 가집니다.");
        if(c.equals(a)) System.out.println("c와 a는 같은 값(value)을 가집니다.");
        if(d.equals(e)) System.out.println("d와 e는 같은 값(value)을 가집니다.");
        if(e.equals(f)) System.out.println("e와 f는 같은 값(value)을 가집니다.");
        if(f.equals(d)) System.out.println("f와 d는 같은 값(value)을 가집니다.");
    }

    private static void initialize(){
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();
        int j = scan.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();

    }

    public static void main(String[] args) {
        initialize();
    }
}