let scale = 20; // game scale
let mapSize = 40; // map size

// player location
let px = Math.floor(mapSize/2);
let py = Math.floor(mapSize/2);

// velocity of movement
let xv = 0
let yv = 0;

let trail = []; // actual tail
let tail = 3; // tail length

// starting fruit position
let fruitX = Math.floor(Math.random()*mapSize);
let fruitY = Math.floor(Math.random()*mapSize); 

// setting up game board
const camvas = document.getElementById("canvas");
const tailCounter = document.getElementById("counter");
camvas.setAttribute("width",(mapSize*scale));
camvas.setAttribute("height",(mapSize*scale));
let field = camvas.getContext("2d");

// game loop
function game() {
    px += xv;
    py += yv;

    // going out of bounderies
    if(px < 0){
        px = mapSize-1;
    }
    if(px > mapSize-1){
        px = 0;
    }
    if(py < 0){
        py = mapSize-1;
    }
    if(py > mapSize-1){
        py = 0;
    }

    // set backgound to black
    field.fillStyle = "black";
    field.fillRect(0,0,camvas.width,camvas.height);

    // drawing the tail
    field.fillStyle = "lime";
    for(var i=0; i < trail.length; i++) {
        field.fillRect(trail[i].x*scale, trail[i].y*scale, scale-2, scale-2);

        // if tail touches head, reset tail
        if(trail[i].x == px && trail[i].y == py) {
            tail = 3;
            tailCounter.innerText = "Tail length: " + tail;
        }
    }

    // snake is essentially going in reverse
    // push a new head at the "end"
    // remove the unwanted tail
    trail.push({x:px,y:py});
    while(trail.length > tail) {
        trail.shift();
    }

    // did snake head find the fruit
    if(fruitX == px && fruitY == py) {
        tail++;
        fruitX = Math.floor(Math.random()*mapSize);
        fruitY = Math.floor(Math.random()*mapSize);
        tailCounter.innerText = "Tail length: " + tail;
    }

    // drawing the fruit
    field.fillStyle = "red";
    field.fillRect(fruitX*scale, fruitY*scale, scale-2, scale-2);
}

// key push registering
// https://www.freecodecamp.org/news/javascript-keycode-list-keypress-event-key-codes/ (numbered list of keys)
function keyPush(evt) {
    switch(evt.keyCode) {
        case 37:
            xv = -1;
            yv = 0;
            break;
        case 38:
            xv = 0;
            yv = -1;
            break;
        case 39:
            xv = 1;
            yv = 0;
            break;
        case 40:
            xv = 0;
            yv = 1;
            break;
    }
}

document.addEventListener("keydown",keyPush);
setInterval(game,1000/15);
