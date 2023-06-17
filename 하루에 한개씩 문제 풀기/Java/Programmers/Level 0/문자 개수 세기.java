import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        int[] counts = new int[52]; // 알파벳 개수를 저장할 배열 초기화

        for (char c : my_string.toCharArray()) {
            if (c >= 'A' && c <= 'Z') { // 대문자인 경우
                int index = c - 'A'; // 알파벳의 인덱스 계산
                counts[index]++; // 개수 증가
            } else if (c >= 'a' && c <= 'z') { // 소문자인 경우
                int index = c - 'a' + 26; // 알파벳의 인덱스 계산
                counts[index]++; // 개수 증가
            }
        }

        return counts;
    }
}