public class Solution {
    public static String solution(String myString, int[] indices) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < myString.length(); i++) {
            if (!contains(indices, i)) {
                result.append(myString.charAt(i));
            }
        }
        return result.toString();
    }

    public static boolean contains(int[] arr, int target) {
        for (int num : arr) {
            if (num == target) {
                return true;
            }
        }
        return false;
    }
}
