// Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

// You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

// Example 1:

// Input: name = "alex", typed = "aaleex"
// Output: true
// Explanation: 'a' and 'e' in 'alex' were long pressed.
// Example 2:

// Input: name = "saeed", typed = "ssaaedd"
// Output: false
// Explanation: 'e' must have been pressed twice, but it was not in the typed output.


class LongPressedName{
    public static void main(String[] args) {
        
    }

    public static boolean isLongPressedName(String name,String typed){
        int index1=0,index2=0;
        char prev=name.charAt(0);
        while(index1<name.length() && index2<typed.length()){
            if(name.charAt(index1)==typed.charAt(index2)){
                prev=name.charAt(index1);
                index1++;
                index2++;

            }
            else if(typed.charAt(index2)==prev){
                index2++;
            }
            else{
                return false;
            }
    }

    while(index2<typed.length()){
         if(prev!=typed.charAt(index2)) return false;
    }
    return index1<name.length() || index2<typed.length() ? false : true;
}
}