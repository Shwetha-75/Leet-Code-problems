const method=(sentence,searchWord)=>{
    const result=sentence.split(" ");
    for(let i=0;i<result.length;i++){
        if(result[i].startsWith(searchWord)){
            return i+1;
        }
    }
    return -1;
};

function main(){
    const result=method("i love eating burger","burg");
    console.log(result);
}
main()