/*
Манташев А.У. М8О-305Б-20
Лабораторная работа №6.
Задание: 
Для поверхности, созданной в л.р. №5, обеспечить выполнение следующего шейдерного эффекта
Вариант: 
Анимация. Координата Y изменяется по закону Y = Y*cos(t+Y)
 */

'use strict'

let WIDTH = 1200, HEIGHT = 800;

function drawCylinder(h, r, x, y, z) {
    let step = Math.floor(360 / int(document.getElementById('approx').value));

    y = y * cos(frameCount * 0.1 + y);

    for (var fi = 0; fi < 360; fi += step) { // вершины
        beginShape();
        vertex(x, y + h / 2, z);
        vertex(x + cos(fi / 360 * 2 * PI) * r,
            y + h / 2,
            z + sin(fi / 360 * 2 * PI) * r);
        vertex(x + cos((fi + step) / 360 * 2 * PI) * r,
            y + h / 2,
            z + sin((fi + step) / 360 * 2 * PI) * r);
        endShape();             // соединение вершин в одну плоскость

        beginShape();
        vertex(x, y - h / 2, z);
        vertex(x + cos(fi / 360 * 2 * PI) * r,
            y - h / 2,
            z + sin(fi / 360 * 2 * PI) * r);
        vertex(x + cos((fi + step) / 360 * 2 * PI) * r,
            y - h / 2,
            z + sin((fi + step) / 360 * 2 * PI) * r);
        endShape();

        beginShape();
        vertex(x + cos(fi / 360 * 2 * PI) * r,
            y - h / 2,
            z + sin(fi / 360 * 2 * PI) * r);

        vertex(x + cos(fi / 360 * 2 * PI) * r,
            y + h / 2,
            z + sin(fi / 360 * 2 * PI) * r);

        vertex(x + cos((fi + step) / 360 * 2 * PI) * r,
            y + h / 2,
            z + sin((fi + step) / 360 * 2 * PI) * r);

        vertex(x + cos((fi + step) / 360 * 2 * PI) * r,
            y - h / 2,
            z + sin((fi + step) / 360 * 2 * PI) * r);

        endShape();
    }
}

function setup() {							//создаем поле для изображения фигуры
    createCanvas(WIDTH, HEIGHT, WEBGL);
    background(0, 0, 0);
    debugMode(AXES);
}

function draw() {
    stroke(0, 0, 0);
    strokeWeight(1);
    background(0, 0, 0);
    ambientLight(100);									//создает свет

    let x1 = map(mouseX, 0, WIDTH, -200, 200);
    let x2 = map(mouseY, 0, HEIGHT, 200, -200);

    directionalLight(100, 100, 100, x1, x2, 200);   //создает направленный свет
    ambientMaterial(0, 0, 255);
    orbitControl();

    drawCylinder(300, 100, 0, 100, 0);

}