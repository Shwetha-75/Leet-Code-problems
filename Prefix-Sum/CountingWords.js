const element=(words,pref)=>{
    let counter=0;
    for(let i=0;i<words.length;i++){
        if(words[i].startsWith(words[i],pref)){
            counter++;
        }
    }
    return counter;
}