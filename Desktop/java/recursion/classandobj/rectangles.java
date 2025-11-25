package classandobj;

public class rectangles{
    public double l;
    public double b;
    public double area(){
        return l*b;
    }

    public double perimeter(){
        return 2*(l+b);
    }
}

 class rectangle1 {
   
    public static void main(String[] args){

        rectangles r1 = new rectangles();

        r1.l = 10;
        r1.b = 20;

        System.out.println(r1.area());
        System.out.println(r1.perimeter());
    }
    
}
