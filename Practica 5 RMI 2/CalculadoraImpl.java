import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class CalculadoraImpl extends UnicastRemoteObject implements CalculadoraServicio {

    protected CalculadoraImpl() throws RemoteException {
        super();
    }

    @Override
    public float sumar(float a, float b) throws RemoteException {
        System.out.println("Conexión con el cliente exitosa: método sumar() invocado.");
        return a + b;
    }

    @Override
    public float restar(float a, float b) throws RemoteException {
        System.out.println("Conexión con el cliente exitosa: método restar() invocado.");
        return a - b;
    }

    @Override
    public float multiplicar(float a, float b) throws RemoteException {
        System.out.println("Conexión con el cliente exitosa: método multiplicar() invocado.");
        return a * b;
    }

    @Override
    public float dividir(float a, float b) throws RemoteException {
        System.out.println("Conexión con el cliente exitosa: método dividir() invocado.");
        if (b == 0) throw new ArithmeticException("División por cero");
        return a / b;
    }
}