public class Solution {
    //����ֱ����string���� �ᳬʱ ����ת����char��
public String reverseString(String s) {
        char[] result = new char[s.length()];  
        int index = 0;  
        for (int i = s.length() - 1; i >= 0; i--) {  
            result[index++] = s.charAt(i);  
        }  
        return new String(result);  
    }
}