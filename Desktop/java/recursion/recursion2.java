public class recursion2 {
    public static void main (String [] args){
       message(1);
       print(2);
      System.out.println(square_root(4)) ;
       System.out.println(square_root(5)) ;
    }

    static void message(int n) {
        System.out.println(n);
    }

    
static void print (int n){
    System.out.println(n);
}

static  boolean square_root (int n){
    for(int i=0;i<n;i++){
        if(i*i==n){
            return true;
        }
    }
    return false;
}
}

