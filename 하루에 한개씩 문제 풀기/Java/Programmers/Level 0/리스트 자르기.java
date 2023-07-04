import java.util.ArrayList;
import java.util.List;

class Solution {
    public static int[] solution(int n, int[] slicer, int[] numList) {
        int a = slicer[0];
        int b = slicer[1];
        int c = slicer[2];

        List<Integer> resultList = new ArrayList<>();

        switch (n) {
            case 1:
                for (int i = 0; i <= b; i++) {
                    resultList.add(numList[i]);
                }
                break;
            case 2:
                for (int i = a; i < numList.length; i++) {
                    resultList.add(numList[i]);
                }
                break;
            case 3:
                for (int i = a; i <= b; i++) {
                    resultList.add(numList[i]);
                }
                break;
            case 4:
                for (int i = a; i <= b; i += c) {
                    resultList.add(numList[i]);
                }
                break;
        }

        int[] result = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            result[i] = resultList.get(i);
        }
        return result;
    }
}