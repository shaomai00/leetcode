public class Solution {
    //不能直接用string操作 会超时 必须转换成char型
public String reverseString(String s) {
        char[] result = new char[s.length()];  
        int index = 0;  
        for (int i = s.length() - 1; i >= 0; i--) {  
            result[index++] = s.charAt(i);  
        }  
        return new String(result);  
    }
}