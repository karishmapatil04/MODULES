import java.util.ArrayList;

public static ArrayList<String> findUniqueElements(ArrayList<String> list) {

    ArrayList<String> uniqueList = new ArrayList<>();

    for (String item : list) {
        if (!uniqueList.contains(item)) {
            uniqueList.add(item);
        }
    }

    return uniqueList;
}