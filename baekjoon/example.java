class example {
    public static void main(String[] args) {
        int n = 100;
        switch (n/10){
            case 10:
            case 9:
                System.out.println("A");
            case 8:
                System.out.println("b");
            case 7:
                System.out.println("c");
            default:
                System.out.println("F");
        }
    }
}
