
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    stages: [
        { duration: '30s', target: 10 },
        { duration: '1m', target: 30 },
        { duration: '30s', target: 50 },
        { duration: '30s', target: 0 },
    ],
};

export default function () {
    const respuesta = http.get('http://localhost:8080/');

    check(respuesta, {
        'estado HTTP es 200': (r) => r.status === 200,
        'respuesta contiene instancia': (r) =>
            r.body.includes('Backend-'),
    });

    sleep(1);
}
