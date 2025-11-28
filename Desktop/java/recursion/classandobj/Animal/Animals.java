package classandobj.Animal;

public class Animals {

     void sound(){
        System.out.println("sound of animal");
     }

    
    
}

class  Dog extends Animals{

    
        @Override
            void sound(){
            System.out.println("dog barks ");
        }
    

}

 class puppy extends Dog{
        @Override

        void sound(){
            System.out.println("puppy yelps");
        }
 }


 class inheritances {
    public static void main(String[] args) {
        puppy p =new puppy();

        p.sound();
    }
 }

// class Animal {
//     Animal() {
//         System.out.println("Animal constructor called");
//     }

//     void sound() {
//         System.out.println("Animal makes a sound");
//     }
// }

// class Dog extends Animal {
//     Dog() {
//         super(); // calling parent constructor
//         System.out.println("Dog constructor called");
//     }

//     @Override
//     void sound() {
//         System.out.println("Dog barks");
//     }
// }