package hello.core.singleton;

public class StatefulService {
    /**
     * 싱글톤에서 공유필드를 사용하면 같은 자원에 다른 쓰레드가 접근하여 값이 바뀔수 있다.
     */
//    private int price;  // 상태를 유지하는 필드

//    public void order(String name, int price) {
//        System.out.println("name: " + name + " price: " + price);
//        this.price = price;
//    }

//    public int getPrice() {
//        return price;
//    }

    /**
     * 공유 필드 없이 구현
     */
    public int order(String name, int price){
        System.out.println("name: " + name + " price: " + price);
        return price;
    }
}
