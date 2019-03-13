
// this will build the list of assignments that a course has
function listOfAssignments(course) {

   // when they choose a course, get the list of assignments from here
   switch(course) {
      case "cosc1p02":
         return c1p02();
      case "cosc1p03":
         return c1p03();
      case "cosc2p03":
         return c2p03();
   }

}

function c1p02() {

   let arr = [];
   for (let i = 0; i < 4; i++) {
      arr[i] = (i + 1);
   }

   return arr;
}