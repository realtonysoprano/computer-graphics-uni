/*
Манташев А.У. М8О-305Б-20
Лабораторная работа №3.
Задание: 
Используя результаты Л.Р. №2, аппроксимировать заданное тело выпуклым многогранником. Точность 
аппроксимации задается пользователем. Обеспечить возможность вращения и масштабирования многогранника и 
удаление невидимых линий и поверхностей. Реализовать простую модель закраски для случая одного источника света.
Параметры освещения и отражающие свойства материала задаются пользователем в диалоговом режиме.
Вариант 12: 
Прямой круговой цилиндр.
 */

'use strict'
let WIDTH = 1200, HEIGHT = 800;

function drawCylinder(h, r, x, y, z) {
	let step = int(document.getElementById('approx').value);

	for (var fi = 0; fi < 360; fi += step) { // array of vertices
		beginShape();
		vertex(x, y + h / 2, z);
		vertex(x + cos(fi / 360 * 2 * PI) * r,
			y + h / 2,
			z + sin(fi / 360 * 2 * PI) * r);
		vertex(x + cos((fi + step) / 360 * 2 * PI) * r,
			y + h / 2,
			z + sin((fi + step) / 360 * 2 * PI) * r);
		endShape(); // соединение вершин в одну плоскость

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
	background(200);
	debugMode(AXES);
}

function draw() {
	stroke(0, 0, 0);
	strokeWeight(2);
	background('black');
	ambientLight(100);									//создает свет

	let x1 = map(mouseX, 0, WIDTH, -200, 200);
	let x2 = map(mouseY, 0, HEIGHT, 200, -200);

	directionalLight(100, 100, 100, x1, x2, 300);		//создает направленный свет
	ambientMaterial('blue');
	orbitControl();
	drawCylinder(260, 100, 0, 0, 0);
}