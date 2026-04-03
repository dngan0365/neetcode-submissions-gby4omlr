static class Singleton {
    private static Singleton uniqueInstance = null;
    private String str = null;
    private Singleton() {
        this.str = null;
    }

    public static Singleton getInstance() {
        if (uniqueInstance == null){
            uniqueInstance = new Singleton();
        }
        return uniqueInstance;
    }

    public String getValue() {
        return uniqueInstance.str;
    }

    public void setValue(String value) {
        uniqueInstance.str = value;
    }
    
}
