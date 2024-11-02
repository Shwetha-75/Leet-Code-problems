var result=(string)=>{
    let array=string.split(" ");
    if (array.length===1)
    {
        return string.charAt(0)===string.charAt(string.length-1);
    }
    for(let i=0;i<array.length-1;i++){
      if(i===0){
        if(array[i].charAt(0)!==array[array.length-1].charAt(array[array.length-1].length-1))
        {
            return false;
        }
      }

      if(array[i].charAt(array[i].length-1)!==array[i+1].charAt(0))
      {
        return false
      }
    }
    return true;
}

var element=result("Leetcode is cool")
console.log(element )