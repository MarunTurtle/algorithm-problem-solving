public class Solution {
    public String[] solution(String[] names) {
        
        int len = names.length;
        String[] result = new String[(len - 1 + 5)/5];
        
        for(int i = 0, j = 0; i < len; i++) {
            if (i % 5 == 0) {
                result[j++] = names[i];
            }
        }
        
        return result;
    }
}