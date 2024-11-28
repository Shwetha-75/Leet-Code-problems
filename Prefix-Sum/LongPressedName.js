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
 

// Constraints:

// 1 <= name.length, typed.length <= 1000
// name and typed consist of only lowercase English letters.

const result=(name,typed)=>{
    let index1=0;
    let index2=0;
    let prev=name[0]
    while(index1<name.length && index2<typed.length){
        if(name[index1]===typed[index2]){
            prev=name[index1];
            index1++;
            index2++;
            

        }
        else if(typed[index2]===prev){
            index2++;
        }
        else{
            return false;
        }
    }

    while(index2<typed.length){
        if(typed[index2]!==prev){
            return false;
        }
        index2++;
    };
    return index1<name.length || index2<typed.length ? false : true;
}

function main(){
    const res=result("alex","aaleex");
    console.log(res);
}
main()
