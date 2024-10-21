#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h> // Para el uso de sockets en Windows

#pragma comment(lib, "ws2_32.lib") // Necesario para vincular Winsock

int main() {
    WSADATA wsa;
    SOCKET sock;
    struct sockaddr_in servidor;
    char mensaje[1000], respuesta[1000];
    int tamano_respuesta;

    // Iniciar Winsock
    printf("Iniciando Winsock...\n");
    if (WSAStartup(MAKEWORD(2,2), &wsa) != 0) {
        printf("Error en la inicialización de Winsock. Código de error: %d\n", WSAGetLastError());
        return 1;
    }
    printf("Winsock inicializado.\n");

    // Crear el socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
        printf("No se pudo crear el socket. Código de error: %d\n", WSAGetLastError());
        WSACleanup();
        return 1;
    }

    servidor.sin_addr.s_addr = inet_addr("127.0.0.1"); // Dirección IP del servidor (localhost)
    servidor.sin_family = AF_INET;
    servidor.sin_port = htons(5000); // Puerto de conexión

    // Conectarse al servidor
    if (connect(sock, (struct sockaddr *)&servidor, sizeof(servidor)) < 0) {
        printf("Conexión fallida. Código de error: %d\n", WSAGetLastError());
        closesocket(sock);
        WSACleanup();
        return 1;
    }

    printf("Conectado al servidor\n");

    // Enviar un mensaje al servidor
    strcpy(mensaje, "Hola\n");
    if (send(sock, mensaje, strlen(mensaje), 0) < 0) {
        printf("No se pudo enviar el mensaje. Código de error: %d\n", WSAGetLastError());
        closesocket(sock);
        WSACleanup();
        return 1;
    }

    // Recibir la respuesta del servidor
    if ((tamano_respuesta = recv(sock, respuesta, sizeof(respuesta), 0)) == SOCKET_ERROR) {
        printf("No se pudo recibir la respuesta. Código de error: %d\n", WSAGetLastError());
        closesocket(sock);
        WSACleanup();
        return 1;
    }

    respuesta[tamano_respuesta] = '\0'; // Asegurarse de terminar la cadena
    printf("Respuesta del servidor: %s\n", respuesta);

    // Cerrar el socket
    closesocket(sock);
    WSACleanup(); // Limpiar Winsock

    return 0;
}
