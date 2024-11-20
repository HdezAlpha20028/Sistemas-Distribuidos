/*
 * This is sample code generated by rpcgen.
 * These are only templates and you can use them
 * as a guideline for developing your own functions.
 */
#include "Calculadora.h"
#include <stdio.h>

int * suma_1_svc(dupla_int *argp, struct svc_req *rqstp) {
    static int result;
    result = argp->a + argp->b;
    return &result;
}

int * resta_1_svc(dupla_int *argp, struct svc_req *rqstp) {
    static int result;
    result = argp->a - argp->b;
    return &result;
}

int * multiplica_1_svc(dupla_int *argp, struct svc_req *rqstp) {
    static int result;
    result = argp->a * argp->b;
    return &result;
}

int * divide_1_svc(dupla_int *argp, struct svc_req *rqstp) {
    static int result;
    if (argp->b == 0) {
        printf("Error: División por cero.\n");
        result = 0;
    } else {
        result = argp->a / argp->b;
    }
    return &result;
}