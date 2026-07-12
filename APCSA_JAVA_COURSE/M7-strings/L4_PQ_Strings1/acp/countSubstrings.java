import java.util.HashMap;

public static void countSubstrings(String str, int k) {
    HashMap<String, Integer> map = new HashMap<>();

    for (int i = 0; i <= str.length() - k; i++) {
        String sub = str.substring(i, i + k);

        if (map.containsKey(sub)) {
            map.put(sub, map.get(sub) + 1);
        } else {
            map.put(sub, 1);
        }
    }

    for (String key : map.keySet()) {
        System.out.println(key + " -> " + map.get(key));
    }
}