#include <stdio.h>
#include <winsock2.h>

#pragma comment(lib, "ws2_32.lib") // Librería para Winsock

int main() {
    WSADATA wsa;
    SOCKET server_socket, client_socket;
    struct sockaddr_in server_addr, client_addr;
    int client_len, num;

    // Inicialización de Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        printf("Error al inicializar Winsock. Código: %d\n", WSAGetLastError());
        return 1;
    }

    // Crear socket
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == INVALID_SOCKET) {
        printf("No se pudo crear el socket. Código: %d\n", WSAGetLastError());
        WSACleanup();
        return 1;
    }

    // Configuración del servidor
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(8888);

    // Enlazar socket
    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) == SOCKET_ERROR) {
        printf("Error en bind. Código: %d\n", WSAGetLastError());
        closesocket(server_socket);
        WSACleanup();
        return 1;
    }

    // Escuchar conexiones
    listen(server_socket, 3);

    printf("Esperando conexiones...\n");
    client_len = sizeof(client_addr);
    client_socket = accept(server_socket, (struct sockaddr *)&client_addr, &client_len);
    if (client_socket == INVALID_SOCKET) {
        printf("Fallo en aceptar conexión. Código: %d\n", WSAGetLastError());
        closesocket(server_socket);
        WSACleanup();
        return 1;
    }

    printf("Cliente conectado.\n");

    // Bucle para recibir números
    while (1) {
        int recv_result = recv(client_socket, (char *)&num, sizeof(num), 0);
        if (recv_result == SOCKET_ERROR) {
            printf("Error al recibir datos. Código: %d\n", WSAGetLastError());
            break;
        }

        num = ntohl(num); // Convertir a formato de host
        if (num == 0) {
            printf("El cliente envió un 0. Terminando...\n");
            break;
        }

        printf("Número recibido: %d\n", num);
        num += 1;
        num = htonl(num); // Convertir a formato de red

        send(client_socket, (char *)&num, sizeof(num), 0);
    }

    // Cerrar sockets y limpiar Winsock
    closesocket(client_socket);
    closesocket(server_socket);
    WSACleanup();

    return 0;
}
