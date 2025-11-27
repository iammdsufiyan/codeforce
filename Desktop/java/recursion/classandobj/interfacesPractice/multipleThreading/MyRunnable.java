package classandobj.interfacesPractice.multipleThreading;

public class MyRunnable  implements Runnable{
    
    public void run(){
        int i=0;
        while (true) {
            System.out.println("hellow");
            i++;
        }
    }
}

 class  runn {

    public static void main(String[] args) {
        
            MyRunnable r = new MyRunnable();
            Thread t = new Thread(r);
            t.start();

            int i=0;
             while (true) {
            System.out.println("world");
            i++;
        }
            
    }
}
