package classandobj.interfacesPractice;

 interface Test {

    void meth();
    void meth1();
}

public class My  implements Test {

   public void meth(){
        System.out.println("meth is printed");
    }

   public void meth1(){
        System.out.println("meth1 is printed ");
    }

    void meth3(){
        System.out.println("meth 3");
    }
    
}

 class interfacesPractice {
    public static void main(String[] args) {
        Test t = new My();
        t.meth();
        t.meth1();
    }
    
}
