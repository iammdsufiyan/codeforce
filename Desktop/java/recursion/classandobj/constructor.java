package classandobj;

public class constructor {
    private double radius;
    private double height;

    public double getradius(){
        return radius;
    }

    public double getheight(){
        return height;
    }

    public void setradius(){
       this.radius = radius;
    }

    public void setheight(){
       this. height = height;
    }

    public constructor(){
        radius = 1;
        height = 1;
    }
    public constructor(double radius, double height){
       this. radius = radius;
        this.height = height;
    }

        public double area(){
            return Math.PI*radius*radius*height;
        }

        public double perimeter(){
            return Math.PI*2*radius*height;
        }
    public static void main(String[] args){

        constructor cylinder = new constructor();

        System.out.println(cylinder.area());b
        System.out.println(cylinder.perimeter());
    }
}
