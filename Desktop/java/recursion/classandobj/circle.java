package classandobj;
import java.util.Scanner;
public class circle {
      

        public double radius;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        double num = sc.nextDouble();
       
        circle myCircle = new circle();
       myCircle.radius = num;

       double circlePerimeter = myCircle.perimeter(num);
       System.out.println(circlePerimeter);
       sc.close();

    }

    public  double perimeter(double radius){
        

        return 2 *3.14 * radius; 
    }
}


// package classandobj;
// import java.util.Scanner;
// public class circle {
//     public double radius;

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter the radius of the circle: ");
//         double radiusInput = sc.nextDouble();

//         circle myCircle = new circle();
//         myCircle.radius = radiusInput;

//         double circlePerimeter = myCircle.perimeter();
//         System.out.println("The perimeter of the circle is: " + circlePerimeter);
//         sc.close();
//     }

//     public double perimeter() {
//         return 2 * 3.14 * this.radius;
//     }
// }
