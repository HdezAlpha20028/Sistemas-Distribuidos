import java.io.*;
import java.net.*;

public class Servidor {
    public static void main(String[] args) {
        try {
            // Crear socket de servidor escuchando en el puerto 5000
            ServerSocket serverSocket = new ServerSocket(5000);
            System.out.println("Servidor iniciado, esperando conexión...");

            // Aceptar la conexión del cliente
            Socket socket = serverSocket.accept();
            System.out.println("Cliente conectado.");

            // Crear canales de entrada y salida
            BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter salida = new PrintWriter(socket.getOutputStream(), true);

            // Leer el mensaje del cliente
            String mensajeCliente = entrada.readLine();
            System.out.println("Cliente dice: " + mensajeCliente);

            // Enviar una respuesta al cliente
            String mensajeServidor = "Hola, ¿qué tal?";
            salida.println(mensajeServidor);
            System.out.println("Mensaje enviado al cliente: " + mensajeServidor);

            // Cerrar los streams y socket
            entrada.close();
            salida.close();
            socket.close();
            serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
