public class recursionfirstex{
    public static void main(String [] args){

        rec(1);
     

    }

    static void  rec(int n){
        if(n==5){
               System.out.println(n);
        return;
       }
       System.out.println(n);
       rec(n+1);
       
    }
}

//javac recursionfirstex.java && java recursionfirstex

