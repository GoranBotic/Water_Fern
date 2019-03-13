package Assign_1_B; 
 
 
import Media.*;                  // for Turtle and TurtleDisplayer 
import static Media.Turtle.*;    // for Turtle speeds 
import static java.lang.Math.*;  // for Math constants and functions 
import static java.awt.Color.*;  // for Color constants 
 
 
/** This class ... 
  * 
  * @author Adam Pascal 
  *  
  * @version 1.0 (January 25)                                                        */ 
 
public class Crystal { 
     
     
    private TurtleDisplayer   display;
    private Turtle            yertle;
    
      
     
    /** This constructor draws a crystal                                                    */ 
     
    public Crystal ( ) { 
         
        display = new TurtleDisplayer();
        yertle = new Turtle(FAST);
        display.placeTurtle(yertle);
       
        for ( int j=1 ; j<=24 ; j++) {
        for ( int i=1 ; i<=12 ; i++ ) {
        yertle.penDown();
        yertle.forward(25);
        yertle.right(PI/6);
        }
        yertle.right(PI/12);
    }
        
        display.close();
        
    }; // constructor 
     
     
     public static void main ( String[] args ) { Crystal s = new Crystal(); }; 
     
     
} // Crystal 
