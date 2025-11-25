public class recursion1{

public static void main (String [] args){
System.out.println("hello world");

message();

}

static void message (){
    System.out.println("1");
    message1();
}

static void message1(){
    System.out.println("2");
    message3();
}

static void message3(){
    System.out.println("3");
    message4();
}
static void message4(){
    System.out.println("4");
    message5();
}
static void message5(){
    System.out.println("5");
}
}