// function courses() {
//   return JSON.parse($.ajax({
//     type: "POST",
//     url: "/api/v1/getClassList",
//     // data: {
//     //     'assignmentID': 0
//     // },
//     async:false
//   }).responseText);
//   // return [
//   //     [1,"cosc1p02"],
//   //     [2,"cosc1p03"],
//   //     [3,"cosc2p03"]
//   // ];
// }

// function offerings(course){
//   return JSON.parse($.ajax({
//     type: "POST",
//     url: "/api/v1/getOfferingList",
//     data: {
//         'classID': course
//     },
//     async:false
//   }).responseText);
// }

// function assignments(offering) {
//   return JSON.parse($.ajax({
//     type: "POST",
//     url: "/api/v1/getAssignmentList",
//     data: {
//         'offeringID': offering
//     },
//     async:false
//   }).responseText);
//     // return [1,2,3,4];
// }

// function submissions(assignment) {
//   return JSON.parse($.ajax({
//     type: "POST",
//     url: "/api/v1/getSubmissionsList",
//     data: {
//         'assignmentID': assignment
//     },
//     async:false
//   }).responseText);
//   // return [
//   //     [1,"Adam"],
//   //     [2,"Alice"],
//   //     [3,"Bob"],
//   //     [4,"Eve"]
//   // ];
// }

// function associations(sida, sidb){

//   console.log(sida)
//   console.log(sidb)
//   ass = JSON.parse($.ajax({
//     type: "POST",
//     url: "/api/v1/getAssociations",
//     data: {
//         'fID': sida
//     },
//     async:false
//   }).responseText);

//   new_ass = [];
//   //ass.document1 ass.document2 ind1.start_line ind1.end_line ind2.start_line ind2.end_line similarity 
//   //startlineA, endlineA, startlineB, endlineB, similarity

//   for(var i = 0; i < ass.length; i++) {
//     var row = ass[i];
//     if(row[0] == sidb) {
//       var newRow = [row[4], row[5], row[2], row[3], row[6]]
//       new_ass.push(newRow)
//     } else if(row[1] == sidb) {
//       var newRow = [row[2], row[3], row[4], row[5], row[6]]
//       new_ass.push(newRow)
//     }

//   }

//   // for(var spec_ass in ass){
//   //   if(ass[spec_ass][0] == sida && ass[spec_ass][1] == sidb){
//   //     new_ass.push([ass[spec_ass][2],ass[spec_ass][3],ass[spec_ass][4],ass[spec_ass][5],ass[spec_ass][6]]);
//   //   }else if(ass[spec_ass][1] == sida && ass[spec_ass][0] == sidb){
//   //     new_ass.push([ass[spec_ass][4],ass[spec_ass][5],ass[spec_ass][2],ass[spec_ass][3],ass[spec_ass][6]]);
//   //   }
//   // }

//   return new_ass;
//   // return [
//   //   [0,5,3,8,0.8],
//   //   [7,15,9,12,0.2],
//   //   [12,14,10,15,0.3]
//   // ]
// }

// function submission(sid) {
//   return JSON.parse($.ajax({
//     type: "POST",
//     url: "/api/v1/getSubmission",
//     data: {
//         'submissionID': sid
//     },
//     async:false
//   }).responseText);
    // return `static void
    // c_lex_one_token (c_parser *parser, c_token *token)
    // {
    //   timevar_push (TV_LEX);
    
    //   token->type = c_lex_with_flags (&token->value, &token->location,
    //                   &token->flags,
    //                   (parser->lex_untranslated_string
    //                    ? C_LEX_STRING_NO_TRANSLATE : 0));
    //   token->id_kind = C_ID_NONE;
    //   token->keyword = RID_MAX;
    //   token->pragma_kind = PRAGMA_NONE;
    
    //   switch (token->type)
    //     {
    //     case CPP_NAME:
    //       {
    //     tree decl;
    
    //     bool objc_force_identifier = parser->objc_need_raw_identifier;
    //     if (c_dialect_objc ())
    //       parser->objc_need_raw_identifier = false;
    
    //     if (C_IS_RESERVED_WORD (token->value))
    //       {
    //         enum rid rid_code = C_RID_CODE (token->value);
    
    //         if (rid_code == RID_CXX_COMPAT_WARN)
    //           {
    //         warning_at (token->location,
    //                 OPT_Wc___compat,
    //                 "identifier %qE conflicts with C++ keyword",
    //                 token->value);
    //           }
    //         else if (rid_code >= RID_FIRST_ADDR_SPACE
    //              && rid_code <= RID_LAST_ADDR_SPACE)
    //           {
    //         addr_space_t as;
    //         as = (addr_space_t) (rid_code - RID_FIRST_ADDR_SPACE);
    //         targetm.addr_space.diagnose_usage (as, token->location);
    //         token->id_kind = C_ID_ADDRSPACE;
    //         token->keyword = rid_code;
    //         break;
    //           }
    //         else if (c_dialect_objc () && OBJC_IS_PQ_KEYWORD (rid_code))
    //           {
    //         /* We found an Objective-C "pq" keyword (in, out,
    //            inout, bycopy, byref, oneway).  They need special
    //            care because the interpretation depends on the
    //            context.  */
    //         if (parser->objc_pq_context)
    //           {
    //             token->type = CPP_KEYWORD;
    //             token->keyword = rid_code;
    //             break;
    //           }
    //         else if (parser->objc_could_be_foreach_context
    //              && rid_code == RID_IN)
    //           {
    //             token->type = CPP_KEYWORD;
    //             token->keyword = rid_code;
    //             break;
    //           }
    //           }
    //         else if (c_dialect_objc () && OBJC_IS_PATTR_KEYWORD (rid_code))
    //           {
    //         /* We found an Objective-C "property attribute"
    //            keyword (getter, setter, readonly, etc). These are
    //            only valid in the property context.  */
    //         if (parser->objc_property_attr_context)
    //           {
    //             token->type = CPP_KEYWORD;
    //             token->keyword = rid_code;
    //             break;
    //           }
    //         /* Else they are not special keywords.
    //         */
    //           }
    //         else if (c_dialect_objc () 
    //              && (OBJC_IS_AT_KEYWORD (rid_code)
    //              || OBJC_IS_CXX_KEYWORD (rid_code)))
    //           {
    //         ;
    //           }
    //         else
    //           {
    //         token->type = CPP_KEYWORD;
    //         token->keyword = rid_code;
    //         break;
    //           }
    //       }
    
    //     decl = lookup_name (token->value);
    //     if (decl)
    //       {
    //         if (TREE_CODE (decl) == TYPE_DECL)
    //           {
    //         token->id_kind = C_ID_TYPENAME;
    //         break;
    //           }
    //       }
    //     else if (c_dialect_objc ())
    //       {
    //         tree objc_interface_decl = objc_is_class_name (token->value);
    //         if (objc_interface_decl
    //                 && (!objc_force_identifier || global_bindings_p ()))
    //           {
    //         token->value = objc_interface_decl;
    //         token->id_kind = C_ID_CLASSNAME;
    //         break;
    //           }
    //       }
    //         token->id_kind = C_ID_ID;
    //       }
    //       break;
    //     case CPP_AT_NAME:
    //       /* This only happens in Objective-C; it must be a keyword.  */
    //       token->type = CPP_KEYWORD;
    //       switch (C_RID_CODE (token->value))
    //     {
    //     case RID_CLASS:     token->keyword = RID_AT_CLASS; break;
    //     case RID_PRIVATE:   token->keyword = RID_AT_PRIVATE; break;
    //     case RID_PROTECTED: token->keyword = RID_AT_PROTECTED; break;
    //     case RID_PUBLIC:    token->keyword = RID_AT_PUBLIC; break;
    //     case RID_THROW:     token->keyword = RID_AT_THROW; break;
    //     case RID_TRY:       token->keyword = RID_AT_TRY; break;
    //     case RID_CATCH:     token->keyword = RID_AT_CATCH; break;
    //     case RID_SYNCHRONIZED: token->keyword = RID_AT_SYNCHRONIZED; break;
    //     default:            token->keyword = C_RID_CODE (token->value);
    //     }
    //       break;
    //     case CPP_COLON:
    //     case CPP_COMMA:
    //     case CPP_CLOSE_PAREN:
    //     case CPP_SEMICOLON:
    //       /* These tokens may affect the interpretation of any identifiers
    //      following, if doing Objective-C.  */
    //       if (c_dialect_objc ())
    //     parser->objc_need_raw_identifier = false;
    //       break;
    //     case CPP_PRAGMA:
    //       /* We smuggled the cpp_token->u.pragma value in an INTEGER_CST.  */
    //       token->pragma_kind = (enum pragma_kind) TREE_INT_CST_LOW (token->value);
    //       token->value = NULL;
    //       break;
    //     default:
    //       break;
    //     }
    //   timevar_pop (TV_LEX);
    // }`
// }


function dummyData() {
  return [
    {
      "name": "T",
      "files": [
        {
          "file": "Main.java",
          "data": [
            " package Assign5A;",
            "",
            " import Media.*;",
            " import java.awt.*;",
            " import static java.lang.Math.*;",
            " import static java.awt.Color.*;",
            "",
            " /*",
            " * March 15, 2019",
            "",
            " * */",
            "",
            " public class Edge {",
            "",
            "   private static final double TOLERANCE = 10.0;",
            "   private PictureDisplayer display;",
            "   private Picture apic;",
            "",
            "   public Edge() {",
            "",
            "     display = new PictureDisplayer();",
            "",
            "     apic = new Picture();",
            "     display.placePicture(apic);",
            "     display.waitForUser();",
            "     detect(apic);",
            "     display.close();",
            "",
            "   }",
            "",
            "   private void detect(Picture aPic) {",
            "",
            "     Pixel p1, p2;",
            "     Color c1, c2;",
            "",
            "     double intense1, intense2, diff;",
            "",
            "     for (int i = 0; i < aPic.getHeight() - 1; i++) {",
            "       for (int j = 0; j < aPic.getWidth() - 1; j++) {",
            "         if (i != aPic.getHeight() - 1) {",
            "",
            "           p1 = aPic.getPixel(j, i);",
            "           p2 = aPic.getPixel(j, i + 1);",
            "           c1 = p1.getColor();",
            "           c2 = p2.getColor();",
            "           intense1 = intensity(c1);",
            "           intense2 = intensity(c2);",
            "           diff = abs(intense1 - intense2);",
            "",
            "         }",
            "",
            "         else {",
            "           p1 = aPic.getPixel(j, i);",
            "           diff = 0;",
            "",
            "         }",
            "         if (diff < TOLERANCE) {",
            "           p1.setColor(WHITE);",
            "",
            "         }",
            "",
            "         else {",
            "",
            "           p1.setColor(BLACK);",
            "         }",
            "",
            "       }",
            "",
            "     }",
            "",
            "   }",
            "",
            "   private double intensity(Color c) {",
            "",
            "     double avg;",
            "     int r;",
            "     int g;",
            "     int b;",
            "     r = c.getRed();",
            "     b = c.getBlue();",
            "     g = c.getGreen();",
            "     avg = (r + g + b) / 3;",
            "",
            "     return avg;",
            "",
            "   }",
            "",
            "   public static void main(String args[]) {",
            "     Edge s = new Edge();",
            "   }",
            "",
            " }"
          ]
        },
        {
          "file": "OtherClass.java",
          "data": [
              " package Assign5B;",
              "",
              "",
              "",
              "  import Media.*;                  // for Picture and Sound etc.",
              " import java.awt.*;               // for Color objects and methods",
              " import static java.lang.Math.*;  // for math constants and functions",
              " import static java.awt.Color.*;  // for Color constants",
              "",
              "",
              "",
              "",
              "",
              " /** COSC 1P02",
              "",
              "   * @version 1.0 (March 15, 2019)*/",
              "",
              "",
              "",
              " public class NoiseReduction {",
              "",
              "",
              "",
              "   private SoundPlayer player;",
              "   private Sound bad;",
              "   private Sound good;",
              "",
              "",
              "",
              "   // instance variables",
              "",
              " public NoiseReduction ( ) {",
              "",
              "",
              "",
              "     player = new SoundPlayer();",
              "     bad = new Sound();",
              "",
              "     player.placeSound(bad);",
              "     player.waitForUser();",
              "     player.close();",
              "",
              "   }; // constructor",
              " private Sound clean (Sound original, int factor) {",
              "",
              "     Sound  result;",
              "     double total;",
              "     int s1 = 0;",
              "     int s2 =0;",
              "     int    numSamp;",
              "     int    amp;",
              "     int    newAmp;",
              "",
              "",
              "     numSamp = original.getNumSamples();",
              "",
              "     result = new Sound(numSamp, original);",
              "",
              "     for (int i=factor;i <numSamp-factor; i++) {",
              "",
              "       original.getSample(i);",
              "",
              "",
              "       for (int j=0; j<(2-factor+4) ; j++) {",
              "         original.getSample(j);",
              "",
              "         s2 = s2 + original.getSample(j).getAmp();",
              "",
              "         total = (double)(s2/5);",
              "",
              "    original.getSample(i).setAmp((int)total);",
              "",
              "",
              "",
              "       }",
              "",
              "",
              "",
              "",
              "     }",
              "     return result;",
              "   }",
              " public static void main ( String[] args ) { NoiseReduction s = new NoiseReduction(); };",
              " }"
          ]
        }
      ]
    },
    {
      "name": "Melissa",
      "files": [
        {
          "file": "Main.java",
          "data": [
              " package Assign_5_A;",
              "",
              " import Media.*;",
              " import java.awt.*;",
              " import static java.lang.Math.*;",
              " import static java.awt.Color.*;",
              "",
              " /* COSC 1P02",
              "  * March 15, 2019",
              "  * */",
              "",
              " public class Edge {",
              "",
              "",
              "   private static final double TOLERANCE = 10.0;",
              "   private PictureDisplayer display;",
              "   private Picture pic;",
              "",
              "",
              "   public Edge() {",
              "",
              "     display = new PictureDisplayer();",
              "     pic = new Picture();",
              "     display.placePicture(pic);",
              "     display.waitForUser();",
              "     detect(pic);",
              "     display.close();",
              "",
              "   }",
              "",
              "",
              "   private void detect(Picture aPic ) {",
              "",
              "     Pixel p1, p2;",
              "     Color c1, c2;",
              "     double intense1, intense2, diff;",
              "",
              "",
              "     for(int i = 0; i< aPic.getHeight()-1 ; i++){",
              "",
              "       for(int j = 0; j <aPic.getWidth()-1 ; j++){",
              "",
              "         if ( i != aPic.getHeight()-1 ){",
              "",
              "           p1 = aPic.getPixel(j,i);",
              "           p2 = aPic.getPixel(j,i+1);",
              "           c1 = p1.getColor();",
              "           c2 = p2.getColor();",
              "           intense1 = intensity(c1);",
              "           intense2 = intensity(c2);",
              "           diff = abs( intense1-intense2 );",
              "",
              "         }",
              "         else {",
              "",
              "           p1 = aPic.getPixel(j,i);",
              "",
              "           diff = 0;",
              "",
              "         }",
              "",
              "         if (diff<TOLERANCE){",
              "",
              "           p1.setColor(WHITE);",
              "",
              "         }",
              "         else{",
              "",
              "           p1.setColor(BLACK);",
              "",
              "         }",
              "",
              "       }",
              "",
              "     }",
              "",
              "   }",
              "",
              "   private double intensity ( Color c ) {",
              "",
              "     double avg;",
              "     int r;",
              "     int g;",
              "     int b;",
              "     r = c.getRed();",
              "     b = c.getBlue();",
              "     g = c.getGreen();",
              "     avg = (r + g + b)/3;",
              "",
              "     return avg;",
              "   }",
              "",
              "   public static void main(String args[]) { Edge s = new Edge(); }",
              " }"
          ]
        },
        {
          "file": "SomeClass.java",
          "data": [
            " package Assign_5_B;",
            "",
            "",
            " import Media.*;                  // for Picture and Sound etc.",
            " import java.awt.*;               // for Color objects and methods",
            " import static java.lang.Math.*;  // for math constants and functions",
            " import static java.awt.Color.*;  // for Color constants",
            "",
            "",
            " /** This class ...",
            "   *",
            "   * @author <your name>",
            "   * @version 1.0 (<date>)                                                        */",
            "",
            " public class NoiseReduction {",
            "",
            "   private SoundPlayer player;",
            "   private Sound messy;",
            "   private Sound cleaned;",
            "",
            "   // instance variables",
            "",
            "",
            "   /** This constructor ...                                                     */",
            "",
            "   public NoiseReduction ( ) {",
            "",
            "     player = new SoundPlayer();",
            "     messy = new Sound();",
            "     player.placeSound(messy);",
            "     player.waitForUser();",
            "",
            "     player.close();",
            "",
            "",
            "",
            "",
            "   }; // constructor",
            "",
            "",
            "   private Sound clean (Sound original, int factor) {",
            "",
            "     Sound  result;",
            "     double total;",
            "     int s1 = 0;",
            "     int s2 =0;",
            "     int    numSamp;",
            "     int    amp;",
            "     int    newAmp;",
            "",
            "",
            "",
            "     numSamp = original.getNumSamples();",
            "     result = new Sound(numSamp, original);",
            "",
            "",
            "     for (int i=factor;i <numSamp-factor; i++) {",
            "",
            "       original.getSample(i);",
            "",
            "",
            "",
            "       //  for (Sample oSamp: original) {",
            "",
            "       for (int j=0; j<(2-factor+4) ; j++) {",
            "",
            "         /* newSamp = original.next();",
            "          newSamp.getAmp(j);",
            "",
            "          amp = oSamp.getAmp();",
            "          newAmp = (int)((amp*(2-factor+4))/5)",
            "          newSamp = result.next();",
            "          newSamp.setAmp(newAmp); */",
            "",
            "         original.getSample(j);",
            "         s2 = s2 + original.getSample(j).getAmp();",
            "         total = (double)(s2/5);",
            "",
            "         original.getSample(i).setAmp((int)total);",
            "",
            "",
            "       }",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "     }",
            "",
            "",
            "",
            "     //}",
            "",
            "     return result;",
            "",
            "",
            "   }",
            "",
            "",
            " public static void main ( String[] args ) { NoiseReduction s = new NoiseReduction(); };",
            "",
            "",
            " } // NoiseReduction"
          ]
        }
      ]
    },
    {
      "name": "Patrick",
      "files": [
        {
          "file": "Census.java",
          "data": [
            "   package Assign_6;",
            "",
            "",
            "   import BasicIO.*;",
            "   import static BasicIO.Formats.*;",
            "   import static java.lang.Math.*;",
            "",
            "",
            "",
            "   public class Census {",
            "",
            "   private ASCIIDataFile      addData;",
            "   private BasicForm          household;",
            "   private BasicForm          person;",
            "   private ASCIIOutputFile    cendata;",
            "   String                     address;",
            "   int                        numPeople ;",
            "   int                        numMale;",
            "   int                        numFemale ;",
            "   int                        numE ;",
            "   int                        numF;",
            "   int                        numOther ;",
            "   int                        num;",
            "",
            "",
            "   public Census ( ) {",
            "",
            "     addData = new ASCIIDataFile();",
            "     household = new BasicForm(\"OK\",\"Skip\");",
            "     person = new BasicForm();",
            "     cendata = new ASCIIOutputFile();",
            "     buildHouseholdForm();",
            "     buildIndividualForm();",
            "     for( ; ;){",
            "       address = addData.readString();",
            "       if (addData.isEOF()  )  break;",
            "       processHousehold(address);",
            "     }",
            "",
            "     addData.close();",
            "     cendata.close();",
            "     household.close();",
            "     person.close();",
            "   };",
            "",
            "   private void processHousehold(String address){",
            "",
            "",
            "     int button;",
            "",
            "     fillHouseholdForm(address);",
            "     button = household.accept();",
            "     numPeople = household.readInt(\"numPeople\");",
            "     if( button == 0){",
            "       for (  int i = 1; i<=numPeople; i++){",
            "         person.clearAll();",
            "         num =i;",
            "         processPerson();",
            "       }",
            "",
            "       writeCensus( address, numPeople,  numMale,  numFemale,  numE,  numF,  numOther",
            "                  );",
            "",
            "     }",
            "   }",
            "",
            "   private void processPerson(){",
            "",
            "",
            "     String name;",
            "     int    sex;",
            "     int    lang;",
            "     int    age;",
            "",
            "     fillPersonForm(num);",
            "",
            "     person.accept();",
            "     name = person.readString(\"name\");",
            "     sex = person.readInt(\"sex\");",
            "     lang = person.readInt(\"lang\");",
            "     age = person.readInt(\"age\");",
            "",
            "     if ( sex == 0){",
            "       numMale = numMale+1;",
            "     }",
            "     else {",
            "       numFemale =numFemale+1;",
            "     }",
            "     lang = person.readInt(\"lang\");",
            "     if ( lang == 0){",
            "       numE= numE+1;",
            "     }",
            "     else {",
            "       if  (lang == 1){",
            "         numF = numF +1;",
            "       }",
            "       else {",
            "         numOther= numOther+1;",
            "       }    }",
            "   }//processPerson",
            "",
            "   private void buildHouseholdForm ( ) {",
            "     household.setTitle(\"Household\");",
            "     household.addTextField(\"addr\",\"Address\",20,10,10);",
            "       household.setEditable(\"addr\",false);",
            "     household.addTextField(\"numPeople\",\"# People\",2,10,50);",
            "   }",
            "",
            "   private void buildIndividualForm ( ) {",
            "     person.setTitle(\"Individual\");",
            "     person.addTextField(\"num\",\"Person\",2,10,10);",
            "     person.setEditable(\"num\",false);",
            "     person.addTextField(\"name\",\"Name\",20,10,50);",
            "     person.addTextField(\"age\",\"Age\",3,10,80);",
            "     person.addRadioButtons(\"sex\",\"Sex\",false,10,110,\"Male\",\"Female\");",
            "     person.addRadioButtons(\"lang\",\"Language\",false,10,160,",
            "                            \"English\",\"French\",\"Other\");",
            "   }",
            "",
            "   private void fillHouseholdForm( String address){",
            "     household.clearAll();",
            "     household.writeString(\"addr\", address);",
            "",
            "   }",
            "   private void fillPersonForm(int num){",
            "     person.clearAll();",
            "     person.writeInt(\"num\",num);",
            "",
            "   }",
            "",
            "   private void writeCensus (String address,int numPeople, int numMale, int numFemale, int  numE, int numF,",
            "                             int numOther  ) {",
            "     cendata.writeString(address);",
            "     cendata.writeInt(numPeople);",
            "     cendata.writeInt(numMale);",
            "     cendata.writeInt(numFemale);",
            "     cendata.writeInt(numE);",
            "     cendata.writeInt(numF);",
            "     cendata.writeInt(numOther);",
            "     cendata.newLine();",
            "   }",
            "   public static void main ( String[] args ) { Census c = new Census(); };",
            " }"
          ]
        }
      ]
    },
    {
      "name": "Steven",
      "files": [
        {
          "file": "Survey.java",
          "data": [
            " package Assign_6;",
            "",
            "",
            " import BasicIO.*;                // for IO classes",
            " import static BasicIO.Formats.*; // for field formats",
            " import static java.lang.Math.*;  // for math constants and functions",
            "",
            "",
            " /** This class ...",
            "   *",
            "   * @author <your name>",
            "   * @version 1.0 (<date>)                                                        */",
            "",
            " public class Survey {",
            "",
            "",
            "     private ASCIIDataFile  surData;",
            "     private ASCIIOutputFile   newsurData;",
            "     private BasicForm      household, person;",
            "     //private ReportPrinter  report;",
            "     /** This constructor ...                                                    */",
            "",
            "     public Survey ( ) {",
            "        String  adrs;  // address",
            "        String  Name;",
            "        int     button;",
            "        int     numPeople; // number of people",
            "        int     male;  //  sex of man",
            "        int     female;  //  sex of women",
            "        int     english; // language of english",
            "        int     french;  //  language of french",
            "        int     others;  //  others language",
            "",
            "",
            "        surData = new ASCIIDataFile();",
            "        newsurData = new ASCIIOutputFile();",
            "        household = new BasicForm(\"OK\",\"Skip\");",
            "        person = new BasicForm(\"OK\");",
            "        buildhousehold();",
            "        buildperson();",
            "        /*setUpReport();*/",
            "        //buildperson();",
            "       numPeople = 0;",
            "",
            "       //newsurData.writeString(\"\");",
            "      // newsurData.newLine();",
            "       for( ; ; ) {",
            "       male = 0;  // initial value of male",
            "       female = 0; // initial value of female",
            "       english = 0; // initial value of english",
            "       french = 0; // initial value of french",
            "       others = 0; // initial value of others",
            "",
            "            adrs = surData.readString();",
            "            if ( surData.isEOF()  ) break;",
            "            writeDetailhousehold(adrs, numPeople);",
            "            button =  household.accept();",
            "            if(button ==0) {",
            "            numPeople = household.readInt(\"members\");",
            "",
            "            for ( int i =1; i<= numPeople ; i++) {",
            "               person.clearAll();",
            "              // System.out.println(\"XXXXXXXXXXXXXXXXXXXXXXXXXXXX\");",
            "               person.writeInt(\"num\",i);",
            "               person.accept();",
            "               if(person.readInt(\"sex\")== 0){",
            "                  male = male + 1;",
            "               }",
            "               else {",
            "                  female = female + 1;",
            "               }",
            "               if (person.readInt(\"lang\") ==0) {",
            "                 english = english + 1;",
            "               } else if (person.readInt(\"lang\") == 1) {",
            "                 french = french +1;",
            "               }else {",
            "                  others = others + 1;",
            "               }",
            "",
            "",
            "",
            "            }",
            "            }",
            "            if(button == 0){",
            "            writesurData(adrs,numPeople,male,female,english,french,others);",
            "            }",
            "         }",
            "",
            "          household.close();",
            "          person.close();",
            "",
            "     }; // constructor",
            "",
            "",
            "",
            "",
            "     private void writeDetailhousehold(String adrs,int numPeople) {",
            "",
            "",
            "          household.writeString(\"addr\",adrs);",
            " //         household.writeInt(\"members\",numPeople);",
            "     }",
            "     private void  writeDetailperson(int male, int female, int english,int french,int others){",
            "          person.clearAll();",
            "          person.readInt(\"sex\");",
            "          person.readInt(\"lang\");",
            "     }",
            "",
            "        private void buildhousehold ( ) {",
            "",
            "         household.setTitle(\"Household\");",
            "         household.addTextField(\"addr\",\"Address\",20,10,10);",
            "         household.setEditable(\"addr\",false);",
            "         household.addTextField(\"members\",\"# People\",2,10,50);",
            "        }",
            "",
            "         private void buildperson () {",
            "         person.setTitle(\"Individual\");",
            "         person.addTextField(\"num\",\"Person\",2,10,10);",
            "         person.setEditable(\"num\",false);",
            "         person.addTextField(\"name\",\"Name\",20,10,50);",
            "         person.addTextField(\"age\",\"Age\",3,10,80);",
            "         person.addRadioButtons(\"sex\",\"Sex\",false,10,110,\"Male\",\"Female\");",
            "         person.addRadioButtons(\"lang\",\"Language\",false,10,160,",
            "                                \"English\",\"French\",\"Other\");",
            "",
            "     };  // buildForms",
            "",
            "",
            "       private void writesurData(String adrs, int numPeople,int male, int female, int english, int french, int others) {",
            "                   newsurData.writeString(adrs);",
            "                   newsurData.writeInt(numPeople);",
            "                   newsurData.writeInt(male);",
            "                   newsurData.writeInt(female);",
            "                   newsurData.writeInt(english);",
            "                   newsurData.writeInt(french);",
            "                   newsurData.writeInt(others);",
            "                   newsurData.newLine();",
            "",
            "       }",
            "",
            "",
            "     public static void main ( String[] args ) { Survey c = new Survey (); };",
            "",
            "",
            " } // <className>"
          ]
        }
      ]
    }
  ];
}

function similars() {

  return [
    {
      "name1": "T",
      "name2": "Melissa",
      "file1": "",
      "file2": "",
      "similar1": [3,5],
      "similar2": [4,5]
    }
  ];

}

// let data = dummyData();
// console.log("name 1 = " + name1[1].name);

