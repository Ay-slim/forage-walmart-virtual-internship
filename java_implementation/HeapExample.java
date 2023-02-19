import java_implementation.Heap;
public class HeapExample{
  public static void main(String[] args){
    System.out.println("pring something");
    Heap<Integer> sampleHeap = new Heap<Integer>(2);
    sampleHeap.insert(15);
    sampleHeap.insert(8);
    sampleHeap.insert(9);
    sampleHeap.insert(7);
    sampleHeap.insert(4);
    sampleHeap.insert(3);
    sampleHeap.insert(1);
    sampleHeap.insert(2);
    System.out.println(sampleHeap.getData());
    sampleHeap.popMax();
    System.out.println(sampleHeap.getData());
    // for (int i = 0; i < sampleHeap.getData(); i++) {
    //   System.out.println(sampleHeap.data.get(i));
    // }
  }
}