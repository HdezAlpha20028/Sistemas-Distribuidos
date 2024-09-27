import java.io.*;
import java.net.*;

public class cliente {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 8888);
             DataInputStream in = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {

            System.out.println("Conectado al servidor.");

            while (true) {
                System.out.print("Introduce un número entero (0 para terminar): ");
                int num = Integer.parseInt(reader.readLine());

                out.writeInt(num);  // Enviar número al servidor

                if (num == 0) {
                    break;
                }

                int respuesta = in.readInt();  // Leer respuesta del servidor
                System.out.println("Respuesta del servidor: " + respuesta);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
