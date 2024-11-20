import java.rmi.Naming;
import java.util.Scanner;

public class CalculadoraCliente {
    public static void main(String[] args) {
        try {
            // Localizar el servicio en el registro RMI usando la IP del servidor
            CalculadoraServicio calculadora = (CalculadoraServicio) Naming.lookup("rmi://10.86.15.247/CalculadoraServicio");

            Scanner scanner = new Scanner(System.in);

            System.out.print("Ingresa el primer número: ");
            float a = scanner.nextFloat();

            System.out.print("Ingresa el segundo número: ");
            float b = scanner.nextFloat();

            System.out.println("Selecciona la operación:");
            System.out.println("1. Sumar");
            System.out.println("2. Restar");
            System.out.println("3. Multiplicar");
            System.out.println("4. Dividir");

            int opcion = scanner.nextInt();
            float resultado = 0;

            switch (opcion) {
                case 1:
                    resultado = calculadora.sumar(a, b);
                    System.out.println("Resultado de la suma: " + resultado);
                    break;
                case 2:
                    resultado = calculadora.restar(a, b);
                    System.out.println("Resultado de la resta: " + resultado);
                    break;
                case 3:
                    resultado = calculadora.multiplicar(a, b);
                    System.out.println("Resultado de la multiplicación: " + resultado);
                    break;
                case 4:
                    resultado = calculadora.dividir(a, b);
                    System.out.println("Resultado de la división: " + resultado);
                    break;
                default:
                    System.out.println("Opción no válida.");
                    break;
            }

            scanner.close();

        } catch (Exception e) {
            System.err.println("Error en el cliente RMI: " + e.getMessage());
            e.printStackTrace();
        }
    }
}

