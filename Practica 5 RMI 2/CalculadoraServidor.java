import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class CalculadoraServidor {
    public static void main(String[] args) {
        try {
            // Configura la IP que el servidor RMI utilizará para comunicarse
            System.setProperty("java.rmi.server.hostname", "10.86.15.247"); // Asegúrate de que la IP esté entre comillas

            // Crear el registro RMI en el puerto 1099
            Registry registry = LocateRegistry.createRegistry(1099);

            // Crear e instanciar el objeto remoto
            CalculadoraImpl calculadora = new CalculadoraImpl();

            // Registrar el objeto remoto en el registro con un nombre descriptivo
            registry.rebind("CalculadoraServicio", calculadora);

            System.out.println("Servidor RMI iniciado y listo para conexiones.");
        } catch (Exception e) {
            System.err.println("Error en el servidor RMI: " + e.toString());
            e.printStackTrace();
        }
    }
}

