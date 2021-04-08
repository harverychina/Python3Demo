package answerquestion.flatten;

import java.util.ArrayList;

public class FlattenNestedArrays {
  public static void main (String[] args) {
    Object[] array = {1, 2, new Object[] {3, 4, new Object[] {5, new Object[] {new Object[] {6}}}, 7}, 8, 9, 10};
    System.out.println(flatten(array).toString());

  }
  public static ArrayList<Integer> flatten(Object[] arr) {
    ArrayList<Integer> res = new ArrayList<>();
    for (Object item: arr) {
        if (item.getClass().isArray()) {
            res.addAll(flatten((Object[]) item));
        }
        else {
            res.add((Integer) item);
        }
    }
    return res;
  }
}
