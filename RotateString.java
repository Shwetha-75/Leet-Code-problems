class RotateString{
    public static void main(String[] args) {
        String input="abcde";
        String goal="cdeab";
        RotateString rotate=new RotateString();
        boolean result=rotate.checkRotateString(input, goal);
        System.out.println(result);
    }
    boolean checkRotateString(String input,String goal)
    {
        StringBuffer temp=new StringBuffer(input);
       
        char ch=temp.charAt(0);
        temp=temp.replace(0, 1, "");
        
        temp.append(ch);
     
        while(!(temp.equals(input)))
        {
            System.out.println(temp);
           
            if(temp.toString().equals(goal)) return true;
            char ch1=temp.charAt(0);
            temp.replace(0, 1, "");
            temp.append(ch1);
        }
        return false;
    }
}