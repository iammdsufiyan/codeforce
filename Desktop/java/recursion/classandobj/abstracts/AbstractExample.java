package classandobj.abstracts;

abstract class Super {

    public Super() {
        System.out.println("constructor");
    }

    public void meth() {
        System.out.println("meth");
    }

    abstract public void meth1();
}

class sub extends Super {
    @Override
    public void meth1() {
        System.out.println("meth1 and sub");
    }
}

public class AbstractExample {

    public static void main(String[] args) {

        // Super s = new Super();
        // s.meth();

        Super s1 = new sub();
        s1.meth1();
    }

}
