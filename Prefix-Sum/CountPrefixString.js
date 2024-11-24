const method=(words,s)=>{
    let count=0;
    for(let i=0;i<words.length;i++){
        let n=words[i].length;
        if(s.slice(0,n)===words[i]) count++;
    }
    return count;
}

