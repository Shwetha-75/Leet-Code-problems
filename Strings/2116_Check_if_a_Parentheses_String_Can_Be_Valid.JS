var canBeValid = function(s, locked) {
    function helper(s){
        let stack=[];
        for(let char of s){
            if(stack && stack[stack.length-1]==='(' && char===')'){
                stack.pop();
            }
            else{
                stack.push(char)
            }
        }
        return stack.length===0 ? true : false;
    }
    if(helper(s)){
        return true 
    }
    else{
        let open=[],unlocked=[],n=s.length;
        for(let i=0;i<n;i++){
            if(locked[i]==='0'){
                unlocked.push(i)
            }
            else if(s[i]==='('){
                if(open){
                    open.push(i)
                }
            }
            else if(s[i]===')'){
                if(open) open.pop()
                else if(unlocked) unlocked.pop()
                else return false 
            }

        }
        while(open && unlocked && open[-1]<unlocked[-1]){
            open.pop();
            unlocked.pop()
        }
        if(open) return false 
        return true 
    }
};