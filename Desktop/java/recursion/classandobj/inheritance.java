package classandobj;

class Circle {
    
    public double radius;

    public double area(){
            return Math.PI*radius*radius;
    }

    public double perimeter(){
        return Math.PI*2*radius;
    }
}

    class cylinder  extends Circle{

        public double heights;


        public double volume(){
            return area()*heights;
        }


}

public class inheritance {
    public static void main(String[] args){
        Circle cir = new Circle();

        cylinder clyndr = new cylinder();

       
           clyndr.radius = 7;
            clyndr.heights = 10;
     

        System.out.println(clyndr.volume());
        System.out.println(clyndr.area());
    }
}

