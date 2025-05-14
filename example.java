public abstract class example {
    protected String systemName;
    protected String apiUrl;
    protected String authToken;

    public example(String systemName, String apiUrl, String authToken) {
        this.systemName = systemName;
        this.apiUrl = apiUrl;
        this.authToken = authToken;
    }

    // Общий метод: инициализация соединения
    public void initialize() {
        System.out.println("Initializing connection to " + systemName + " at " + apiUrl);
        authenticate();
    }

    // Общий метод: аутентификация
    protected abstract void authenticate();

    // Метод для загрузки товаров из ERP
    public abstract void fetchProducts();

    // Метод для отправки заказа в ERP
    public abstract void sendOrder(Order order);

    // Метод для обновления остатков
    public abstract void syncStock();

    // Общий метод: логирование
    protected void log(String message) {
        System.out.println("[" + systemName + "] " + message);
    }
}



public class OneCIntegrator extends example {
    public OneCIntegrator(String apiUrl, String authToken) {
        super("1C", apiUrl, authToken);
    }

    @Override
    protected void authenticate() {
        // Пример авторизации для 1C
        log("Authenticating with token: " + authToken);
    }

    @Override
    public void fetchProducts() {
        log("Fetching products from 1C via " + apiUrl);
        // Логика запроса к API 1C
    }

    @Override
    public void sendOrder(Order order) {
        log("Sending order to 1C: " + order.getId());
        // Логика отправки заказа
    }

    @Override
    public void syncStock() {
        log("Syncing stock with 1C");
        // Логика обновления остатков
    }
}



public class Order {
    private String id;
    private double totalAmount;

    public Order(String id, double totalAmount) {
        this.id = id;
        this.totalAmount = totalAmount;
    }

    public String getId() {
        return id;
    }

    public double getTotalAmount() {
        return totalAmount;
    }
}



public class SAPIntegrator extends example {
    // Реализация под SAP
}

public class CustomCMSOIntegrator extends example {
    // Реализация под кастомную ERP
}
