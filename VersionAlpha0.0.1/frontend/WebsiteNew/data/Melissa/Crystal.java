package Assign_1A;


import Media.*;                  // for Turtle and TurtleDisplayer
import static java.lang.Math.*;  // for Math constants and functions
import static java.awt.Color.*;  // for Color constants
import static Media.Turtle.*;

/** This class ...
  *
  * @author Aldrin Maliakal
  * 
  * @version 1.0 03/02/2019                                                       */

public class Crystal {
  
    private TurtleDisplayer  display;  // display to draw on
    private Turtle           yertle;   // turtle to do drawing
    
    
    // instance variables
    
    
    /** This constructor ...                                                     */
    
    public Crystal ( ) {
        
          display = new TurtleDisplayer();
          yertle = new Turtle(FAST);
          display.placeTurtle(yertle);
        
          yertle.penDown();
          
          for(int j=1 ; j<=24 ; j++) {
            
           
            for ( int i=1 ; i<=12 ; i++ ) {
          
            yertle.forward(25);
            yertle.right(PI/6);
            
          };
            
            yertle.right(PI/12);
          };
          yertle.penUp();
          
          display.close();
          
        // statements
        
          }; // constructor
    
    
    public static void main ( String[] args ) { Crystal s = new Crystal(); };
    
    
} // Crsytal
