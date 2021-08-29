
/**
 * Write a description of class Main here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Main {
  // main function
    public static void main(String[] args) {
    
        //System.out.println("Hello World");
        Student ahmed = new Student("Ahmed", 30);
        ahmed.printName();
        NewStudent(ahmed);
  }
  
  public static Student NewStudent(Student s){
      return s;
    }
}