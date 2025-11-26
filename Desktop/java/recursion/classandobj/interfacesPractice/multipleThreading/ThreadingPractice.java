package classandobj.interfacesPractice.multipleThreading;

public class ThreadingPractice  extends Thread{

    public void run(){
        int i=1;

        while(true){
            System.out.println("hello");
            i++;
        }
    }
  
}

 class  Threadtest {

    public static void main(String[] args) {
        
        ThreadingPractice t = new ThreadingPractice();

        t.start();
        int i=0;
        while(true){
            System.out.println("world");
            i++;
        }
    }
}


