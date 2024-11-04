var element=(word)=>{
    let comp=new Array();
    let index=1;
    let result='';
    comp.push(word.charAt(0));
    while(index<word.length)
    {
        if(comp.length==9 || comp.some(element=>element!==word[index]))
        {
            result+=comp.length.toString()+comp[0];
            comp=new Array();

        }
        comp.push(word[index]);
        index+=1
    

    }
    if(comp.length!==0){
        result+=comp.length.toString()+comp[0]
    }

    return result;
}

function main(){
    var result=element("aaabbbcccccccccddddd");
    console.log(result);
}
main()